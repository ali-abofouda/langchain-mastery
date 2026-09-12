# 🦜️🔗 LangChain Learning & Experiments

مشروع تعليمي شامل وموثق لتطبيق واستكشاف مفاهيم **LangChain** وبناء تطبيقات الـ **RAG (Retrieval-Augmented Generation)** والـ **LLMs** خطوة بخطوة باستخدام أحدث المعايير ومدير الحزم فائق السرعة **`uv`**.

---

## 📁 هيكل المشروع (Project Structure)

```text
Langchain/
├── data/                                      # مجلد البيانات التجريبية
│   ├── sample.pdf                             # ملف PDF لاختبارات الـ PDF Loaders
│   └── sample.txt                             # ملف نصي مرجعي لاختبار الـ Loaders والـ Vector Stores
│
├── playground/                                # 🧪 مجلد التجارب والمسودات الحرة (Scratchpad أثناء التعلم)
│   └── README.md                              # كيفية التجربة وتوجيه الـ AI للتنظيف والتحويل
│
├── notebooks/                                 # 📓 كراسات التعليم والتجارب المفاهيمية (01 - 07)
│   ├── 01_data_ingestion/                     # استيراد واستيعاب البيانات
│   ├── 02_text_splitting/                     # تقنيات تقسيم النصوص (Chunking)
│   ├── 03_embeddings/                         # التضمينات والبحث الدلالي
│   ├── 04_vector_stores/                      # مستودعات المتجهات واستراتيجيات الاسترجاع
│   ├── 05_chains_and_lcel/                    # سلاسل LCEL وتطبيقات الذكاء الاصطناعي التوليدي
│   ├── 06_ollama_and_local_llms/              # النماذج المحلية والتتبع بـ LangSmith
│   └── 07_langserve_and_deployment/           # نشر السلاسل كـ REST API والمخرجات المهيكلة
│
├── projects/                                  # 🚀 التطبيقات والمشاريع التفاعلية المستقلة
│   ├── 01_football_rag/                       # تطبيق Football RAG (CLI + Streamlit UI)
│   │   ├── app.py                             # تطبيق سطر الأوامر التفاعلي
│   │   └── streamlit_app.py                   # تطبيق الويب التفاعلي
│   ├── 02_langserve_api/                      # خادم REST API للـ LCEL بـ LangServe & FastAPI
│   │   └── serve.py                           # سكريبت تشغيل خادم الـ REST API
│   └── 03_ollama_local_assistant/             # مساعد ذكي محلي بـ Ollama & Streamlit
│       └── app.py                             # تطبيق المساعد المحلي التفاعلي
│
└── book/                                      # 📚 الكتاب الشامل وحقيبة التعلم وأسئلة المقابلات
    ├── README.md                              # فهرس وخريطة الكتاب الشامل
    ├── 01_data_ingestion_guide.md             # دليل استيعاب وقراءة المستندات (Loaders)
    ├── 02_text_splitting_guide.md            # دليل تكتيكات واستراتيجيات تقسيم النصوص (Chunking)
    ├── 03_embeddings_and_vector_stores.md     # دليل التضمين الرقمي ومستودعات المتجهات
    ├── 04_lcel_chains_and_deployment.md       # دليل سلاسل LCEL و Pydantic و LangServe & Ollama
    ├── 05_real_world_projects_architecture.md # الدليل المعماري للمشاريع الإنتاجية والأنظمة الحقيقية
    └── 06_interview_questions_and_answers.md # 🎯 بنك أسئلة وإجابات المقابلات الشخصية (40+ Interview Q&A)
```

---

## 🔄 دورة حياة التعلم (The 4-Step Learning Lifecycle)

يقوم النظام على دورة عمل مرنة تمنحك الحرية الكاملة أثناء متابعة أي كورس:

```text
1. Playground (التجربة المسودة)  ──>  ضع أكوادك الحرة المسودة في playground/
2. Notebooks (التنظيم والتنسيق)  ──>  يقوم الـ AI بصياغتها كـ Notebook قياسي في notebooks/
3. Projects (الإفراد البرمجي)     ──>  يعزل الـ AI الأكواد التشغيلية في projects/
4. Book (التوثيق والمقابلات)     ──>  يكتب الـ AI الشرح النظري بـ book/ ويضيف أسئلة المقابلات
```

---

## 📚 المحتوى التعليمي والكتاب المرجعي (The Learning Handbook)

المشروع مبني على أركان قياسية:
1. **[playground/](file:///d:/Code/AI/Langchain/playground)**: مجلد التجارب الحرة والتطبيقات المسودة أثناء الدراسة.
2. **[notebooks/](file:///d:/Code/AI/Langchain/notebooks)**: كراسات Jupyter المفاهيمية التفاعلية خطوة بخطوة.
3. **[projects/](file:///d:/Code/AI/Langchain/projects)**: تطبيقات كاملة التشغيل والاستخدام المباشر.
4. **[book/](file:///d:/Code/AI/Langchain/book)**: الكتاب المرجعي الخاص بك الذي يشرح كافة المفاهيم مع قسم متكامل لـ **أسئلة المقابلات الشخصية (Interview Q&A)**.

---

### 1️⃣ كراسات المسارات التعليمية (Notebooks 01 - 07)
- **01 Data Ingestion**: استيراد نصوص الـ Text, PDF, Web, و Arxiv.
- **02 Text Splitting**: تكتيكات التقسيم التكراري والهيكلي وتوازن Overlap.
- **03 Embeddings**: التضمينات المحلية وبحث تشابه جيب التمام والكاش.
- **04 Vector Stores**: مستودعات FAISS, Chroma DB, Qdrant, و InMemory.
- **05 Chains & LCEL**: تعبيرات LCEL وقوالب المحادثات وسلاسل RAG.
- **06 Local LLMs & Ollama**: ربط النماذج المحلية والتتبع بـ LangSmith.
- **07 LangServe Deployment**: استخراج الـ Schemas بـ Pydantic ونشر خوادم الـ REST APIs.

### 2️⃣ التطبيقات التشغيلية المستقلة (Standalone Projects)
- **01 Football RAG**: تطبيق RAG متكامل بالـ CLI و Streamlit UI استناداً لبيانات ويكيبيديا.
- **02 LangServe API**: خادم REST API حي وجاهز للاستخدام مع Swagger & Playground.
- **03 Ollama Local Assistant**: مساعد محلي ذكي يشتغل بدون إنترنت بـ Ollama & Streamlit.

### 3️⃣ الكتاب المرجعي وبنك المقابلات (`book/`)
- **[الفصل 01 - استيعاب المستندات](file:///d:/Code/AI/Langchain/book/01_data_ingestion_guide.md)**
- **[الفصل 02 - تقنيات تقسيم النصوص](file:///d:/Code/AI/Langchain/book/02_text_splitting_guide.md)**
- **[الفصل 03 - التضمين ومستودعات المتجهات](file:///d:/Code/AI/Langchain/book/03_embeddings_and_vector_stores.md)**
- **[الفصل 04 - LCEL والنشر والنماذج المحلية](file:///d:/Code/AI/Langchain/book/04_lcel_chains_and_deployment.md)**
- **[الفصل 05 - معمارية الأنظمة والمشاريع](file:///d:/Code/AI/Langchain/book/05_real_world_projects_architecture.md)**
- **🎯 [الفصل 06 - أسئلة وإجابات المقابلات الشخصية (Interview Q&A)](file:///d:/Code/AI/Langchain/book/06_interview_questions_and_answers.md)**

---

## 🛠️ التقنيات والمكتبات المستخدمة (Tech Stack)

- **Language**: Python 3.12+
- **Environment & Package Manager**: [uv](https://github.com/astral-sh/uv)
- **Frameworks & Stores**:
  - `langchain-core`, `langchain-community`, `langchain-chroma`, `langchain-qdrant`
  - `faiss-cpu`, `chromadb`, `qdrant-client`, `scikit-learn`, `docarray`
  - `langchain-huggingface`, `sentence-transformers`, `fastembed`, `langchain-groq`
  - `pypdf`, `pymupdf`, `beautifulsoup4`, `arxiv`, `python-dotenv`

---

## 🚀 البدء والتشغيل (Getting Started)

### 1. المتطلبات الأساسية
تأكد من تثبيت مدير الحزم **uv**:
```powershell
# للتثبيت على Windows عبر PowerShell:
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. إعداد البيئة وتثبيت الحزم
```powershell
# مزامنة البيئة وتثبيت جميع الاعتماديات تلقائياً
uv sync
```

### 3. إعداد متغيرات البيئة (API Keys)
قم بنسخ ملف `.env.example` إلى `.env`:
```powershell
cp .env.example .env
```
ثم افتح ملف `.env` وقم بتعيين مفاتيحك الخاصة:
- **HF_TOKEN**: للحصول على نماذج Hugging Face.
- **GROQ_API_KEY**: للوصول إلى نماذج Groq فائقة السرعة.
- **LANGCHAIN_API_KEY** (اختياري): لتفعيل مراقبة وتتبع استدعاءات النماذج عبر LangSmith.

### 4. تشغيل كراسات Jupyter Notebooks
- افتح أي كراس داخل مجلد `notebooks/`.
- تأكد من اختيار كيرنل البيئة الافتراضية التابعة للمشروع (`.venv`).
