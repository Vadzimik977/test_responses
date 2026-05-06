#!/usr/bin/env python3
"""
Скрипт для проверки кеширования моделей через Responses API.

Тестирует sticky credential behavior:
- Turn 1: создаем response без previous_response_id
- Turn 2: создаем response с previous_response_id (должен использовать тот же credential)

Usage:
    python test_cache.py --api-key YOUR_KEY --model openai/gpt-4o
    
    python test_cache.py --api-key YOUR_KEY --list-models
    
    python test_cache.py --api-key YOUR_KEY --test-all
"""

import argparse
import json
import os
import time
import requests
from datetime import datetime
from openai import OpenAI


LLM_MODELS = [
     "xiaomi/mimo-v2.5-pro",
    "moonshotai/kimi-k2.6",
    "qwen/qwen3.6-max-preview",
    "qwen/qwen3.6-flash",
    "qwen/qwen3.6-35b-a3b",
    "qwen/qwen3-coder-next",
    "qwen/qwen3-vl-plus",
    "z-ai/glm-4.6v-flashx",
    "yandex/gpt5-pro",
    "z-ai/glm-4.7",
    "qwen/qwen3-vl-8b-instruct",
    "openai/gpt-5.1-chat",
    "qwen/qwen3-vl-flash",
    "openai/gpt-5.1",
    "z-ai/glm-4.5-air",
    "openai/gpt-4.1",
    "openai/gpt-5-mini",
    "deepseek/deepseek-v3.2",
    "z-ai/glm-4.6v-flash",
    "qwen/qwen3-vl-30b-a3b-thinking",
    "anthropic/claude-sonnet-4",
    "openai/gpt-5.2-chat",
    "openai/gpt-5-chat",
    "openai/gpt-4.1-mini",
    "openai/gpt-4.1-nano",
    "openai/chatgpt-4o-latest",
    "openai/gpt-oss-120b",
    "openai/gpt-oss-20b",
    "google/gemini-2.5-pro",
    "qwen/qwen3-vl-235b-a22b-instruct",
    "openai/gpt-5.4-nano",
    "moonshotai/kimi-k2-0905",
    "qwen/qwen3.5-plus",
    "deepseek/deepseek-r1-distill-llama-70b",
    "google/gemini-3-flash-preview",
    "google/gemini-2.5-flash",
    "qwen/qwen3-vl-30b-a3b-instruct",
    "qwen/qwen3-vl-8b-thinking",
    "qwen/qwen3.5-flash",
    "qwen/qwen3.5-397b-a17b",
    "yandex/gpt5.1-pro",
    "yandex/gpt5-lite",
    "anthropic/claude-haiku-4.5",
    "openai/gpt-5.2",
    "z-ai/glm-4.6",
    "qwen/qwen3-max-thinking",
    "anthropic/claude-opus-4.5",
    "openai/gpt-5.4",
    "GigaChat/GigaChat-2-Max",
    "google/gemini-3.1-flash-lite-preview",
    "anthropic/claude-sonnet-4.5",
    "anthropic/claude-opus-4.7",
    "openai/gpt-5.3-chat",
    "meta-llama/llama-3.3-70b-instruct",
    "x-ai/grok-code-fast-1",
    "google/gemini-3.1-pro-preview",
    "openai/gpt-5.4-mini",
    "qwen/qwen3-235b-a22b",
    "t-tech/T-pro-it-2.0",
    "google/gemini-3.1-pro-preview-customtools",
    "xiaomi/mimo-v2-omni",
    "qwen/qwen3-vl-235b-a22b-thinking",
    "z-ai/glm-5.1",
    "anthropic/claude-sonnet-4.6",
    "anthropic/claude-opus-4.6",
    "xiaomi/mimo-v2.5",
    "xiaomi/mimo-v2-flash",
    "deepseek/deepseek-v3.2-speciale",
    "deepseek/deepseek-v4-pro",
    "anthropic/claude-opus-4.1",
    "qwen/qwen3.6-plus",
    "openai/gpt-5.4-pro",
    "openai/gpt-4o-mini",
    "deepseek/deepseek-v4-flash",
    "openai/gpt-5.3-codex",
    "openai/gpt-5.2-codex",
    "openai/gpt-5",
    "openai/gpt-5-nano",
    "moonshotai/kimi-k2.5",
    "xiaomi/mimo-v2-pro",
    "z-ai/glm-5",
    "z-ai/glm-4.7-flash",
    "z-ai/glm-4.6v",
    "openai/gpt-5.5",
    "deepseek/deepseek-chat-v3-0324",
]


def get_llm_models_from_provider(api_key: str, base_url: str = "https://api.vsellm.ru/v1"):
    """Return hardcoded list of LLM models."""
    return LLM_MODELS.copy()


def to_json_serializable(obj):
    """Convert any object to JSON-serializable format."""
    if obj is None:
        return None
    if isinstance(obj, (str, int, float, bool)):
        return obj
    if isinstance(obj, (list, tuple)):
        return [to_json_serializable(item) for item in obj]
    if isinstance(obj, dict):
        return {k: to_json_serializable(v) for k, v in obj.items()}
    
 
    if hasattr(obj, "__dict__"):
        return to_json_serializable(obj.__dict__)
    
  
    if hasattr(obj, "_asdict"):
        return to_json_serializable(obj._asdict())
    
    return str(obj)


def response_to_dict(response):
    """Convert OpenAI response object to dictionary."""
    result = {
        "id": getattr(response, "id", None),
        "model": getattr(response, "model", None),
        "object": getattr(response, "object", None),
        "created_at": getattr(response, "created_at", None),
        "output_text": getattr(response, "output_text", None),
    }
    
    try:
        if hasattr(response, "usage") and response.usage:
            usage = response.usage
            result["usage"] = {}
            if hasattr(usage, "input_tokens"):
                result["usage"]["input_tokens"] = usage.input_tokens
            if hasattr(usage, "output_tokens"):
                result["usage"]["output_tokens"] = usage.output_tokens
            if hasattr(usage, "total_tokens"):
                result["usage"]["total_tokens"] = usage.total_tokens
            if hasattr(usage, "cached_tokens"):
                result["usage"]["cached_tokens"] = usage.cached_tokens
            if hasattr(usage, "input_tokens_details") and usage.input_tokens_details:
                result["usage"]["input_tokens_details"] = to_json_serializable(usage.input_tokens_details)
            if hasattr(usage, "output_tokens_details") and usage.output_tokens_details:
                result["usage"]["output_tokens_details"] = to_json_serializable(usage.output_tokens_details)
    except Exception as e:
        result["usage_error"] = str(e)
    

    try:
        if hasattr(response, "output") and response.output:
            result["output"] = []
            for item in response.output:
                item_dict = {}
                if hasattr(item, "type"):
                    item_dict["type"] = item.type
                if hasattr(item, "content"):
                    item_dict["content"] = []
                    for content in item.content:
                        content_dict = {}
                        if hasattr(content, "type"):
                            content_dict["type"] = content.type
                        if hasattr(content, "text"):
                            content_dict["text"] = content.text
                        item_dict["content"].append(content_dict)
                result["output"].append(item_dict)
    except Exception:
        pass
    
    return result


def save_responses_json(model: str, r1, r2, output_dir: str = "test_cache_responses"):
    """Save both responses to JSON files."""
    os.makedirs(output_dir, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_model = model.replace("/", "_")
    
    data = {
        "model": model,
        "timestamp": timestamp,
        "test_type": "responses_api_cache_test",
        "turn_1": response_to_dict(r1),
        "turn_2": response_to_dict(r2),
        "analysis": {
            "same_model_used": getattr(r1, "model", None) == getattr(r2, "model", None),
            "previous_response_id_used": getattr(r2, "previous_response_id", None) == getattr(r1, "id", None),
            "context_referenced": "joke" in getattr(r2, "output_text", "").lower(),
        }
    }
    
    filename = f"{safe_model}_{timestamp}.json"
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"  💾 Responses saved to: {filepath}")
    return filepath


def generate_markdown_report(results: list, responses_dir: str, output_file: str = "test_cache_report.md"):
    """Generate Markdown report from test results."""
    
    total = len(results)
    passed = sum(1 for _, success, _, _ in results if success)
    failed = total - passed
    
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    
    md_content = f"""# Отчет тестирования кеширования Responses API

**Дата:** {timestamp}  
**Всего моделей:** {total}  
**Успешно:** {passed} ✅  
**Ошибок:** {failed} ❌  
**Директория с JSON:** `{responses_dir}/`

---

## Сводка

| Модель | Статус | Ошибка | JSON файл |
|--------|--------|--------|-----------|
"""
    
    for model, success, error_msg, json_file in results:
        status = "✅ OK" if success else "❌ FAILED"
        error = error_msg if error_msg else "-"
        json_link = f"[{os.path.basename(json_file)}]({json_file})" if json_file else "-"
        md_content += f"| `{model}` | {status} | {error} | {json_link} |\n"
    
    md_content += f"""

---

## Подробные результаты

"""
    
    for model, success, error_msg, json_file in results:
        md_content += f"""### {model}

- **Статус:** {"✅ Успешно" if success else "❌ Ошибка"}
- **JSON файл:** `{json_file if json_file else "N/A"}`
"""
        if error_msg:
            md_content += f"- **Ошибка:** `{error_msg}`\n"
        md_content += "\n"
    
    md_content += f"""
---

## Структура JSON

Каждый JSON-файл содержит:

- `model` - тестируемая модель
- `timestamp` - время теста
- `turn_1` - первый response (без previous_response_id)
- `turn_2` - второй response (с previous_response_id)
- `analysis` - автоматический анализ:
  - `same_model_used` - использовалась ли одна модель в обоих запросах
  - `previous_response_id_used` - передан ли previous_response_id корректно
  - `context_referenced` - упоминается ли шутка во втором ответе

### Поля usage

В `turn_1.usage` и `turn_2.usage` проверьте наличие:
- `cached_tokens` - количество закешированных токенов
- `input_tokens_details.cached_tokens` - детали по кешу

---

*Сгенерировано автоматически скриптом test_cache.py*
"""
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(md_content)
    
    print(f"\n📄 Markdown отчет сохранен: {output_file}")
    return output_file


def test_responses_api_cache(api_key: str, model: str, base_url: str = "https://api.vsellm.ru/v1", 
                              responses_dir: str = "test_cache_responses"):
    """Test cache behavior for a specific model. Returns (success: bool, error_msg: str, json_file: str)."""
    
    client = OpenAI(
        api_key=api_key,
        base_url=base_url
    )
    
    user_id = f"test-conv-{int(time.time())}"
    
    print(f"\n{'='*60}")
    print(f"Testing model: {model}")
    print(f"User ID: {user_id}")
    print(f"{'='*60}\n")
    
    r1 = None
    r2 = None
    
    print("Turn 1: Creating initial response...")
    try:
        r1 = client.responses.create(
            model=model,
            input="Hello! Tell me a short joke.",
            store=True,
            user=user_id,
        )
        print(f"  Response ID: {r1.id}")
        print(f"  Model used: {r1.model}")
        print(f"  Output: {r1.output_text[:100]}...")
        
        if hasattr(r1, "usage") and r1.usage:
            print(f"  Usage: {r1.usage}")
    except Exception as e:
        print(f"  ERROR: {e}")
        return False, str(e), None
    
    print("\nTurn 2: Testing sticky credential with previous_response_id...")
    try:
        r2 = client.responses.create(
            model=model,
            input="Continue our conversation. What was the joke about?",
            previous_response_id=r1.id,
            store=True,
            user=user_id,
        )
        print(f"  Response ID: {r2.id}")
        print(f"  Model used: {r2.model}")
        print(f"  Output: {r2.output_text[:100]}...")
        

        if hasattr(r2, "usage") and r2.usage:
            print(f"  Usage: {r2.usage}")
        

        if "joke" in r2.output_text.lower():
            print("  \n  OK: Response references previous context (cache works!)")
        else:
            print("  \n  WARNING: Response may not reference previous context")
            
    except Exception as e:
        print(f"  ERROR: {e}")

        if r1:
            json_file = save_responses_json(model, r1, type('obj', (object,), {
                'id': 'ERROR', 'model': 'ERROR', 'output_text': str(e),
                'usage': None, 'object': 'error', 'created_at': None
            })())
            return False, str(e), json_file
        return False, str(e), None
    

    json_file = save_responses_json(model, r1, r2, responses_dir)
    
    print(f"\n{'='*60}")
    print("Test completed successfully!")
    print(f"{'='*60}\n")
    return True, None, json_file


def main():
    parser = argparse.ArgumentParser(description="Test cache behavior for LLM models")
    parser.add_argument("--api-key", required=True, help="Your VseLLM API key")
    parser.add_argument("--model", default="openai/gpt-4o", help="Model to test (default: openai/gpt-4o)")
    parser.add_argument("--base-url", default="https://api.vsellm.ru/v1", help="Base URL for API")
    parser.add_argument("--list-models", action="store_true", help="List available LLM models and exit")
    parser.add_argument("--test-all", action="store_true", help="Test all available LLM models")
    parser.add_argument("--responses-dir", default="test_cache_responses", help="Directory to save JSON responses")
    parser.add_argument("--report-file", default="test_cache_report.md", help="Markdown report filename")
    
    args = parser.parse_args()
    
    if args.list_models:
        print("Fetching LLM models from provider...\n")
        models = get_llm_models_from_provider(args.api_key, args.base_url)
        print(f"Found {len(models)} models:")
        for i, model in enumerate(models[:20], 1):  # Show first 20
            print(f"  {i}. {model}")
        if len(models) > 20:
            print(f"  ... and {len(models) - 20} more")
        return
    
    if args.test_all:
        print("Fetching LLM models from provider...\n")
        models = get_llm_models_from_provider(args.api_key, args.base_url)
        
        print(f"\nTesting {len(models)} models...")
        print(f"JSON responses will be saved to: {args.responses_dir}/\n")
        
        results = []
        for model in models:
            success, error_msg, json_file = test_responses_api_cache(
                args.api_key, model, args.base_url, args.responses_dir
            )
            results.append((model, success, error_msg, json_file))
            time.sleep(1)  # Rate limiting
        
        print(f"\n{'='*60}")
        print("SUMMARY:")
        print(f"{'='*60}")
        for model, success, _, _ in results:
            status = "OK" if success else "FAILED"
            print(f"  {model}: {status}")
        
       
        report_file = generate_markdown_report(results, args.responses_dir, args.report_file)
        print(f"\n📊 Полный отчет доступен в файле: {report_file}")
        print(f"💾 JSON ответы сохранены в: {args.responses_dir}/")
        return
    

    success, error_msg, json_file = test_responses_api_cache(
        args.api_key, args.model, args.base_url, args.responses_dir
    )
    if json_file:
        print(f"\n📄 JSON saved: {json_file}")


if __name__ == "__main__":
    main()
