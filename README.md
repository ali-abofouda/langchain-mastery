# 🦜️🔗 LangChain Learning & Experiments

مشروع تعليمي شامل وموثق لتطبيق واستكشاف مفاهيم **LangChain** وبناء تطبيقات الـ **RAG (Retrieval-Augmented Generation)** والـ **LLMs** خطوة بخطوة باستخدام أحدث المعايير ومدير الحزم فائق السرعة **`uv`**.

---

## 📁 هيكل المشروع (Project Structure)

```text
Langchain/
├── data/                                      # مجلد الملفات والبيانات التجريبية
│   ├── sample.pdf                             # ملف PDF تجريبي لاختبار الـ PDF Loaders
│   └── sample.txt                             # ملف نصي تجريبي لاختبار TextLoader
│
├── notebooks/                                 # كراسات Jupyter Notebook التعليمية
│   ├── 01_data_ingestion/                     # المرحلة الأولى: استيراد واستيعاب البيانات
│   │   ├── 01_text_loader.ipynb               # قراءة الملفات النصية الخام (TextLoader)
│   │   ├── 02_pdf_loader.ipynb                # استخراج نصوص PDF (PyPDF & PyMuPDF)
│   │   ├── 03_web_loader.ipynb                # سحب محتوى صفحات الويب (WebBaseLoader & BeautifulSoup)
│   │   └── 04_arxiv_loader.ipynb              # جلب الأوراق العلمية والملخصات (ArxivLoader)
│   │
│   ├── 02_text_splitting/                     # المرحلة الثانية: تقنيات تقسيم النصوص (Chunking)
│   │   ├── 01_recursive_character_splitter.ipynb # التقسيم الذكي التكراري للنصوص العامة
│   │   ├── 02_character_text_splitter.ipynb   # التقسيم المباشر بناءً على فواصل محددة
│   │   ├── 03_html_splitters.ipynb            # تقسيم هياكل الويب مع الحفاظ على العناوين (HTML Splitters)
│   │   └── 04_json_splitter.ipynb             # تقسيم البيانات الهيكلية (Recursive JSON Splitter)
│   │
│   └── 03_embeddings/                         # المرحلة الثالثة: التضمينات والبحث الدلالي
│       ├── 01_huggingface_embeddings.ipynb    # نماذج التضمين المحلية وعبر Hugging Face Inference
│       ├── 02_fastembed_embeddings.ipynb      # تضمينات فائقة السرعة على المعالج (FastEmbed ONNX)
│       ├── 03_semantic_search_cosine_similarity.ipynb # البحث الدلالي وحساب تشابه جيب التمام (Cosine Similarity)
│       ├── 04_cache_backed_embeddings.ipynb   # تسريع الأداء وحفظ التضمينات مؤقتاً (CacheBackedEmbeddings)
│       └── 05_end_to_end_pipeline.ipynb       # مسار متكامل: Ingestion ➔ Splitting ➔ Embedding ➔ Search
│
├── .env                                       # ملف المفاتيح السرية (محلي - غير مرفوع للـ Git)
├── .env.example                               # نموذج متغيرات البيئة والمفاتيح المطلوبة
├── .gitignore                                 # استثناء الملفات والبيئات الافتراضية من Git
├── main.py                                    # نقطة دخول سريعة لتجارب بايثون المباشرة
├── pyproject.toml                             # تعريف الحزم والاعتماديات الخاصة بـ uv
└── README.md                                  # دليل المشروع والتوثيق الشامل
```

---

## 📚 المحتوى التعليمي والمسارات (Learning Modules)

### 1️⃣ استيعاب البيانات (Data Ingestion)
- **TextLoader**: قراءة ومعالجة الملفات النصية مع مراقبة الميتاداتا وترميز الأحرف (UTF-8).
- **PDF Loaders**: مقارنة أداء استخراج النصوص والصفحات بين `PyPDFLoader` و `PyMuPDFLoader`.
- **WebBaseLoader**: جلب المقالات والصفحات عبر الإنترنت وتنقيتها باستخدام `BeautifulSoup`.
- **ArxivLoader**: البحث المباشر في قاعدة أبحاث arXiv وتحميل ملخصات الأوراق البحثية والبيانات الوصفية.

### 2️⃣ تقسيم النصوص (Text Splitting & Chunking)
- **RecursiveCharacterTextSplitter**: المحافظة على السياق اللغوي وترابط الفقرات والجمل قبل التقسيم.
- **CharacterTextSplitter**: التقسيم المعتمد على أحرف وفواصل مخصصة مع مراعاة `chunk_size` و `chunk_overlap`.
- **HTML Splitters**: تقسيم صفحات الويب بناءً على وسمات العناوين (`<h1>`, `<h2>`, `<h3>`) لربط كل فقرة بعنوانها الأصلي.
- **RecursiveJsonSplitter**: معالجة وهيكلة ملفات الـ JSON والبيانات المتداخلة دون كسر بنية البيانات.

### 3️⃣ التضمينات النصية والبحث الدلالي (Embeddings & Semantic Search)
- **HuggingFace Embeddings**: استخدام نماذج متقدمة مفتوحة المصدر مثل `sentence-transformers/all-MiniLM-L6-v2` و `BAAI/bge-small-en-v1.5`.
- **FastEmbed**: تنفيذ سريع جداً للتضمينات باستخدام محرك ONNX المحسن للمعالجات العادية (CPU-friendly).
- **Semantic Search**: حساب الـ Cosine Similarity واسترجاع أكثر المستندات صلة دلالية بالاستعلام.
- **Cache-Backed Embeddings**: تخزين التضمينات في مخزن محلي (`LocalFileStore` أو `InMemoryByteStore`) لتجنب إعادة حساب نفس النصوص وتوفير الوقت والتكلفة.
- **End-to-End Pipeline**: تطبيق مسار متكامل يبدأ من المستندات الخام وصولاً إلى استرجاع النتائج الأكثر ملاءمة دلالياً.

---

## 🛠️ التقنيات والمكتبات المستخدمة (Tech Stack)

- **Language**: Python 3.12+
- **Environment & Package Manager**: [uv](https://github.com/astral-sh/uv)
- **Frameworks**:
  - `langchain-community`, `langchain-huggingface`, `langchain-groq`
  - `sentence-transformers`, `fastembed`
  - `pypdf`, `pymupdf`, `beautifulsoup4`, `arxiv`
  - `python-dotenv`, `ipykernel`

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
