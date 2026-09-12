# 🦜️🔗 LangChain Project Standards & AI Developer Guidelines

هذا الملف يحدد **المعايير القياسية، الهيكل العام، وسكيما بناء الكراسات والتوثيق (Notebooks & Documentation Schema)** المعتمدة في هذا المشروع، لضمان التناسق التام وسهولة إضافة مسارات تعليمية وتجارب جديدة لأي وكيل ذكاء اصطناعي (AI Agent) أو مطور.

---

## 🏗️ 1. المبادئ التقنية الأساسية (Core Tech Stack & Principles)

1. **مدير الحزم والبيئات الافتراضية**:
   - الاعتماد الحصري على **`uv`** لإدارة وتثبيت الحزم (`uv add <package>`, `uv sync`, `uv run python ...`).
   - إصدار بايثون المعتمد: `Python 3.12+`.

2. **معايير LangChain الحديثة (Modern Standards)**:
   - استخدام بنية **LangChain 0.3+** وتفضيل الحزم المستقلة الحديثة (`langchain-core`, `langchain-huggingface`, `langchain-chroma`, `langchain-qdrant`).
   - بناء السلاسل باستخدام **LCEL (LangChain Expression Language)** وعامل الربط `|` (تجنب الفئات القديمة مثل `LLMChain` و `RetrievalQA.from_chain_type`).
   - نموذج التضمين الافتراضي المحلي: `sentence-transformers/all-MiniLM-L6-v2` (384 بعداً، سريع، ومجاني محلياً).

3. **إدارة المفاتيح والمتغيرات**:
   - تحميل البيئة تلقائياً عبر:
     ```python
     from dotenv import load_dotenv, find_dotenv
     load_dotenv(find_dotenv())
     ```
   - دعم التوثيق الاختياري مع فحص وجود المفاتيح (`HF_TOKEN`, `GROQ_API_KEY`, `LANGCHAIN_API_KEY`).

---

## 📁 2. هيكل وتسمية المجلدات (Directory Structure Schema)

```text
Langchain/
├── AGENTS.md                                  # هذا الملف (دليل وقواعد الـ AI)
├── README.md                                  # دليل المشروع الشامل المحدث باستمرار
├── pyproject.toml                             # حزم واعتماديات uv
├── .env.example                               # نموذج المفاتيح
├── data/                                      # مجلد البيانات التجريبية
│   ├── sample.txt                             # الملف النصي المرجعي الشامل
│   └── sample.pdf                             # ملف PDF لاختبارات الـ PDF Loaders
│
├── notebooks/                                 # 📓 كراسات التعليم والتجارب المفاهيمية
│   ├── 01_data_ingestion/                     # مسار استيعاب واستيراد البيانات
│   ├── 02_text_splitting/                     # مسار تقنيات تقسيم النصوص (Chunking)
│   ├── 03_embeddings/                         # مسار التضمينات والبحث الدلالي والكاش
│   ├── 04_vector_stores/                      # مسار مستودعات المتجهات والمُسترجعات
│   ├── 05_chains_and_lcel/                    # مسار سلاسل LCEL والمنطق التفاعلي
│   ├── 06_ollama_and_local_llms/              # مسار النماذج المحلية والتتبع بـ LangSmith
│   └── 07_langserve_and_deployment/           # مسار نشر السلاسل والمخرجات المهيكلة
│
├── projects/                                  # 🚀 التطبيقات والمشاريع التفاعلية المستقلة
│   ├── 01_football_rag/                       # تطبيق Football RAG (CLI + Streamlit UI)
│   ├── 02_langserve_api/                      # خادم REST API للـ LCEL بـ LangServe & FastAPI
│   └── 03_ollama_local_assistant/             # مساعد ذكي محلي بـ Ollama & Streamlit
│
└── book/                                      # 📚 الكتاب الشامل وحقيبة التعلم وأسئلة المقابلات
    ├── README.md                              # مقدمة وفهرس الكتاب
    ├── 01_data_ingestion_guide.md             # الشرح الشامل لاستيعاب وقراءة المستندات
    ├── 02_text_splitting_guide.md            # الشرح الشامل لاستراتيجيات تقنيات التقسيم
    ├── 03_embeddings_and_vector_stores.md     # الشرح الشامل للتضمين ومستودعات المتجهات
    ├── 04_lcel_chains_and_deployment.md       # الشرح الشامل لـ LCEL, LangServe, Ollama & LangSmith
    ├── 05_real_world_projects_architecture.md # الشرح المعماري لمشاريع الـ RAG والأنظمة الحقيقية
    └── 06_interview_questions_and_answers.md # 🎯 بنك أسئلة وأجوبة المقابلات الشخصية (Interview Q&A)
```

### 🏷️ قواعد تسمية المجلدات والملفات:
- **المجلدات**: `<number>_<topic_name>` (مثال: `01_data_ingestion`, `05_chains_and_lcel`).
- **دليل المجلد النظري**: **إلزامي** إنشاء ملف `README.md` داخل كل مجلد يشرح المفاهيم المعمارية والنظرية بالتفصيل باللغتين العربية والإنجليزية **بدون كود** مع ضبط اتجاه النصوص (`<div dir="rtl">` للعربية و `<div dir="ltr">` للإنجليزية).
- **الكراسات المفردة**: `<number>_<specific_technique>.ipynb` (مثال: `01_text_loader.ipynb`, `02_faiss_vector_store.ipynb`).
- **الكراس الختامي في كل مجلد**: **إلزامي** إنشاء كراس باسم `<last_number>_end_to_end_<topic>.ipynb` يجمع كل ما تم شرحه في المجلد من الصفر وحتى خط النهاية.

---

## 📓 3. سكيما وهيكل الـ Jupyter Notebook (Notebook Schema)

كل كراس يتم إنشاؤه **يجب** أن يتبع الترتيب القياسي التالي:

### 1. خلية المقدمة والشرح النظري (Markdown Cell):
- تبدأ بوسم المحاذاة لليمين `<div dir="rtl">`.
- عنوان رئيسي جذاب مع إيموجي ورقم الكراس بالإنجليزية.
- شرح مبسط ومباشر للمفهوم باللغة العربية (ما هو؟ ولماذا نستخدمه؟ وما هي أهم مميزاته؟).

```markdown
<div dir="rtl">

# 🗄️ 01 - Feature Name in LangChain

## ما هو [المفهوم]؟
- شرح موجز ومركّز للنقاط الأساسية.
- الفوائد العملية واستخداماته في مشاريع الـ RAG والذكاء الاصطناعي.

</div>
```

### 2. خلية تحميل البيئة ونموذج التضمين (Code Cell):
```python
import os
from pathlib import Path
from dotenv import load_dotenv, find_dotenv
from langchain_core.documents import Document

# تحميل البيئة
load_dotenv(find_dotenv())

# تحديد مسار مجلد البيانات
DATA_DIR = Path("data") if Path("data").exists() else Path("../../data") if Path("../../data").exists() else Path("../data")
```

### 3. خطوات تعليمية مرقمة تفاعلية (`### 1️⃣`, `### 2️⃣`, `### 3️⃣`):
- كل خطوة كود يسبقها صندوق Markdown توضيحي بالعربية يشرح:
  - ماذا سنفعل في هذا المقطع البرمجي؟
  - ما هي المعاملات (Parameters) المستخدمة ولماذا تم اختيارها؟
- كتابة أكواد واضحة مع طباعة مخرجات ورسائل نجاح مفيدة ومريحة للقارئ (`✅ تم تحميل المستند...`, `📊 عدد القطع: ...`).

### 4. خاتمة وخلاصة عملية (Summary & Next Steps):
- تلخيص سريع لأبرز ما تم تعلمه وربطه بالخطوة التالية في مسار التعلم.

---

## 🧪 4. معايير كتابة واختبار الأكواد (Code Quality Standards)

1. **التعامل مع المسارات بمرونة**:
   - استخدام `pathlib.Path` مع التحقق من مسار مجلد `data/` ليعمل الكود بنجاح سواء تم تشغيل الكراس من مجلده الفرعي أو من المجلد الرئيسي.
2. **الاستقلالية وسهولة التشغيل**:
   - يجب أن يكون كل كراس قابلاً للتشغيل التلقائي دون الاعتماد على متغيرات معرفة في كراسات سابقة.
3. **تجنب المكتبات المنتهية صلاحيتها**:
   - استخدام `from langchain_text_splitters import ...` بدلاً من `langchain.text_splitter`.
   - استخدام `from langchain_core.prompts import PromptTemplate` بدلاً من المسارات القديمة.
   - استخدام `from langchain_core.runnables import RunnablePassthrough`.

---

## 🔄 5. بروتوكول التحديث عند إضافة أي ميزة جديدة (Update Checklist)

عند قيام أي وكيل AI أو مطور بإضافة موضوع أو مجلد أو كراس جديد:
- [ ] التأكد من تثبيت الحزم المطلوبة عبر `uv add <package>` وتحديث `pyproject.toml`.
- [ ] إنشاء ملف `README.md` النظري ثنائي اللغة داخل المجلد (بدون كود).
- [ ] تطبيق سكيما الكراسات المذكورة أعلاه مع التوثيق بالعربية.
- [ ] إضافة كراس `end_to_end` ختامي في نهاية كل مجلد مسار.
- [ ] تحديث ملف **`README.md`** الرئيسي ليعكس:
  1. شجرة المجلدات والملفات الجديدة.
  2. ملخص المسار التعليمي في قسم `Learning Modules`.
  3. قائمة الحزم في قسم `Tech Stack`.

---

## 🔄 6. بروتوكول تحويل التجارب الحرة (Playground to Production Protocol)

يعمل وكيل الذكاء الاصطناعي (AI Agent) كـ **مهندس مراجعة وتنظيم (Code Refactoring & Documentation Engineer)** لتحويل مسودات المستخدم من مجلد `playground/` إلى أصل برمجي ومعرفي منظم.

### 📋 خطوات بروتوكول تحويل التجارب المسودة:
1. **التحليل الفني لتجارب الـ `playground/`**:
   - فحص الكود والتجارب المسودة المكتوبة في مجلد `playground/` وتحديد المفاهيم والأدوات المستخدمة فيها.
2. **إعادة الهيكلة والتنسيق في `notebooks/`**:
   - إعادة صياغة الكود وفق سكيما Jupyter Notebook القياسية باللغة العربية (مقدمة اتجاهية، تحميل مرن للمسارات عبر `pathlib.Path` مع `dotenv`، خطوات تفاعلية مرقمة `### 1️⃣` وتلخيص ختامي).
   - تحديث الكراس الختامي `end_to_end` للمسار المعني.
3. **الفصل والتحويل إلى `projects/`**:
   - إذا تضمنت المسودة تطبيقاً تشغيلياً كاملاً (واجهة Streamlit UI، خادم FastAPI & LangServe، أو تطبيق CLI)، يتم إفراده داخل مجلد مستقل بحزمة `projects/<number>_<project_name>/` مع ملف `README.md` توضيحي لطريقة التشغيل بـ `uv`.
4. **إثراء الكتاب المرجعي `book/`**:
   - كتابة الشرح النظري والمعماري الشامل للمفهوم في الفصل المناسب داخل مجلد `book/` بالترتيب المنطقي السليم.
   - إضافة أسئلة وأجوبة مقابلات تقنية متعمقة ذات صلة للمفهوم الجديد في ملف `book/06_interview_questions_and_answers.md`.
5. **تحديث التوثيق وتأكيد الجودة**:
   - تحديث الشجرة الرئيسية والملخصات في ملف `README.md`.
   - إجراء فحص تجميع أكواد بايثون وفحص الـ JSON للـ Notebooks للتأكد من خلو المشروع من الأخطاء.

