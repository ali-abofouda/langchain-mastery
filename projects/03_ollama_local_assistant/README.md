# 🦙 03 - Ollama Local Assistant

مساعد ذكي محلي يستند إلى خادم **Ollama** ونموذج `qwen3:8b` المفتوح المصدر مع واجهة محادثة تفاعلية أنيقة مدمجة باستخدام **Streamlit** وتتبع أداء عبر **LangSmith**.

## 🚀 كيفية التشغيل

1. تأكد من تشغيل خادم Ollama محلياً وتحميل النموذج:
   ```bash
   ollama run qwen3:8b
   ```

2. قم بتشغيل تطبيق Streamlit من جذر المشروع:
   ```bash
   uv run streamlit run projects/03_ollama_local_assistant/app.py
   ```
