# 🦜️🔗 LangChain Learning & Experiments

مشروع تعليمي عملي لتطبيق واستكشاف مفاهيم **LangChain** والـ **RAG** والـ **LLMs** باستخدام **`uv`** كمدير للبيئة والحزم.

---

## 📁 هيكل المشروع (Project Structure)

```text
Langchain/
├── data/                               # مجلد الملفات والبيانات التجريبية
│   ├── sample.pdf                      # ملف PDF تجريبي لاختبار PyPDFLoader
│   └── sample.txt                      # ملف نصي تجريبي لاختبار TextLoader
│
├── notebooks/                          # كراسات Jupyter Notebook التعليمية
│   ├── 01_data_ingestion.ipynb         # جلب واستيعاب البيانات (Text, PDF, Web, Arxiv)
│   └── 02_text_splitting_techniques.ipynb # تقنيات تقسيم النصوص (Chunking)
│
├── .env                                # ملف المفاتيح السرية (محلي وغير مرفوع للـ Git)
├── .env.example                        # نموذج لمتغيرات البيئة المطلوبة
├── .gitignore                          # استثناء ملفات البيئة والمفاتيح من Git
├── main.py                             # نقطة دخول سريعة لتجربة النماذج عبر بايثون
├── pyproject.toml                      # إعدادات المشروع وحزم uv
└── README.md                           # دليل المشروع
```

---

## 🚀 البدء والتشغيل (Getting Started)

### 1. إعداد البيئة وتثبيت الحزم
باستخدام `uv`:
```powershell
uv sync
```

### 2. إعداد مفاتيح الـ API
انسخ ملف `.env.example` إلى `.env` وضع مفاتيحك:
```powershell
cp .env.example .env
```

### 3. تشغيل كراسات الـ Jupyter
افتح أي Notebook من مجلد `notebooks/` واختر كيرنل البيئة الافتراضية (`.venv`).
