# 🦜️🔗 LangChain Learning & Experiments

مشروع تعليمي شامل وموثق لتطبيق واستكشاف مفاهيم **LangChain** وبناء تطبيقات الـ **RAG (Retrieval-Augmented Generation)** والـ **LLMs** خطوة بخطوة باستخدام أحدث المعايير ومدير الحزم فائق السرعة **`uv`**.

---

## 📁 هيكل المشروع (Project Structure)

```text
Langchain/
├── data/                                      # مجلد الملفات والبيانات التجريبية وقواعد البيانات
│   ├── sample.pdf                             # ملف PDF تجريبي لاختبار الـ PDF Loaders
│   └── sample.txt                             # ملف نصي شامل لاختبار الـ Loaders والـ Vector Stores
│
├── notebooks/                                 # كراسات Jupyter Notebook التعليمية
│   ├── 01_data_ingestion/                     # المرحلة الأولى: استيراد واستيعاب البيانات
│   │   ├── README.md                          # 📖 الدليل النظري المفاهيمي الشامل (عربي / English)
│   │   ├── 01_text_loader.ipynb               # قراءة الملفات النصية الخام (TextLoader)
│   │   ├── 02_pdf_loader.ipynb                # استخراج نصوص PDF (PyPDF & PyMuPDF)
│   │   ├── 03_web_loader.ipynb                # سحب محتوى صفحات الويب (WebBaseLoader & BeautifulSoup)
│   │   ├── 04_arxiv_loader.ipynb              # جلب الأوراق العلمية والملخصات (ArxivLoader)
│   │   └── 05_end_to_end_data_ingestion.ipynb # 🚀 مسار استيعاب متكامل من الصفر لكافة المصادر
│   │
│   ├── 02_text_splitting/                     # المرحلة الثانية: تقنيات تقسيم النصوص (Chunking)
│   │   ├── README.md                          # 📖 الدليل النظري المفاهيمي الشامل (عربي / English)
│   │   ├── 01_recursive_character_splitter.ipynb # التقسيم الذكي التكراري للنصوص العامة
│   │   ├── 02_character_text_splitter.ipynb   # التقسيم المباشر بناءً على فواصل محددة
│   │   ├── 03_html_splitters.ipynb            # تقسيم هياكل الويب مع الحفاظ على العناوين (HTML Splitters)
│   │   ├── 04_json_splitter.ipynb             # تقسيم البيانات الهيكلية (Recursive JSON Splitter)
│   │   └── 05_end_to_end_text_splitting.ipynb # 🚀 مسار متكامل لتقسيم وتحليل جودة النصوص
│   │
│   ├── 03_embeddings/                         # المرحلة الثالثة: التضمينات والبحث الدلالي
│   │   ├── README.md                          # 📖 الدليل النظري المفاهيمي الشامل (عربي / English)
│   │   ├── 01_huggingface_embeddings.ipynb    # نماذج التضمين المحلية وعبر Hugging Face Inference
│   │   ├── 02_fastembed_embeddings.ipynb      # تضمينات فائقة السرعة على المعالج (FastEmbed ONNX)
│   │   ├── 03_semantic_search_cosine_similarity.ipynb # البحث الدلالي وحساب تشابه جيب التمام (Cosine Similarity)
│   │   ├── 04_cache_backed_embeddings.ipynb   # تسريع الأداء وحفظ التضمينات مؤقتاً (CacheBackedEmbeddings)
│   │   └── 05_end_to_end_pipeline.ipynb       # 🚀 مسار التضمينات والبحث الدلالي والكاش المتكامل
│   │
│   ├── 04_vector_stores/                      # المرحلة الرابعة: مستودعات المتجهات واستراتيجيات الاسترجاع
│   │   ├── README.md                          # 📖 الدليل النظري المفاهيمي الشامل (عربي / English)
│   │   ├── 01_in_memory_vector_store.ipynb    # المستودع المدمج بالذاكرة في نواة LangChain Core
│   │   ├── 02_faiss_vector_store.ipynb        # مكتبة FAISS من Meta (حفظ محلي، مسافات L2، ودمج الفهارس)
│   │   ├── 03_chroma_vector_store.ipynb       # مستودع Chroma DB (تخزين دائم، مجموعات، وفلترة متقدمة)
│   │   ├── 04_qdrant_vector_store.ipynb       # محرك Qdrant بلغة Rust (أداء فائق وفلترة بالـ Payload)
│   │   ├── 05_docarray_and_sklearn_stores.ipynb # مستودعات خفيفة تعتمد على Scikit-Learn و DocArray
│   │   ├── 06_retrievers_and_search_types.ipynb # استراتيجيات الاسترجاع المتقدمة (Similarity, MMR, Threshold, LCEL)
│   │   └── 07_end_to_end_rag_vector_pipeline.ipynb # 🚀 منظومة RAG متكاملة من التحميل للـ QA الموثق
│   │
│   └── 05_chains_and_lcel/                    # المرحلة الخامسة: سلاسل LCEL وتطبيقات الذكاء الاصطناعي التوليدي
│       ├── README.md                          # 📖 الدليل النظري المفاهيمي الشامل (عربي / English)
│       ├── 01_chat_models_and_prompts.ipynb   # نماذج المحادثة (ChatGroq) وقوالب التوجيه (ChatPromptTemplate)
│       ├── 02_lcel_and_output_parsers.ipynb   # لغة التعبير LCEL ومحللات المخرجات (StrOutputParser & Runnables)
│       ├── 03_rag_chains_with_retrievers.ipynb # بناء سلاسل RAG متقدمة وربط الـ Retrievers بالسلاسل
│       └── 04_end_to_end_web_rag_app.ipynb    # 🚀 تطبيق GenAI متكامل من صفحات الويب إلى إجابات موثقة
│
├── .env                                       # ملف المفاتيح السرية (محلي - غير مرفوع للـ Git)
├── .env.example                               # نموذج متغيرات البيئة والمفاتيح المطلوبة
├── .gitignore                                 # استثناء الملفات والبيئات الافتراضية من Git
├── AGENTS.md                                  # سكيما ومعايير الـ AI والمطورين لإضافة المسارات
├── main.py                                    # نقطة دخول سريعة لتجارب بايثون المباشرة
├── pyproject.toml                             # تعريف الحزم والاعتماديات الخاصة بـ uv
└── README.md                                  # دليل المشروع والتوثيق الشامل
```

---

## 📚 المحتوى التعليمي والمسارات (Learning Modules)

كل مسار تعليمي يشتمل على **دليل نظري معماري مستقل (`README.md`)** باللغتين العربية والإنجليزية يشرح المفاهيم بدون كود، بالإضافة لكراسات التطبيق العملي والكراس الختامي الشامل:

### 1️⃣ استيعاب البيانات (Data Ingestion)
- **📖 الدليل النظري**: [01_data_ingestion/README.md](file:///d:/Code/AI/Langchain/notebooks/01_data_ingestion/README.md)
- **TextLoader**: قراءة ومعالجة الملفات النصية مع مراقبة الميتاداتا وترميز الأحرف (UTF-8).
- **PDF Loaders**: مقارنة أداء استخراج النصوص والصفحات بين `PyPDFLoader` و `PyMuPDFLoader`.
- **WebBaseLoader**: جلب المقالات والصفحات عبر الإنترنت وتنقيتها باستخدام `BeautifulSoup`.
- **ArxivLoader**: البحث المباشر في قاعدة أبحاث arXiv وتحميل ملخصات الأوراق البحثية والبيانات الوصفية.
- **🚀 End-to-End Pipeline**: دمج كافة المصادر المتعددة في قائمة موحدة من الـ Documents وإثراء الميتاداتا وفحص الجودة.

### 2️⃣ تقسيم النصوص (Text Splitting & Chunking)
- **📖 الدليل النظري**: [02_text_splitting/README.md](file:///d:/Code/AI/Langchain/notebooks/02_text_splitting/README.md)
- **RecursiveCharacterTextSplitter**: المحافظة على السياق اللغوي وترابط الفقرات والجمل قبل التقسيم.
- **CharacterTextSplitter**: التقسيم المعتمد على أحرف وفواصل مخصصة مع مراعاة `chunk_size` و `chunk_overlap`.
- **HTML Splitters**: تقسيم صفحات الويب بناءً على وسمات العناوين (`<h1>`, `<h2>`, `<h3>`) لربط كل فقرة بعنوانها الأصلي.
- **RecursiveJsonSplitter**: معالجة وهيكلة ملفات الـ JSON والبيانات المتداخلة دون كسر بنية البيانات.
- **🚀 End-to-End Pipeline**: خط أنابيب شامل يقسم المستندات المتنوعة ويحلل إحصائيات الجودة (min/max/avg length).

### 3️⃣ التضمينات النصية والبحث الدلالي (Embeddings & Semantic Search)
- **📖 الدليل النظري**: [03_embeddings/README.md](file:///d:/Code/AI/Langchain/notebooks/03_embeddings/README.md)
- **HuggingFace Embeddings**: استخدام نماذج متقدمة مفتوحة المصدر مثل `sentence-transformers/all-MiniLM-L6-v2` و `BAAI/bge-small-en-v1.5`.
- **FastEmbed**: تنفيذ سريع جداً للتضمينات باستخدام محرك ONNX المحسن للمعالجات العادية (CPU-friendly).
- **Semantic Search**: حساب الـ Cosine Similarity واسترجاع أكثر المستندات صلة دلالية بالاستعلام.
- **Cache-Backed Embeddings**: تخزين التضمينات في مخزن محلي (`LocalFileStore` أو `InMemoryByteStore`) لتجنب إعادة حساب نفس النصوص وتوفير الوقت والتكلفة.
- **🚀 End-to-End Pipeline**: مسار متكامل يبدأ من المستندات الخام وصولاً إلى استرجاع النتائج الأكثر ملاءمة دلالياً وحساب التشابه الرياضي يدوياً.

### 4️⃣ مستودعات المتجهات والمُسترجعات (Vector Stores & Retrievers)
- **📖 الدليل النظري**: [04_vector_stores/README.md](file:///d:/Code/AI/Langchain/notebooks/04_vector_stores/README.md)
- **InMemoryVectorStore**: مستودع خفيف جداً مدمج في `langchain_core` للاختبارات السريعة والجلسات المؤقتة.
- **FAISS (Facebook AI)**: الفهرسة عالية الكفاءة للمتجهات الكثيفة، حساب مسافات L2، حفظ وتحميل الفهارس محلياً (`save_local` / `load_local`)، ودمج عدة فهارس (`merge_from`).
- **Chroma DB**: تخزين دائم على القرص (`persist_directory`)، إدارة المجموعات، وعمليات الفلترة المتقدمة بالمعاملات المنطقية (`$and`, `$gte`, `$in`).
- **Qdrant**: محرك متجهي فائق السرعة بلغة Rust، يدعم التشغيل بالذاكرة أو على القرص أو عبر السحابة مع فلترة الـ Payload.
- **Scikit-Learn & DocArray**: بناء مستودعات متجهية محلية باستخدام خوارزميات `NearestNeighbors` في Scikit-Learn مع خيارات الحفظ بصيغة JSON و Parquet.
- **Retrievers & Search Strategies**: تحويل أي مستودع إلى Retriever واستخدام أنماط بحث متطورة (`similarity`, `mmr`, `similarity_score_threshold`).
- **🚀 End-to-End RAG Pipeline**: تطبيق منظومة RAG كاملة تبدأ من النص الخام، تمر بالتقسيم والتضمين والفهرسة بالـ FAISS، ثم الـ MMR Retriever وربطها بسلسلة LCEL و Prompt موجه لتقديم إجابات موثقة بالأدلة.

### 5️⃣ سلاسل LCEL وتطبيقات الذكاء الاصطناعي التوليدي (Chains & LCEL)
- **📖 الدليل النظري**: [05_chains_and_lcel/README.md](file:///d:/Code/AI/Langchain/notebooks/05_chains_and_lcel/README.md)
- **Chat Models & Prompts**: استخدام نماذج `ChatGroq` الفائقة السرعة وقوالب التوجيه المنظمة `ChatPromptTemplate` والبث الحي (Streaming).
- **LCEL & Output Parsers**: المعمارية الحديثة بمشغل الربط `|`، واستخراج النصوص النظيفة عبر `StrOutputParser` وإدارة التدفق بـ `RunnablePassthrough` و `RunnableParallel`.
- **RAG Chains with Retrievers**: ربط مستودعات المتجهات بالسلاسل التوليدية، تنسيق السياق (`format_docs`) وصياغة قوالب تمنع الهلوسة.
- **🚀 End-to-End Web RAG App**: تطبيق GenAI متكامل من استيعاب صفحات الويب الحية عبر `WebBaseLoader`، تقسيم النصوص، التضمين المحلي، الفهرسة بـ FAISS، وحتى الرد التفاعلي الموثق.

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
