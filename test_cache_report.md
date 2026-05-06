# Отчет тестирования кеширования Responses API

**Дата:** 2026-05-06 15:55:49  
**Всего моделей:** 85  
**Успешно:** 54 ✅  
**Ошибок:** 31 ❌  
**Директория с JSON:** `test_cache_responses/`

---

## Сводка

| Модель | Статус | Ошибка | JSON файл |
|--------|--------|--------|-----------|
| `xiaomi/mimo-v2.5-pro` | ✅ OK | - | [xiaomi_mimo-v2.5-pro_20260506_154046.json](test_cache_responses/xiaomi_mimo-v2.5-pro_20260506_154046.json) |
| `moonshotai/kimi-k2.6` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"45536e3b-0f8e-9b18-b6dd-9b5c3b6e12cb","code":"InvalidParameter","message":"Unsupported model: \'kimi-k2.6\'."}. Received Model Group=moonshotai/kimi-k2.6\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `qwen/qwen3.6-max-preview` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"609c32e4-e7b5-9724-afa6-9f345fe2fe38","code":"InvalidParameter","message":"Unsupported model: \'qwen3.6-max-preview\'."}. Received Model Group=qwen/qwen3.6-max-preview\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `qwen/qwen3.6-flash` | ✅ OK | - | [qwen_qwen3.6-flash_20260506_154058.json](test_cache_responses/qwen_qwen3.6-flash_20260506_154058.json) |
| `qwen/qwen3.6-35b-a3b` | ✅ OK | - | [qwen_qwen3.6-35b-a3b_20260506_154107.json](test_cache_responses/qwen_qwen3.6-35b-a3b_20260506_154107.json) |
| `qwen/qwen3-coder-next` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"64a989db-6896-9caf-b2d9-075b426d3c0f","code":"InvalidParameter","message":"Unsupported model: \'qwen3-coder-next\'."}. Received Model Group=qwen/qwen3-coder-next\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `qwen/qwen3-vl-plus` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"a837b2dc-1d7d-91ce-8ebe-d97df3e363f9","code":"InvalidParameter","message":"Unsupported model: \'qwen3-vl-plus\'."}. Received Model Group=qwen/qwen3-vl-plus\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `z-ai/glm-4.6v-flashx` | ✅ OK | - | [z-ai_glm-4.6v-flashx_20260506_154301.json](test_cache_responses/z-ai_glm-4.6v-flashx_20260506_154301.json) |
| `yandex/gpt5-pro` | ❌ FAILED | Error code: 404 - {'error': {'message': 'litellm.NotFoundError: NotFoundError: OpenAIException - 404 page not found\n. Received Model Group=yandex/gpt5-pro\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '404'}} | - |
| `z-ai/glm-4.7` | ✅ OK | - | [z-ai_glm-4.7_20260506_154308.json](test_cache_responses/z-ai_glm-4.7_20260506_154308.json) |
| `qwen/qwen3-vl-8b-instruct` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"bd5d57f0-7da7-9d4b-a637-b6b04378c379","code":"InvalidParameter","message":"Unsupported model: \'qwen3-vl-8b-instruct\'."}. Received Model Group=qwen/qwen3-vl-8b-instruct\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `openai/gpt-5.1-chat` | ✅ OK | - | [openai_gpt-5.1-chat_20260506_154318.json](test_cache_responses/openai_gpt-5.1-chat_20260506_154318.json) |
| `qwen/qwen3-vl-flash` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"14f5d6ee-699f-914e-befa-e93495fef1bc","code":"InvalidParameter","message":"Unsupported model: \'qwen3-vl-flash\'."}. Received Model Group=qwen/qwen3-vl-flash\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `openai/gpt-5.1` | ✅ OK | - | [openai_gpt-5.1_20260506_154325.json](test_cache_responses/openai_gpt-5.1_20260506_154325.json) |
| `z-ai/glm-4.5-air` | ✅ OK | - | [z-ai_glm-4.5-air_20260506_154337.json](test_cache_responses/z-ai_glm-4.5-air_20260506_154337.json) |
| `openai/gpt-4.1` | ✅ OK | - | [openai_gpt-4.1_20260506_154343.json](test_cache_responses/openai_gpt-4.1_20260506_154343.json) |
| `openai/gpt-5-mini` | ✅ OK | - | [openai_gpt-5-mini_20260506_154354.json](test_cache_responses/openai_gpt-5-mini_20260506_154354.json) |
| `deepseek/deepseek-v3.2` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"ca2d189c-b407-967b-996e-e9a07f4f07e8","code":"InvalidParameter","message":"Unsupported model: \'deepseek-v3.2\'."}. Received Model Group=deepseek/deepseek-v3.2\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `z-ai/glm-4.6v-flash` | ✅ OK | - | [z-ai_glm-4.6v-flash_20260506_154447.json](test_cache_responses/z-ai_glm-4.6v-flash_20260506_154447.json) |
| `qwen/qwen3-vl-30b-a3b-thinking` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"680dfe98-4391-9681-88d6-70bc20dfcc27","code":"InvalidParameter","message":"Unsupported model: \'qwen3-vl-30b-a3b-thinking\'."}. Received Model Group=qwen/qwen3-vl-30b-a3b-thinking\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `anthropic/claude-sonnet-4` | ✅ OK | - | [anthropic_claude-sonnet-4_20260506_154455.json](test_cache_responses/anthropic_claude-sonnet-4_20260506_154455.json) |
| `openai/gpt-5.2-chat` | ✅ OK | - | [openai_gpt-5.2-chat_20260506_154500.json](test_cache_responses/openai_gpt-5.2-chat_20260506_154500.json) |
| `openai/gpt-5-chat` | ✅ OK | - | [openai_gpt-5-chat_20260506_154505.json](test_cache_responses/openai_gpt-5-chat_20260506_154505.json) |
| `openai/gpt-4.1-mini` | ✅ OK | - | [openai_gpt-4.1-mini_20260506_154511.json](test_cache_responses/openai_gpt-4.1-mini_20260506_154511.json) |
| `openai/gpt-4.1-nano` | ✅ OK | - | [openai_gpt-4.1-nano_20260506_154514.json](test_cache_responses/openai_gpt-4.1-nano_20260506_154514.json) |
| `openai/chatgpt-4o-latest` | ✅ OK | - | [openai_chatgpt-4o-latest_20260506_154523.json](test_cache_responses/openai_chatgpt-4o-latest_20260506_154523.json) |
| `openai/gpt-oss-120b` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"error":{"code":"unrecognized_request_argument","message":"Unrecognized request argument supplied: input","details":"Unrecognized request argument supplied: input"}}. Received Model Group=openai/gpt-oss-120b\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `openai/gpt-oss-20b` | ✅ OK | - | [openai_gpt-oss-20b_20260506_154543.json](test_cache_responses/openai_gpt-oss-20b_20260506_154543.json) |
| `google/gemini-2.5-pro` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {\n  "error": {\n    "code": 400,\n    "message": "* GenerateContentRequest.contents: contents is not specified\\n",\n    "status": "INVALID_ARGUMENT"\n  }\n}\n. Received Model Group=google/gemini-2.5-pro\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `qwen/qwen3-vl-235b-a22b-instruct` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"0e8e54e5-4e71-98a2-b2ac-e8f82d059ab1","code":"InvalidParameter","message":"Unsupported model: \'qwen3-vl-235b-a22b-instruct\'."}. Received Model Group=qwen/qwen3-vl-235b-a22b-instruct\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `openai/gpt-5.4-nano` | ✅ OK | - | [openai_gpt-5.4-nano_20260506_154554.json](test_cache_responses/openai_gpt-5.4-nano_20260506_154554.json) |
| `moonshotai/kimi-k2-0905` | ✅ OK | - | [moonshotai_kimi-k2-0905_20260506_154601.json](test_cache_responses/moonshotai_kimi-k2-0905_20260506_154601.json) |
| `qwen/qwen3.5-plus` | ✅ OK | - | [qwen_qwen3.5-plus_20260506_154622.json](test_cache_responses/qwen_qwen3.5-plus_20260506_154622.json) |
| `deepseek/deepseek-r1-distill-llama-70b` | ✅ OK | - | [deepseek_deepseek-r1-distill-llama-70b_20260506_154654.json](test_cache_responses/deepseek_deepseek-r1-distill-llama-70b_20260506_154654.json) |
| `google/gemini-3-flash-preview` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {\n  "error": {\n    "code": 400,\n    "message": "* GenerateContentRequest.contents: contents is not specified\\n",\n    "status": "INVALID_ARGUMENT"\n  }\n}\n. Received Model Group=google/gemini-3-flash-preview\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `google/gemini-2.5-flash` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {\n  "error": {\n    "code": 400,\n    "message": "* GenerateContentRequest.contents: contents is not specified\\n",\n    "status": "INVALID_ARGUMENT"\n  }\n}\n. Received Model Group=google/gemini-2.5-flash\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `qwen/qwen3-vl-30b-a3b-instruct` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"0f995d31-61e0-9149-8a49-85871c4739cc","code":"InvalidParameter","message":"Unsupported model: \'qwen3-vl-30b-a3b-instruct\'."}. Received Model Group=qwen/qwen3-vl-30b-a3b-instruct\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `qwen/qwen3-vl-8b-thinking` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"972b456f-097d-9508-acd3-9949d68e070c","code":"InvalidParameter","message":"Unsupported model: \'qwen3-vl-8b-thinking\'."}. Received Model Group=qwen/qwen3-vl-8b-thinking\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `qwen/qwen3.5-flash` | ✅ OK | - | [qwen_qwen3.5-flash_20260506_154721.json](test_cache_responses/qwen_qwen3.5-flash_20260506_154721.json) |
| `qwen/qwen3.5-397b-a17b` | ✅ OK | - | [qwen_qwen3.5-397b-a17b_20260506_154744.json](test_cache_responses/qwen_qwen3.5-397b-a17b_20260506_154744.json) |
| `yandex/gpt5.1-pro` | ❌ FAILED | Error code: 404 - {'error': {'message': 'litellm.NotFoundError: NotFoundError: OpenAIException - 404 page not found\n. Received Model Group=yandex/gpt5.1-pro\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '404'}} | - |
| `yandex/gpt5-lite` | ❌ FAILED | Error code: 404 - {'error': {'message': 'litellm.NotFoundError: NotFoundError: OpenAIException - 404 page not found\n. Received Model Group=yandex/gpt5-lite\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '404'}} | - |
| `anthropic/claude-haiku-4.5` | ✅ OK | - | [anthropic_claude-haiku-4.5_20260506_154754.json](test_cache_responses/anthropic_claude-haiku-4.5_20260506_154754.json) |
| `openai/gpt-5.2` | ✅ OK | - | [openai_gpt-5.2_20260506_154758.json](test_cache_responses/openai_gpt-5.2_20260506_154758.json) |
| `z-ai/glm-4.6` | ✅ OK | - | [z-ai_glm-4.6_20260506_154955.json](test_cache_responses/z-ai_glm-4.6_20260506_154955.json) |
| `qwen/qwen3-max-thinking` | ✅ OK | - | [qwen_qwen3-max-thinking_20260506_155003.json](test_cache_responses/qwen_qwen3-max-thinking_20260506_155003.json) |
| `anthropic/claude-opus-4.5` | ✅ OK | - | [anthropic_claude-opus-4.5_20260506_155011.json](test_cache_responses/anthropic_claude-opus-4.5_20260506_155011.json) |
| `openai/gpt-5.4` | ✅ OK | - | [openai_gpt-5.4_20260506_155014.json](test_cache_responses/openai_gpt-5.4_20260506_155014.json) |
| `GigaChat/GigaChat-2-Max` | ❌ FAILED | Error code: 404 - {'error': {'message': 'litellm.NotFoundError: NotFoundError: OpenAIException - {"error_msg":"404 Not Found"}\n. Received Model Group=GigaChat/GigaChat-2-Max\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '404'}} | - |
| `google/gemini-3.1-flash-lite-preview` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {\n  "error": {\n    "code": 400,\n    "message": "* GenerateContentRequest.contents: contents is not specified\\n",\n    "status": "INVALID_ARGUMENT"\n  }\n}\n. Received Model Group=google/gemini-3.1-flash-lite-preview\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `anthropic/claude-sonnet-4.5` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"message":"messages: Input should be a valid list"}. Received Model Group=anthropic/claude-sonnet-4.5\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `anthropic/claude-opus-4.7` | ✅ OK | - | [anthropic_claude-opus-4.7_20260506_155027.json](test_cache_responses/anthropic_claude-opus-4.7_20260506_155027.json) |
| `openai/gpt-5.3-chat` | ✅ OK | - | [openai_gpt-5.3-chat_20260506_155033.json](test_cache_responses/openai_gpt-5.3-chat_20260506_155033.json) |
| `meta-llama/llama-3.3-70b-instruct` | ✅ OK | - | [meta-llama_llama-3.3-70b-instruct_20260506_155041.json](test_cache_responses/meta-llama_llama-3.3-70b-instruct_20260506_155041.json) |
| `x-ai/grok-code-fast-1` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - { "code": "400", "message": "{\\"code\\":\\"Client specified an invalid argument\\",\\"error\\":\\"Unable to store messages when zdr is enabled\\"}" }. Received Model Group=x-ai/grok-code-fast-1\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `google/gemini-3.1-pro-preview` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {\n  "error": {\n    "code": 400,\n    "message": "* GenerateContentRequest.contents: contents is not specified\\n",\n    "status": "INVALID_ARGUMENT"\n  }\n}\n. Received Model Group=google/gemini-3.1-pro-preview\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `openai/gpt-5.4-mini` | ✅ OK | - | [openai_gpt-5.4-mini_20260506_155049.json](test_cache_responses/openai_gpt-5.4-mini_20260506_155049.json) |
| `qwen/qwen3-235b-a22b` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"1b1e7503-664c-9d4a-9e30-9464fac52f17","code":"InvalidParameter","message":"Unsupported model: \'qwen3-235b-a22b\'."}. Received Model Group=qwen/qwen3-235b-a22b\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `t-tech/T-pro-it-2.0` | ❌ FAILED | Error code: 404 - {'error': {'message': 'litellm.NotFoundError: NotFoundError: OpenAIException - {"error_msg":"404 Not Found"}\n. Received Model Group=t-tech/T-pro-it-2.0\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '404'}} | - |
| `google/gemini-3.1-pro-preview-customtools` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {\n  "error": {\n    "code": 400,\n    "message": "* GenerateContentRequest.contents: contents is not specified\\n",\n    "status": "INVALID_ARGUMENT"\n  }\n}\n. Received Model Group=google/gemini-3.1-pro-preview-customtools\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `xiaomi/mimo-v2-omni` | ✅ OK | - | [xiaomi_mimo-v2-omni_20260506_155108.json](test_cache_responses/xiaomi_mimo-v2-omni_20260506_155108.json) |
| `qwen/qwen3-vl-235b-a22b-thinking` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"7dab8d28-ccd0-9aa2-8fec-32dbdd25f2a9","code":"InvalidParameter","message":"Unsupported model: \'qwen3-vl-235b-a22b-thinking\'."}. Received Model Group=qwen/qwen3-vl-235b-a22b-thinking\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `z-ai/glm-5.1` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"94851611-2514-9cd3-a8bc-8601c0475772","code":"InvalidParameter","message":"Unsupported model: \'glm-5.1\'."}. Received Model Group=z-ai/glm-5.1\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `anthropic/claude-sonnet-4.6` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"message":"messages: Input should be a valid list"}. Received Model Group=anthropic/claude-sonnet-4.6\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `anthropic/claude-opus-4.6` | ✅ OK | - | [anthropic_claude-opus-4.6_20260506_155123.json](test_cache_responses/anthropic_claude-opus-4.6_20260506_155123.json) |
| `xiaomi/mimo-v2.5` | ✅ OK | - | [xiaomi_mimo-v2.5_20260506_155133.json](test_cache_responses/xiaomi_mimo-v2.5_20260506_155133.json) |
| `xiaomi/mimo-v2-flash` | ✅ OK | - | [xiaomi_mimo-v2-flash_20260506_155138.json](test_cache_responses/xiaomi_mimo-v2-flash_20260506_155138.json) |
| `deepseek/deepseek-v3.2-speciale` | ✅ OK | - | [deepseek_deepseek-v3.2-speciale_20260506_155159.json](test_cache_responses/deepseek_deepseek-v3.2-speciale_20260506_155159.json) |
| `deepseek/deepseek-v4-pro` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"1290ba77-daa4-944e-b11d-8e86d4fca693","code":"InvalidParameter","message":"Unsupported model: \'deepseek-v4-pro\'."}. Received Model Group=deepseek/deepseek-v4-pro\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `anthropic/claude-opus-4.1` | ✅ OK | - | [anthropic_claude-opus-4.1_20260506_155218.json](test_cache_responses/anthropic_claude-opus-4.1_20260506_155218.json) |
| `qwen/qwen3.6-plus` | ✅ OK | - | [qwen_qwen3.6-plus_20260506_155238.json](test_cache_responses/qwen_qwen3.6-plus_20260506_155238.json) |
| `openai/gpt-5.4-pro` | ✅ OK | - | [openai_gpt-5.4-pro_20260506_155338.json](test_cache_responses/openai_gpt-5.4-pro_20260506_155338.json) |
| `openai/gpt-4o-mini` | ✅ OK | - | [openai_gpt-4o-mini_20260506_155343.json](test_cache_responses/openai_gpt-4o-mini_20260506_155343.json) |
| `deepseek/deepseek-v4-flash` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"3732ddb5-12fb-9bf9-99dd-6044caa4e315","code":"InvalidParameter","message":"Unsupported model: \'deepseek-v4-flash\'."}. Received Model Group=deepseek/deepseek-v4-flash\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `openai/gpt-5.3-codex` | ✅ OK | - | [openai_gpt-5.3-codex_20260506_155349.json](test_cache_responses/openai_gpt-5.3-codex_20260506_155349.json) |
| `openai/gpt-5.2-codex` | ✅ OK | - | [openai_gpt-5.2-codex_20260506_155354.json](test_cache_responses/openai_gpt-5.2-codex_20260506_155354.json) |
| `openai/gpt-5` | ✅ OK | - | [openai_gpt-5_20260506_155402.json](test_cache_responses/openai_gpt-5_20260506_155402.json) |
| `openai/gpt-5-nano` | ✅ OK | - | [openai_gpt-5-nano_20260506_155411.json](test_cache_responses/openai_gpt-5-nano_20260506_155411.json) |
| `moonshotai/kimi-k2.5` | ✅ OK | - | [moonshotai_kimi-k2.5_20260506_155414.json](test_cache_responses/moonshotai_kimi-k2.5_20260506_155414.json) |
| `xiaomi/mimo-v2-pro` | ✅ OK | - | [xiaomi_mimo-v2-pro_20260506_155425.json](test_cache_responses/xiaomi_mimo-v2-pro_20260506_155425.json) |
| `z-ai/glm-5` | ✅ OK | - | [z-ai_glm-5_20260506_155430.json](test_cache_responses/z-ai_glm-5_20260506_155430.json) |
| `z-ai/glm-4.7-flash` | ✅ OK | - | [z-ai_glm-4.7-flash_20260506_155439.json](test_cache_responses/z-ai_glm-4.7-flash_20260506_155439.json) |
| `z-ai/glm-4.6v` | ✅ OK | - | [z-ai_glm-4.6v_20260506_155531.json](test_cache_responses/z-ai_glm-4.6v_20260506_155531.json) |
| `openai/gpt-5.5` | ✅ OK | - | [openai_gpt-5.5_20260506_155536.json](test_cache_responses/openai_gpt-5.5_20260506_155536.json) |
| `deepseek/deepseek-chat-v3-0324` | ✅ OK | - | [deepseek_deepseek-chat-v3-0324_20260506_155548.json](test_cache_responses/deepseek_deepseek-chat-v3-0324_20260506_155548.json) |


---

## Подробные результаты

### xiaomi/mimo-v2.5-pro

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/xiaomi_mimo-v2.5-pro_20260506_154046.json`

### moonshotai/kimi-k2.6

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"45536e3b-0f8e-9b18-b6dd-9b5c3b6e12cb","code":"InvalidParameter","message":"Unsupported model: \'kimi-k2.6\'."}. Received Model Group=moonshotai/kimi-k2.6\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### qwen/qwen3.6-max-preview

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"609c32e4-e7b5-9724-afa6-9f345fe2fe38","code":"InvalidParameter","message":"Unsupported model: \'qwen3.6-max-preview\'."}. Received Model Group=qwen/qwen3.6-max-preview\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### qwen/qwen3.6-flash

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/qwen_qwen3.6-flash_20260506_154058.json`

### qwen/qwen3.6-35b-a3b

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/qwen_qwen3.6-35b-a3b_20260506_154107.json`

### qwen/qwen3-coder-next

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"64a989db-6896-9caf-b2d9-075b426d3c0f","code":"InvalidParameter","message":"Unsupported model: \'qwen3-coder-next\'."}. Received Model Group=qwen/qwen3-coder-next\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### qwen/qwen3-vl-plus

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"a837b2dc-1d7d-91ce-8ebe-d97df3e363f9","code":"InvalidParameter","message":"Unsupported model: \'qwen3-vl-plus\'."}. Received Model Group=qwen/qwen3-vl-plus\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### z-ai/glm-4.6v-flashx

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/z-ai_glm-4.6v-flashx_20260506_154301.json`

### yandex/gpt5-pro

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 404 - {'error': {'message': 'litellm.NotFoundError: NotFoundError: OpenAIException - 404 page not found\n. Received Model Group=yandex/gpt5-pro\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '404'}}`

### z-ai/glm-4.7

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/z-ai_glm-4.7_20260506_154308.json`

### qwen/qwen3-vl-8b-instruct

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"bd5d57f0-7da7-9d4b-a637-b6b04378c379","code":"InvalidParameter","message":"Unsupported model: \'qwen3-vl-8b-instruct\'."}. Received Model Group=qwen/qwen3-vl-8b-instruct\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### openai/gpt-5.1-chat

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-5.1-chat_20260506_154318.json`

### qwen/qwen3-vl-flash

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"14f5d6ee-699f-914e-befa-e93495fef1bc","code":"InvalidParameter","message":"Unsupported model: \'qwen3-vl-flash\'."}. Received Model Group=qwen/qwen3-vl-flash\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### openai/gpt-5.1

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-5.1_20260506_154325.json`

### z-ai/glm-4.5-air

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/z-ai_glm-4.5-air_20260506_154337.json`

### openai/gpt-4.1

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-4.1_20260506_154343.json`

### openai/gpt-5-mini

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-5-mini_20260506_154354.json`

### deepseek/deepseek-v3.2

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"ca2d189c-b407-967b-996e-e9a07f4f07e8","code":"InvalidParameter","message":"Unsupported model: \'deepseek-v3.2\'."}. Received Model Group=deepseek/deepseek-v3.2\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### z-ai/glm-4.6v-flash

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/z-ai_glm-4.6v-flash_20260506_154447.json`

### qwen/qwen3-vl-30b-a3b-thinking

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"680dfe98-4391-9681-88d6-70bc20dfcc27","code":"InvalidParameter","message":"Unsupported model: \'qwen3-vl-30b-a3b-thinking\'."}. Received Model Group=qwen/qwen3-vl-30b-a3b-thinking\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### anthropic/claude-sonnet-4

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/anthropic_claude-sonnet-4_20260506_154455.json`

### openai/gpt-5.2-chat

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-5.2-chat_20260506_154500.json`

### openai/gpt-5-chat

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-5-chat_20260506_154505.json`

### openai/gpt-4.1-mini

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-4.1-mini_20260506_154511.json`

### openai/gpt-4.1-nano

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-4.1-nano_20260506_154514.json`

### openai/chatgpt-4o-latest

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/openai_chatgpt-4o-latest_20260506_154523.json`

### openai/gpt-oss-120b

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"error":{"code":"unrecognized_request_argument","message":"Unrecognized request argument supplied: input","details":"Unrecognized request argument supplied: input"}}. Received Model Group=openai/gpt-oss-120b\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### openai/gpt-oss-20b

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-oss-20b_20260506_154543.json`

### google/gemini-2.5-pro

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {\n  "error": {\n    "code": 400,\n    "message": "* GenerateContentRequest.contents: contents is not specified\\n",\n    "status": "INVALID_ARGUMENT"\n  }\n}\n. Received Model Group=google/gemini-2.5-pro\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### qwen/qwen3-vl-235b-a22b-instruct

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"0e8e54e5-4e71-98a2-b2ac-e8f82d059ab1","code":"InvalidParameter","message":"Unsupported model: \'qwen3-vl-235b-a22b-instruct\'."}. Received Model Group=qwen/qwen3-vl-235b-a22b-instruct\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### openai/gpt-5.4-nano

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-5.4-nano_20260506_154554.json`

### moonshotai/kimi-k2-0905

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/moonshotai_kimi-k2-0905_20260506_154601.json`

### qwen/qwen3.5-plus

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/qwen_qwen3.5-plus_20260506_154622.json`

### deepseek/deepseek-r1-distill-llama-70b

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/deepseek_deepseek-r1-distill-llama-70b_20260506_154654.json`

### google/gemini-3-flash-preview

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {\n  "error": {\n    "code": 400,\n    "message": "* GenerateContentRequest.contents: contents is not specified\\n",\n    "status": "INVALID_ARGUMENT"\n  }\n}\n. Received Model Group=google/gemini-3-flash-preview\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### google/gemini-2.5-flash

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {\n  "error": {\n    "code": 400,\n    "message": "* GenerateContentRequest.contents: contents is not specified\\n",\n    "status": "INVALID_ARGUMENT"\n  }\n}\n. Received Model Group=google/gemini-2.5-flash\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### qwen/qwen3-vl-30b-a3b-instruct

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"0f995d31-61e0-9149-8a49-85871c4739cc","code":"InvalidParameter","message":"Unsupported model: \'qwen3-vl-30b-a3b-instruct\'."}. Received Model Group=qwen/qwen3-vl-30b-a3b-instruct\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### qwen/qwen3-vl-8b-thinking

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"972b456f-097d-9508-acd3-9949d68e070c","code":"InvalidParameter","message":"Unsupported model: \'qwen3-vl-8b-thinking\'."}. Received Model Group=qwen/qwen3-vl-8b-thinking\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### qwen/qwen3.5-flash

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/qwen_qwen3.5-flash_20260506_154721.json`

### qwen/qwen3.5-397b-a17b

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/qwen_qwen3.5-397b-a17b_20260506_154744.json`

### yandex/gpt5.1-pro

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 404 - {'error': {'message': 'litellm.NotFoundError: NotFoundError: OpenAIException - 404 page not found\n. Received Model Group=yandex/gpt5.1-pro\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '404'}}`

### yandex/gpt5-lite

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 404 - {'error': {'message': 'litellm.NotFoundError: NotFoundError: OpenAIException - 404 page not found\n. Received Model Group=yandex/gpt5-lite\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '404'}}`

### anthropic/claude-haiku-4.5

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/anthropic_claude-haiku-4.5_20260506_154754.json`

### openai/gpt-5.2

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-5.2_20260506_154758.json`

### z-ai/glm-4.6

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/z-ai_glm-4.6_20260506_154955.json`

### qwen/qwen3-max-thinking

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/qwen_qwen3-max-thinking_20260506_155003.json`

### anthropic/claude-opus-4.5

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/anthropic_claude-opus-4.5_20260506_155011.json`

### openai/gpt-5.4

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-5.4_20260506_155014.json`

### GigaChat/GigaChat-2-Max

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 404 - {'error': {'message': 'litellm.NotFoundError: NotFoundError: OpenAIException - {"error_msg":"404 Not Found"}\n. Received Model Group=GigaChat/GigaChat-2-Max\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '404'}}`

### google/gemini-3.1-flash-lite-preview

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {\n  "error": {\n    "code": 400,\n    "message": "* GenerateContentRequest.contents: contents is not specified\\n",\n    "status": "INVALID_ARGUMENT"\n  }\n}\n. Received Model Group=google/gemini-3.1-flash-lite-preview\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### anthropic/claude-sonnet-4.5

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"message":"messages: Input should be a valid list"}. Received Model Group=anthropic/claude-sonnet-4.5\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### anthropic/claude-opus-4.7

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/anthropic_claude-opus-4.7_20260506_155027.json`

### openai/gpt-5.3-chat

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-5.3-chat_20260506_155033.json`

### meta-llama/llama-3.3-70b-instruct

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/meta-llama_llama-3.3-70b-instruct_20260506_155041.json`

### x-ai/grok-code-fast-1

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - { "code": "400", "message": "{\\"code\\":\\"Client specified an invalid argument\\",\\"error\\":\\"Unable to store messages when zdr is enabled\\"}" }. Received Model Group=x-ai/grok-code-fast-1\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### google/gemini-3.1-pro-preview

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {\n  "error": {\n    "code": 400,\n    "message": "* GenerateContentRequest.contents: contents is not specified\\n",\n    "status": "INVALID_ARGUMENT"\n  }\n}\n. Received Model Group=google/gemini-3.1-pro-preview\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### openai/gpt-5.4-mini

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-5.4-mini_20260506_155049.json`

### qwen/qwen3-235b-a22b

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"1b1e7503-664c-9d4a-9e30-9464fac52f17","code":"InvalidParameter","message":"Unsupported model: \'qwen3-235b-a22b\'."}. Received Model Group=qwen/qwen3-235b-a22b\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### t-tech/T-pro-it-2.0

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 404 - {'error': {'message': 'litellm.NotFoundError: NotFoundError: OpenAIException - {"error_msg":"404 Not Found"}\n. Received Model Group=t-tech/T-pro-it-2.0\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '404'}}`

### google/gemini-3.1-pro-preview-customtools

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {\n  "error": {\n    "code": 400,\n    "message": "* GenerateContentRequest.contents: contents is not specified\\n",\n    "status": "INVALID_ARGUMENT"\n  }\n}\n. Received Model Group=google/gemini-3.1-pro-preview-customtools\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### xiaomi/mimo-v2-omni

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/xiaomi_mimo-v2-omni_20260506_155108.json`

### qwen/qwen3-vl-235b-a22b-thinking

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"7dab8d28-ccd0-9aa2-8fec-32dbdd25f2a9","code":"InvalidParameter","message":"Unsupported model: \'qwen3-vl-235b-a22b-thinking\'."}. Received Model Group=qwen/qwen3-vl-235b-a22b-thinking\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### z-ai/glm-5.1

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"94851611-2514-9cd3-a8bc-8601c0475772","code":"InvalidParameter","message":"Unsupported model: \'glm-5.1\'."}. Received Model Group=z-ai/glm-5.1\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### anthropic/claude-sonnet-4.6

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"message":"messages: Input should be a valid list"}. Received Model Group=anthropic/claude-sonnet-4.6\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### anthropic/claude-opus-4.6

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/anthropic_claude-opus-4.6_20260506_155123.json`

### xiaomi/mimo-v2.5

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/xiaomi_mimo-v2.5_20260506_155133.json`

### xiaomi/mimo-v2-flash

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/xiaomi_mimo-v2-flash_20260506_155138.json`

### deepseek/deepseek-v3.2-speciale

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/deepseek_deepseek-v3.2-speciale_20260506_155159.json`

### deepseek/deepseek-v4-pro

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"1290ba77-daa4-944e-b11d-8e86d4fca693","code":"InvalidParameter","message":"Unsupported model: \'deepseek-v4-pro\'."}. Received Model Group=deepseek/deepseek-v4-pro\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### anthropic/claude-opus-4.1

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/anthropic_claude-opus-4.1_20260506_155218.json`

### qwen/qwen3.6-plus

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/qwen_qwen3.6-plus_20260506_155238.json`

### openai/gpt-5.4-pro

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-5.4-pro_20260506_155338.json`

### openai/gpt-4o-mini

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-4o-mini_20260506_155343.json`

### deepseek/deepseek-v4-flash

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"3732ddb5-12fb-9bf9-99dd-6044caa4e315","code":"InvalidParameter","message":"Unsupported model: \'deepseek-v4-flash\'."}. Received Model Group=deepseek/deepseek-v4-flash\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### openai/gpt-5.3-codex

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-5.3-codex_20260506_155349.json`

### openai/gpt-5.2-codex

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-5.2-codex_20260506_155354.json`

### openai/gpt-5

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-5_20260506_155402.json`

### openai/gpt-5-nano

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-5-nano_20260506_155411.json`

### moonshotai/kimi-k2.5

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/moonshotai_kimi-k2.5_20260506_155414.json`

### xiaomi/mimo-v2-pro

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/xiaomi_mimo-v2-pro_20260506_155425.json`

### z-ai/glm-5

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/z-ai_glm-5_20260506_155430.json`

### z-ai/glm-4.7-flash

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/z-ai_glm-4.7-flash_20260506_155439.json`

### z-ai/glm-4.6v

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/z-ai_glm-4.6v_20260506_155531.json`

### openai/gpt-5.5

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-5.5_20260506_155536.json`

### deepseek/deepseek-chat-v3-0324

- **Статус:** ✅ Успешно
- **JSON файл:** `test_cache_responses/deepseek_deepseek-chat-v3-0324_20260506_155548.json`


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
