# ⚽ 01 - Football RAG Application

تطبيق عملي متكامل لمنظومة **Retrieval-Augmented Generation (RAG)** يستخرج ويعالج بيانات كرة القدم المباشرة من ويكيبيديا ويقدم إجابات موثقة باللغة العربية والإنجليزية، مع توفير واجهتين: واجهة سطر الأوامر (CLI) وواجهة ويب تفاعلية بـ Streamlit UI.

## 📁 محتويات المشروع

- `streamlit_app.py`: تطبيق الويب التفاعلي الأنيق المزود بتاريخ المحادثات وعرض المصادر المرجعية.
- `app.py`: تطبيق تفاعلي سريع عبر سطر الأوامر (CLI).
- `README.md`: دليل وتشغيل المشروع.

## 🚀 كيفية التشغيل

### 1. تشغيل واجهة الويب (Streamlit App)
من المجلد الرئيسي للمشروع:
```bash
uv run streamlit run projects/01_football_rag/streamlit_app.py
```

### 2. تشغيل تطبيق سطر الأوامر (CLI App)
من المجلد الرئيسي للمشروع:
```bash
uv run python projects/01_football_rag/app.py
```
