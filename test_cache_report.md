# Отчет тестирования кеширования Responses API

**Дата:** 2026-05-06 16:18:28  
**Всего моделей:** 85  
**Успешно:** 55  
**Ошибок:** 30 ❌  
**Директория с JSON:** `test_cache_responses/`

---

## Сводка

| Модель | Статус | Ошибка | JSON файл |
|--------|--------|--------|-----------|
| `xiaomi/mimo-v2.5-pro` |  OK | - | [xiaomi_mimo-v2.5-pro_20260506_160506.json](test_cache_responses/xiaomi_mimo-v2.5-pro_20260506_160506.json) |
| `moonshotai/kimi-k2.6` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"232c3b51-8b5b-9a21-9b6c-25560c706ca6","code":"InvalidParameter","message":"Unsupported model: \'kimi-k2.6\'."}. Received Model Group=moonshotai/kimi-k2.6\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `qwen/qwen3.6-max-preview` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"3130d080-7817-9916-bb3b-960a87156959","code":"InvalidParameter","message":"Unsupported model: \'qwen3.6-max-preview\'."}. Received Model Group=qwen/qwen3.6-max-preview\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `qwen/qwen3.6-flash` |  OK | - | [qwen_qwen3.6-flash_20260506_160523.json](test_cache_responses/qwen_qwen3.6-flash_20260506_160523.json) |
| `qwen/qwen3.6-35b-a3b` |  OK | - | [qwen_qwen3.6-35b-a3b_20260506_160532.json](test_cache_responses/qwen_qwen3.6-35b-a3b_20260506_160532.json) |
| `qwen/qwen3-coder-next` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"4c80c883-3dc9-9fee-afd7-c56d8f23d71f","code":"InvalidParameter","message":"Unsupported model: \'qwen3-coder-next\'."}. Received Model Group=qwen/qwen3-coder-next\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `qwen/qwen3-vl-plus` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"9123d917-8a82-9c6d-bdd5-a878ac0f4861","code":"InvalidParameter","message":"Unsupported model: \'qwen3-vl-plus\'."}. Received Model Group=qwen/qwen3-vl-plus\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `z-ai/glm-4.6v-flashx` |  OK | - | [z-ai_glm-4.6v-flashx_20260506_160551.json](test_cache_responses/z-ai_glm-4.6v-flashx_20260506_160551.json) |
| `yandex/gpt5-pro` | ❌ FAILED | Error code: 404 - {'error': {'message': 'litellm.NotFoundError: NotFoundError: OpenAIException - 404 page not found\n. Received Model Group=yandex/gpt5-pro\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '404'}} | - |
| `z-ai/glm-4.7` |  OK | - | [z-ai_glm-4.7_20260506_160557.json](test_cache_responses/z-ai_glm-4.7_20260506_160557.json) |
| `qwen/qwen3-vl-8b-instruct` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"dc92d6fd-fcbf-92d8-9caa-16d17275729e","code":"InvalidParameter","message":"Unsupported model: \'qwen3-vl-8b-instruct\'."}. Received Model Group=qwen/qwen3-vl-8b-instruct\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `openai/gpt-5.1-chat` |  OK | - | [openai_gpt-5.1-chat_20260506_160605.json](test_cache_responses/openai_gpt-5.1-chat_20260506_160605.json) |
| `qwen/qwen3-vl-flash` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"f4c84d28-c11b-900b-8e79-0353cd0623af","code":"InvalidParameter","message":"Unsupported model: \'qwen3-vl-flash\'."}. Received Model Group=qwen/qwen3-vl-flash\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `openai/gpt-5.1` |  OK | - | [openai_gpt-5.1_20260506_160614.json](test_cache_responses/openai_gpt-5.1_20260506_160614.json) |
| `z-ai/glm-4.5-air` |  OK | - | [z-ai_glm-4.5-air_20260506_160625.json](test_cache_responses/z-ai_glm-4.5-air_20260506_160625.json) |
| `openai/gpt-4.1` |  OK | - | [openai_gpt-4.1_20260506_160629.json](test_cache_responses/openai_gpt-4.1_20260506_160629.json) |
| `openai/gpt-5-mini` |  OK | - | [openai_gpt-5-mini_20260506_160641.json](test_cache_responses/openai_gpt-5-mini_20260506_160641.json) |
| `deepseek/deepseek-v3.2` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"48fdcb92-dfd9-95d9-9afd-6a0a77cad6b8","code":"InvalidParameter","message":"Unsupported model: \'deepseek-v3.2\'."}. Received Model Group=deepseek/deepseek-v3.2\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `z-ai/glm-4.6v-flash` |  OK | - | [z-ai_glm-4.6v-flash_20260506_160711.json](test_cache_responses/z-ai_glm-4.6v-flash_20260506_160711.json) |
| `qwen/qwen3-vl-30b-a3b-thinking` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"9fc1f8d4-63e8-9a9d-8ccb-4502a894696e","code":"InvalidParameter","message":"Unsupported model: \'qwen3-vl-30b-a3b-thinking\'."}. Received Model Group=qwen/qwen3-vl-30b-a3b-thinking\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `anthropic/claude-sonnet-4` |  OK | - | [anthropic_claude-sonnet-4_20260506_160721.json](test_cache_responses/anthropic_claude-sonnet-4_20260506_160721.json) |
| `openai/gpt-5.2-chat` |  OK | - | [openai_gpt-5.2-chat_20260506_160727.json](test_cache_responses/openai_gpt-5.2-chat_20260506_160727.json) |
| `openai/gpt-5-chat` |  OK | - | [openai_gpt-5-chat_20260506_160732.json](test_cache_responses/openai_gpt-5-chat_20260506_160732.json) |
| `openai/gpt-4.1-mini` |  OK | - | [openai_gpt-4.1-mini_20260506_160737.json](test_cache_responses/openai_gpt-4.1-mini_20260506_160737.json) |
| `openai/gpt-4.1-nano` |  OK | - | [openai_gpt-4.1-nano_20260506_160743.json](test_cache_responses/openai_gpt-4.1-nano_20260506_160743.json) |
| `openai/chatgpt-4o-latest` |  OK | - | [openai_chatgpt-4o-latest_20260506_160758.json](test_cache_responses/openai_chatgpt-4o-latest_20260506_160758.json) |
| `openai/gpt-oss-120b` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"error":{"code":"unrecognized_request_argument","message":"Unrecognized request argument supplied: input","details":"Unrecognized request argument supplied: input"}}. Received Model Group=openai/gpt-oss-120b\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `openai/gpt-oss-20b` |  OK | - | [openai_gpt-oss-20b_20260506_160802.json](test_cache_responses/openai_gpt-oss-20b_20260506_160802.json) |
| `google/gemini-2.5-pro` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {\n  "error": {\n    "code": 400,\n    "message": "* GenerateContentRequest.contents: contents is not specified\\n",\n    "status": "INVALID_ARGUMENT"\n  }\n}\n. Received Model Group=google/gemini-2.5-pro\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `qwen/qwen3-vl-235b-a22b-instruct` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"e5a80897-302b-97d2-95c0-19f66d523f4a","code":"InvalidParameter","message":"Unsupported model: \'qwen3-vl-235b-a22b-instruct\'."}. Received Model Group=qwen/qwen3-vl-235b-a22b-instruct\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `openai/gpt-5.4-nano` |  OK | - | [openai_gpt-5.4-nano_20260506_160815.json](test_cache_responses/openai_gpt-5.4-nano_20260506_160815.json) |
| `moonshotai/kimi-k2-0905` |  OK | - | [moonshotai_kimi-k2-0905_20260506_160819.json](test_cache_responses/moonshotai_kimi-k2-0905_20260506_160819.json) |
| `qwen/qwen3.5-plus` |  OK | - | [qwen_qwen3.5-plus_20260506_160843.json](test_cache_responses/qwen_qwen3.5-plus_20260506_160843.json) |
| `deepseek/deepseek-r1-distill-llama-70b` |  OK | - | [deepseek_deepseek-r1-distill-llama-70b_20260506_160857.json](test_cache_responses/deepseek_deepseek-r1-distill-llama-70b_20260506_160857.json) |
| `google/gemini-3-flash-preview` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {\n  "error": {\n    "code": 400,\n    "message": "* GenerateContentRequest.contents: contents is not specified\\n",\n    "status": "INVALID_ARGUMENT"\n  }\n}\n. Received Model Group=google/gemini-3-flash-preview\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `google/gemini-2.5-flash` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {\n  "error": {\n    "code": 400,\n    "message": "* GenerateContentRequest.contents: contents is not specified\\n",\n    "status": "INVALID_ARGUMENT"\n  }\n}\n. Received Model Group=google/gemini-2.5-flash\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `qwen/qwen3-vl-30b-a3b-instruct` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"f2ab1def-af31-9369-99ba-dc02745b0e37","code":"InvalidParameter","message":"Unsupported model: \'qwen3-vl-30b-a3b-instruct\'."}. Received Model Group=qwen/qwen3-vl-30b-a3b-instruct\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `qwen/qwen3-vl-8b-thinking` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"b8268c71-b067-9ad9-ba2a-d34b607b4f2e","code":"InvalidParameter","message":"Unsupported model: \'qwen3-vl-8b-thinking\'."}. Received Model Group=qwen/qwen3-vl-8b-thinking\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `qwen/qwen3.5-flash` |  OK | - | [qwen_qwen3.5-flash_20260506_160945.json](test_cache_responses/qwen_qwen3.5-flash_20260506_160945.json) |
| `qwen/qwen3.5-397b-a17b` |  OK | - | [qwen_qwen3.5-397b-a17b_20260506_161008.json](test_cache_responses/qwen_qwen3.5-397b-a17b_20260506_161008.json) |
| `yandex/gpt5.1-pro` | ❌ FAILED | Error code: 404 - {'error': {'message': 'litellm.NotFoundError: NotFoundError: OpenAIException - 404 page not found\n. Received Model Group=yandex/gpt5.1-pro\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '404'}} | - |
| `yandex/gpt5-lite` | ❌ FAILED | Error code: 404 - {'error': {'message': 'litellm.NotFoundError: NotFoundError: OpenAIException - 404 page not found\n. Received Model Group=yandex/gpt5-lite\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '404'}} | - |
| `anthropic/claude-haiku-4.5` |  OK | - | [anthropic_claude-haiku-4.5_20260506_161019.json](test_cache_responses/anthropic_claude-haiku-4.5_20260506_161019.json) |
| `openai/gpt-5.2` |  OK | - | [openai_gpt-5.2_20260506_161022.json](test_cache_responses/openai_gpt-5.2_20260506_161022.json) |
| `z-ai/glm-4.6` |  OK | - | [z-ai_glm-4.6_20260506_161122.json](test_cache_responses/z-ai_glm-4.6_20260506_161122.json) |
| `qwen/qwen3-max-thinking` |  OK | - | [qwen_qwen3-max-thinking_20260506_161128.json](test_cache_responses/qwen_qwen3-max-thinking_20260506_161128.json) |
| `anthropic/claude-opus-4.5` |  OK | - | [anthropic_claude-opus-4.5_20260506_161135.json](test_cache_responses/anthropic_claude-opus-4.5_20260506_161135.json) |
| `openai/gpt-5.4` |  OK | - | [openai_gpt-5.4_20260506_161222.json](test_cache_responses/openai_gpt-5.4_20260506_161222.json) |
| `GigaChat/GigaChat-2-Max` | ❌ FAILED | Error code: 404 - {'error': {'message': 'litellm.NotFoundError: NotFoundError: OpenAIException - {"error_msg":"404 Not Found"}\n. Received Model Group=GigaChat/GigaChat-2-Max\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '404'}} | - |
| `google/gemini-3.1-flash-lite-preview` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {\n  "error": {\n    "code": 400,\n    "message": "* GenerateContentRequest.contents: contents is not specified\\n",\n    "status": "INVALID_ARGUMENT"\n  }\n}\n. Received Model Group=google/gemini-3.1-flash-lite-preview\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `anthropic/claude-sonnet-4.5` |  OK | - | [anthropic_claude-sonnet-4.5_20260506_161241.json](test_cache_responses/anthropic_claude-sonnet-4.5_20260506_161241.json) |
| `anthropic/claude-opus-4.7` |  OK | - | [anthropic_claude-opus-4.7_20260506_161248.json](test_cache_responses/anthropic_claude-opus-4.7_20260506_161248.json) |
| `openai/gpt-5.3-chat` |  OK | - | [openai_gpt-5.3-chat_20260506_161253.json](test_cache_responses/openai_gpt-5.3-chat_20260506_161253.json) |
| `meta-llama/llama-3.3-70b-instruct` |  OK | - | [meta-llama_llama-3.3-70b-instruct_20260506_161301.json](test_cache_responses/meta-llama_llama-3.3-70b-instruct_20260506_161301.json) |
| `x-ai/grok-code-fast-1` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - { "code": "400", "message": "{\\"code\\":\\"Client specified an invalid argument\\",\\"error\\":\\"Unable to store messages when zdr is enabled\\"}" }. Received Model Group=x-ai/grok-code-fast-1\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `google/gemini-3.1-pro-preview` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {\n  "error": {\n    "code": 400,\n    "message": "* GenerateContentRequest.contents: contents is not specified\\n",\n    "status": "INVALID_ARGUMENT"\n  }\n}\n. Received Model Group=google/gemini-3.1-pro-preview\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `openai/gpt-5.4-mini` |  OK | - | [openai_gpt-5.4-mini_20260506_161311.json](test_cache_responses/openai_gpt-5.4-mini_20260506_161311.json) |
| `qwen/qwen3-235b-a22b` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"bab3737a-0868-9265-a32a-56b6abb1d835","code":"InvalidParameter","message":"Unsupported model: \'qwen3-235b-a22b\'."}. Received Model Group=qwen/qwen3-235b-a22b\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `t-tech/T-pro-it-2.0` | ❌ FAILED | Error code: 404 - {'error': {'message': 'litellm.NotFoundError: NotFoundError: OpenAIException - {"error_msg":"404 Not Found"}\n. Received Model Group=t-tech/T-pro-it-2.0\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '404'}} | - |
| `google/gemini-3.1-pro-preview-customtools` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {\n  "error": {\n    "code": 400,\n    "message": "* GenerateContentRequest.contents: contents is not specified\\n",\n    "status": "INVALID_ARGUMENT"\n  }\n}\n. Received Model Group=google/gemini-3.1-pro-preview-customtools\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `xiaomi/mimo-v2-omni` |  OK | - | [xiaomi_mimo-v2-omni_20260506_161325.json](test_cache_responses/xiaomi_mimo-v2-omni_20260506_161325.json) |
| `qwen/qwen3-vl-235b-a22b-thinking` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"e12ffba5-4e88-938c-b0c3-3cf6e68352cd","code":"InvalidParameter","message":"Unsupported model: \'qwen3-vl-235b-a22b-thinking\'."}. Received Model Group=qwen/qwen3-vl-235b-a22b-thinking\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `z-ai/glm-5.1` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"327009f1-31aa-9aed-b0f0-d30e69f096b8","code":"InvalidParameter","message":"Unsupported model: \'glm-5.1\'."}. Received Model Group=z-ai/glm-5.1\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `anthropic/claude-sonnet-4.6` |  OK | - | [anthropic_claude-sonnet-4.6_20260506_161335.json](test_cache_responses/anthropic_claude-sonnet-4.6_20260506_161335.json) |
| `anthropic/claude-opus-4.6` |  OK | - | [anthropic_claude-opus-4.6_20260506_161342.json](test_cache_responses/anthropic_claude-opus-4.6_20260506_161342.json) |
| `xiaomi/mimo-v2.5` |  OK | - | [xiaomi_mimo-v2.5_20260506_161351.json](test_cache_responses/xiaomi_mimo-v2.5_20260506_161351.json) |
| `xiaomi/mimo-v2-flash` |  OK | - | [xiaomi_mimo-v2-flash_20260506_161356.json](test_cache_responses/xiaomi_mimo-v2-flash_20260506_161356.json) |
| `deepseek/deepseek-v3.2-speciale` |  OK | - | [deepseek_deepseek-v3.2-speciale_20260506_161434.json](test_cache_responses/deepseek_deepseek-v3.2-speciale_20260506_161434.json) |
| `deepseek/deepseek-v4-pro` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"3f4f01e5-f1f0-9056-8264-992bc32ad242","code":"InvalidParameter","message":"Unsupported model: \'deepseek-v4-pro\'."}. Received Model Group=deepseek/deepseek-v4-pro\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `anthropic/claude-opus-4.1` |  OK | - | [anthropic_claude-opus-4.1_20260506_161451.json](test_cache_responses/anthropic_claude-opus-4.1_20260506_161451.json) |
| `qwen/qwen3.6-plus` |  OK | - | [qwen_qwen3.6-plus_20260506_161525.json](test_cache_responses/qwen_qwen3.6-plus_20260506_161525.json) |
| `openai/gpt-5.4-pro` |  OK | - | [openai_gpt-5.4-pro_20260506_161608.json](test_cache_responses/openai_gpt-5.4-pro_20260506_161608.json) |
| `openai/gpt-4o-mini` |  OK | - | [openai_gpt-4o-mini_20260506_161614.json](test_cache_responses/openai_gpt-4o-mini_20260506_161614.json) |
| `deepseek/deepseek-v4-flash` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"5d2af640-995b-9652-a1a1-e2cfea2e196f","code":"InvalidParameter","message":"Unsupported model: \'deepseek-v4-flash\'."}. Received Model Group=deepseek/deepseek-v4-flash\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `openai/gpt-5.3-codex` |  OK | - | [openai_gpt-5.3-codex_20260506_161620.json](test_cache_responses/openai_gpt-5.3-codex_20260506_161620.json) |
| `openai/gpt-5.2-codex` |  OK | - | [openai_gpt-5.2-codex_20260506_161625.json](test_cache_responses/openai_gpt-5.2-codex_20260506_161625.json) |
| `openai/gpt-5` |  OK | - | [openai_gpt-5_20260506_161633.json](test_cache_responses/openai_gpt-5_20260506_161633.json) |
| `openai/gpt-5-nano` |  OK | - | [openai_gpt-5-nano_20260506_161641.json](test_cache_responses/openai_gpt-5-nano_20260506_161641.json) |
| `moonshotai/kimi-k2.5` | ❌ FAILED | Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"error":{"code":"unrecognized_request_argument","message":"Unrecognized request argument supplied: input","details":"Unrecognized request argument supplied: input"}}. Received Model Group=moonshotai/kimi-k2.5\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}} | - |
| `xiaomi/mimo-v2-pro` |  OK | - | [xiaomi_mimo-v2-pro_20260506_161656.json](test_cache_responses/xiaomi_mimo-v2-pro_20260506_161656.json) |
| `z-ai/glm-5` |  OK | - | [z-ai_glm-5_20260506_161721.json](test_cache_responses/z-ai_glm-5_20260506_161721.json) |
| `z-ai/glm-4.7-flash` |  OK | - | [z-ai_glm-4.7-flash_20260506_161724.json](test_cache_responses/z-ai_glm-4.7-flash_20260506_161724.json) |
| `z-ai/glm-4.6v` |  OK | - | [z-ai_glm-4.6v_20260506_161811.json](test_cache_responses/z-ai_glm-4.6v_20260506_161811.json) |
| `openai/gpt-5.5` |  OK | - | [openai_gpt-5.5_20260506_161816.json](test_cache_responses/openai_gpt-5.5_20260506_161816.json) |
| `deepseek/deepseek-chat-v3-0324` |  OK | - | [deepseek_deepseek-chat-v3-0324_20260506_161827.json](test_cache_responses/deepseek_deepseek-chat-v3-0324_20260506_161827.json) |


---

## Подробные результаты

### xiaomi/mimo-v2.5-pro

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/xiaomi_mimo-v2.5-pro_20260506_160506.json`

### moonshotai/kimi-k2.6

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"232c3b51-8b5b-9a21-9b6c-25560c706ca6","code":"InvalidParameter","message":"Unsupported model: \'kimi-k2.6\'."}. Received Model Group=moonshotai/kimi-k2.6\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### qwen/qwen3.6-max-preview

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"3130d080-7817-9916-bb3b-960a87156959","code":"InvalidParameter","message":"Unsupported model: \'qwen3.6-max-preview\'."}. Received Model Group=qwen/qwen3.6-max-preview\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### qwen/qwen3.6-flash

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/qwen_qwen3.6-flash_20260506_160523.json`

### qwen/qwen3.6-35b-a3b

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/qwen_qwen3.6-35b-a3b_20260506_160532.json`

### qwen/qwen3-coder-next

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"4c80c883-3dc9-9fee-afd7-c56d8f23d71f","code":"InvalidParameter","message":"Unsupported model: \'qwen3-coder-next\'."}. Received Model Group=qwen/qwen3-coder-next\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### qwen/qwen3-vl-plus

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"9123d917-8a82-9c6d-bdd5-a878ac0f4861","code":"InvalidParameter","message":"Unsupported model: \'qwen3-vl-plus\'."}. Received Model Group=qwen/qwen3-vl-plus\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### z-ai/glm-4.6v-flashx

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/z-ai_glm-4.6v-flashx_20260506_160551.json`

### yandex/gpt5-pro

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 404 - {'error': {'message': 'litellm.NotFoundError: NotFoundError: OpenAIException - 404 page not found\n. Received Model Group=yandex/gpt5-pro\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '404'}}`

### z-ai/glm-4.7

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/z-ai_glm-4.7_20260506_160557.json`

### qwen/qwen3-vl-8b-instruct

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"dc92d6fd-fcbf-92d8-9caa-16d17275729e","code":"InvalidParameter","message":"Unsupported model: \'qwen3-vl-8b-instruct\'."}. Received Model Group=qwen/qwen3-vl-8b-instruct\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### openai/gpt-5.1-chat

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-5.1-chat_20260506_160605.json`

### qwen/qwen3-vl-flash

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"f4c84d28-c11b-900b-8e79-0353cd0623af","code":"InvalidParameter","message":"Unsupported model: \'qwen3-vl-flash\'."}. Received Model Group=qwen/qwen3-vl-flash\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### openai/gpt-5.1

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-5.1_20260506_160614.json`

### z-ai/glm-4.5-air

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/z-ai_glm-4.5-air_20260506_160625.json`

### openai/gpt-4.1

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-4.1_20260506_160629.json`

### openai/gpt-5-mini

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-5-mini_20260506_160641.json`

### deepseek/deepseek-v3.2

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"48fdcb92-dfd9-95d9-9afd-6a0a77cad6b8","code":"InvalidParameter","message":"Unsupported model: \'deepseek-v3.2\'."}. Received Model Group=deepseek/deepseek-v3.2\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### z-ai/glm-4.6v-flash

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/z-ai_glm-4.6v-flash_20260506_160711.json`

### qwen/qwen3-vl-30b-a3b-thinking

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"9fc1f8d4-63e8-9a9d-8ccb-4502a894696e","code":"InvalidParameter","message":"Unsupported model: \'qwen3-vl-30b-a3b-thinking\'."}. Received Model Group=qwen/qwen3-vl-30b-a3b-thinking\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### anthropic/claude-sonnet-4

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/anthropic_claude-sonnet-4_20260506_160721.json`

### openai/gpt-5.2-chat

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-5.2-chat_20260506_160727.json`

### openai/gpt-5-chat

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-5-chat_20260506_160732.json`

### openai/gpt-4.1-mini

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-4.1-mini_20260506_160737.json`

### openai/gpt-4.1-nano

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-4.1-nano_20260506_160743.json`

### openai/chatgpt-4o-latest

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/openai_chatgpt-4o-latest_20260506_160758.json`

### openai/gpt-oss-120b

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"error":{"code":"unrecognized_request_argument","message":"Unrecognized request argument supplied: input","details":"Unrecognized request argument supplied: input"}}. Received Model Group=openai/gpt-oss-120b\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### openai/gpt-oss-20b

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-oss-20b_20260506_160802.json`

### google/gemini-2.5-pro

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {\n  "error": {\n    "code": 400,\n    "message": "* GenerateContentRequest.contents: contents is not specified\\n",\n    "status": "INVALID_ARGUMENT"\n  }\n}\n. Received Model Group=google/gemini-2.5-pro\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### qwen/qwen3-vl-235b-a22b-instruct

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"e5a80897-302b-97d2-95c0-19f66d523f4a","code":"InvalidParameter","message":"Unsupported model: \'qwen3-vl-235b-a22b-instruct\'."}. Received Model Group=qwen/qwen3-vl-235b-a22b-instruct\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### openai/gpt-5.4-nano

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-5.4-nano_20260506_160815.json`

### moonshotai/kimi-k2-0905

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/moonshotai_kimi-k2-0905_20260506_160819.json`

### qwen/qwen3.5-plus

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/qwen_qwen3.5-plus_20260506_160843.json`

### deepseek/deepseek-r1-distill-llama-70b

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/deepseek_deepseek-r1-distill-llama-70b_20260506_160857.json`

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
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"f2ab1def-af31-9369-99ba-dc02745b0e37","code":"InvalidParameter","message":"Unsupported model: \'qwen3-vl-30b-a3b-instruct\'."}. Received Model Group=qwen/qwen3-vl-30b-a3b-instruct\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### qwen/qwen3-vl-8b-thinking

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"b8268c71-b067-9ad9-ba2a-d34b607b4f2e","code":"InvalidParameter","message":"Unsupported model: \'qwen3-vl-8b-thinking\'."}. Received Model Group=qwen/qwen3-vl-8b-thinking\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### qwen/qwen3.5-flash

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/qwen_qwen3.5-flash_20260506_160945.json`

### qwen/qwen3.5-397b-a17b

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/qwen_qwen3.5-397b-a17b_20260506_161008.json`

### yandex/gpt5.1-pro

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 404 - {'error': {'message': 'litellm.NotFoundError: NotFoundError: OpenAIException - 404 page not found\n. Received Model Group=yandex/gpt5.1-pro\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '404'}}`

### yandex/gpt5-lite

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 404 - {'error': {'message': 'litellm.NotFoundError: NotFoundError: OpenAIException - 404 page not found\n. Received Model Group=yandex/gpt5-lite\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '404'}}`

### anthropic/claude-haiku-4.5

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/anthropic_claude-haiku-4.5_20260506_161019.json`

### openai/gpt-5.2

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-5.2_20260506_161022.json`

### z-ai/glm-4.6

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/z-ai_glm-4.6_20260506_161122.json`

### qwen/qwen3-max-thinking

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/qwen_qwen3-max-thinking_20260506_161128.json`

### anthropic/claude-opus-4.5

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/anthropic_claude-opus-4.5_20260506_161135.json`

### openai/gpt-5.4

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-5.4_20260506_161222.json`

### GigaChat/GigaChat-2-Max

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 404 - {'error': {'message': 'litellm.NotFoundError: NotFoundError: OpenAIException - {"error_msg":"404 Not Found"}\n. Received Model Group=GigaChat/GigaChat-2-Max\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '404'}}`

### google/gemini-3.1-flash-lite-preview

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {\n  "error": {\n    "code": 400,\n    "message": "* GenerateContentRequest.contents: contents is not specified\\n",\n    "status": "INVALID_ARGUMENT"\n  }\n}\n. Received Model Group=google/gemini-3.1-flash-lite-preview\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### anthropic/claude-sonnet-4.5

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/anthropic_claude-sonnet-4.5_20260506_161241.json`

### anthropic/claude-opus-4.7

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/anthropic_claude-opus-4.7_20260506_161248.json`

### openai/gpt-5.3-chat

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-5.3-chat_20260506_161253.json`

### meta-llama/llama-3.3-70b-instruct

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/meta-llama_llama-3.3-70b-instruct_20260506_161301.json`

### x-ai/grok-code-fast-1

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - { "code": "400", "message": "{\\"code\\":\\"Client specified an invalid argument\\",\\"error\\":\\"Unable to store messages when zdr is enabled\\"}" }. Received Model Group=x-ai/grok-code-fast-1\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### google/gemini-3.1-pro-preview

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {\n  "error": {\n    "code": 400,\n    "message": "* GenerateContentRequest.contents: contents is not specified\\n",\n    "status": "INVALID_ARGUMENT"\n  }\n}\n. Received Model Group=google/gemini-3.1-pro-preview\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### openai/gpt-5.4-mini

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-5.4-mini_20260506_161311.json`

### qwen/qwen3-235b-a22b

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"bab3737a-0868-9265-a32a-56b6abb1d835","code":"InvalidParameter","message":"Unsupported model: \'qwen3-235b-a22b\'."}. Received Model Group=qwen/qwen3-235b-a22b\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### t-tech/T-pro-it-2.0

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 404 - {'error': {'message': 'litellm.NotFoundError: NotFoundError: OpenAIException - {"error_msg":"404 Not Found"}\n. Received Model Group=t-tech/T-pro-it-2.0\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '404'}}`

### google/gemini-3.1-pro-preview-customtools

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {\n  "error": {\n    "code": 400,\n    "message": "* GenerateContentRequest.contents: contents is not specified\\n",\n    "status": "INVALID_ARGUMENT"\n  }\n}\n. Received Model Group=google/gemini-3.1-pro-preview-customtools\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### xiaomi/mimo-v2-omni

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/xiaomi_mimo-v2-omni_20260506_161325.json`

### qwen/qwen3-vl-235b-a22b-thinking

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"e12ffba5-4e88-938c-b0c3-3cf6e68352cd","code":"InvalidParameter","message":"Unsupported model: \'qwen3-vl-235b-a22b-thinking\'."}. Received Model Group=qwen/qwen3-vl-235b-a22b-thinking\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### z-ai/glm-5.1

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"327009f1-31aa-9aed-b0f0-d30e69f096b8","code":"InvalidParameter","message":"Unsupported model: \'glm-5.1\'."}. Received Model Group=z-ai/glm-5.1\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### anthropic/claude-sonnet-4.6

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/anthropic_claude-sonnet-4.6_20260506_161335.json`

### anthropic/claude-opus-4.6

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/anthropic_claude-opus-4.6_20260506_161342.json`

### xiaomi/mimo-v2.5

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/xiaomi_mimo-v2.5_20260506_161351.json`

### xiaomi/mimo-v2-flash

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/xiaomi_mimo-v2-flash_20260506_161356.json`

### deepseek/deepseek-v3.2-speciale

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/deepseek_deepseek-v3.2-speciale_20260506_161434.json`

### deepseek/deepseek-v4-pro

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"3f4f01e5-f1f0-9056-8264-992bc32ad242","code":"InvalidParameter","message":"Unsupported model: \'deepseek-v4-pro\'."}. Received Model Group=deepseek/deepseek-v4-pro\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### anthropic/claude-opus-4.1

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/anthropic_claude-opus-4.1_20260506_161451.json`

### qwen/qwen3.6-plus

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/qwen_qwen3.6-plus_20260506_161525.json`

### openai/gpt-5.4-pro

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-5.4-pro_20260506_161608.json`

### openai/gpt-4o-mini

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-4o-mini_20260506_161614.json`

### deepseek/deepseek-v4-flash

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"request_id":"5d2af640-995b-9652-a1a1-e2cfea2e196f","code":"InvalidParameter","message":"Unsupported model: \'deepseek-v4-flash\'."}. Received Model Group=deepseek/deepseek-v4-flash\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### openai/gpt-5.3-codex

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-5.3-codex_20260506_161620.json`

### openai/gpt-5.2-codex

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-5.2-codex_20260506_161625.json`

### openai/gpt-5

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-5_20260506_161633.json`

### openai/gpt-5-nano

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-5-nano_20260506_161641.json`

### moonshotai/kimi-k2.5

- **Статус:** ❌ Ошибка
- **JSON файл:** `N/A`
- **Ошибка:** `Error code: 400 - {'error': {'message': 'litellm.BadRequestError: OpenAIException - {"error":{"code":"unrecognized_request_argument","message":"Unrecognized request argument supplied: input","details":"Unrecognized request argument supplied: input"}}. Received Model Group=moonshotai/kimi-k2.5\nAvailable Model Group Fallbacks=None', 'type': None, 'param': None, 'code': '400'}}`

### xiaomi/mimo-v2-pro

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/xiaomi_mimo-v2-pro_20260506_161656.json`

### z-ai/glm-5

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/z-ai_glm-5_20260506_161721.json`

### z-ai/glm-4.7-flash

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/z-ai_glm-4.7-flash_20260506_161724.json`

### z-ai/glm-4.6v

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/z-ai_glm-4.6v_20260506_161811.json`

### openai/gpt-5.5

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/openai_gpt-5.5_20260506_161816.json`

### deepseek/deepseek-chat-v3-0324

- **Статус:**  Успешно
- **JSON файл:** `test_cache_responses/deepseek_deepseek-chat-v3-0324_20260506_161827.json`


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
