<div dir="rtl">

# 🌐 07 - النشر والمخرجات المهيكلة (LangServe & Deployment)

يتناول هذا المسار كيفية تحويل سلاسل نماذج اللغات الكبيرة (LCEL Chains) إلى مخرجات ذات بنية هندسية محددة (Structured Output) ونشرها كخدمات شبكية حية (REST APIs) جاهزة للاستخدام في التطبيقات الميدانية.

## 📌 أهم المحاور النظرية في هذا المسار

### 1️⃣ المخرجات المهيكلة عبر Pydantic (`with_structured_output`):
- في النظم الإنتاجية، لا نكتفي بالحصول على نص حر من النموذج، بل نحتاج إلى بيانات مجهزة بصيغة JSON محددة الحقول والمحددات لتغدية برمجيات أخرى أو قواعد بيانات.
- يتيح LangChain استخدام مكتبة Pydantic لتعريف Schema صارمة تضم الحقول وأنواعها والوصف الموجه للنموذج.

### 2️⃣ ما هو LangServe؟
- **LangServe** هي مكتبة رسمية مدمجة مع **FastAPI** تحول أي `Runnable` أو سلسلة LCEL إلى خادم REST API مكتمل المميزات بأسطر معدودة من الكود.
- توفر تلقائياً:
  - مسارات متعددة للتفاعل (`/invoke`, `/stream`, `/batch`).
  - واجهة تجريبية تفاعلية أوتوماتيكية للـ Playgrounds على المسار `/playground`.
  - توثيق OpenAPI تفاعلي (Swagger UI).

### 3️⃣ معمارية النشر والتطوير (Production Deployment Architecture):
- فصل نموذج المنطق (LLM Logic) عن واجهة المستخدم (UI/Client).
- إتاحة السلسلة كـ Endpoint يستطيع أي كود بلغة أخرى (React, Flutter, Python) استدعاءه بسهولة وأمان.

</div>

---

<div dir="ltr">

# 🌐 07 - Deployment & Structured Outputs with LangServe & FastAPI

This module focuses on turning LCEL chains into structured, deterministic JSON data formats using Pydantic and deploying them as production-ready REST APIs using LangServe and FastAPI.

## 📌 Key Architectural Concepts

### 1️⃣ Structured Outputs (`with_structured_output`):
- Production systems require structured outputs (JSON) rather than unstructured markdown text.
- Pydantic models define strictly-typed schemas for parameters, validation, and descriptions passed to LLMs.

### 2️⃣ What is LangServe?
- **LangServe** integrates seamlessly with **FastAPI** to expose any LangChain `Runnable` object as a RESTful web service.
- Automatically generates:
  - Endpoints for `/invoke`, `/stream`, and `/batch`.
  - Built-in interactive test playground UI (`/playground`).
  - Auto-generated OpenAPI / Swagger API documentation.

### 3️⃣ Modern GenAI Deployment Architecture:
- Decouples AI chain logic from client-facing applications.
- Enables cross-language integration (Web, Mobile, Enterprise microservices) via HTTP endpoints.

</div>
