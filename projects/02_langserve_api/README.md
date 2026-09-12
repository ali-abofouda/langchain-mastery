# 🌐 02 - LangServe REST API Server

خادم REST API مكتمل ومبني باستخدام **FastAPI** و **LangServe** لنشر سلاسل LangChain كخدمات شبكية حية مع واجهة اختباره التفاعلية (Playground UI) وتوثيق OpenAPI تلقائي.

## 🚀 كيفية التشغيل

من المجلد الرئيسي للمشروع، قم بتشغيل الخادم:
```bash
uv run python projects/02_langserve_api/serve.py
```

سيتم فتح الخادم على:
- **API Endpoint**: `http://localhost:8000/chain/invoke`
- **Interactive Playground**: `http://localhost:8000/chain/playground/`
- **Swagger Documentation**: `http://localhost:8000/docs`
