<div dir="rtl">

# 🌐 05 - Web RAG Assistant (مساعد استعلام مقالات الويب والأبحاث)

تطبيق تفاعلي متكامل قائم على تقنية **Retrieval-Augmented Generation (RAG)** يتيح لك إدخال أي رابط مقال أو وثيقة ويب (مثل أبحاث الذكاء الاصطناعي، وثائق التوثيق، والمقالات)، ليقوم النظام باستيعابها، تقطيعها إلى قطع دلالية، وتخزينها في قاعدة متجهات **Chroma DB** محلية، ثم الإجابة على استفساراتك بدقة موثقة دون هلوسة.

---

## 🌟 المميزات الرئيسية:
- **تحميل مباشر لروابط الويب (Web Ingestion)**: عبر `WebBaseLoader`.
- **تقطيع ذكي متداخل (Chunking)**: استخدام `RecursiveCharacterTextSplitter`.
- **تضمين محلي مجاني (Local Embeddings)**: نموذج `sentence-transformers/all-MiniLM-L6-v2`.
- **قاعدة متجهات Chroma DB**: تخزين المتجهات محلياً واسترجاع أعلى المقاطع صلة.
- **نموذج Groq للتوليد التفاعلي**: أداء فائق السرعة عبر `ChatGroq`.
- **واجهتان للاستخدام**:
  1. **CLI App (`app.py`)**: تطبيق سطر أوامر تفاعلي سريع.
  2. **Streamlit Web UI (`streamlit_app.py`)**: واجهة ويب عصرية تدعم الـ **Dark Mode** والمحادثة المستمرة.

---

## 🚀 طريقة التشغيل

### 1️⃣ التأكد من المتغيرات البيئية:
قم بإنشاء وتعبئة ملف `.env` في المجلد الرئيسي للمشروع وإضافة مفتاح Groq:
```env
GROQ_API_KEY=your_groq_api_key_here
```

### 2️⃣ تشغيل تطبيق سطر الأوامر (CLI):
```bash
uv run python projects/05_web_rag_assistant/app.py
```

### 3️⃣ تشغيل واجهة الويب (Streamlit UI):
```bash
uv run streamlit run projects/05_web_rag_assistant/streamlit_app.py
```

---

## 🏗️ البنية البرمجية (Architecture)

```text
projects/05_web_rag_assistant/
├── README.md          # دليل تشغيل المشروع والشرح الفني
├── app.py             # تطبيق سطر الأوامر التفاعلي CLI
└── streamlit_app.py   # واجهة الويب التفاعلية بـ Streamlit UI (Dark Mode)
```

</div>
