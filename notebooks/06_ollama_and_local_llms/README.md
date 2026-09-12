<div dir="rtl">

# 🦙 06 - النماذج المحلية والتتبع (Local LLMs & Observability)

تعتبر إدارة وتشغيل نماذج الذكاء الاصطناعي التوليدي محلياً (On-Premises / Locally) خطوة استراتيجية فائقة الأهمية للحفاظ على خصوصية البيانات، خفض التكاليف المادية، وتمكين التطوير بدون الاعتماد الكلي على مفاتيح API السحابية.

## 📌 أهم المحاور النظرية في هذا المسار

### 1️⃣ ما هو Ollama؟
- **Ollama** هو محرك وأداة مفتوحة المصدر تتيح تشغيل نماذج اللغات الكبيرة (LLMs) مثل `Llama 3`, `Qwen`, `Mistral`, و `Gemma` محلياً على جهازك الشخصي أو الخوادم الخاصة بكفاءة عالية وأوامر بسيطة.
- يتيح لك Ollama تقديم خادم محلي عبر منفذ `11434` يتعامل بسلاسة مع إطار عمل LangChain من خلال حزمة `langchain-ollama`.

### 2️⃣ مميزات استخدام النماذج المحلية:
- **الخصوصية والأمان**: البيانات لا تغادر جهازك أو شبكتك الداخلية أبداً.
- **توفير التكاليف**: عدم وجود تكاليف على عدد الـ Tokens المستهلكة أثناء مرحلة التطوير والاختبار.
- **العمل بدون إنترنت (Offline Mode)**: إمكانية تطوير واختبار تطبيقات الذكاء الاصطناعي دون الحاجة لاتصال مستمر بالإنترنت.

### 3️⃣ التتبع والمراقبة عبر LangSmith (Observability & Tracing):
- **مفهوم الـ Tracing**: تتبع كل خطوة داخل سلاسل الذكاء الاصطناعي (Prompts, Embeddings, LLM Calls, Output Parsing).
- **LangSmith**: منصة مقدمة من LangChain تتيح لك رؤية تفصيلية لوقت الاستجابة (Latency)، استخدام الـ Tokens، وتتبع أخطاء التنفيذ بكل دقة بمجرد تفعيل المتغير البيئي `LANGSMITH_TRACING=true`.

</div>

---

<div dir="ltr">

# 🦙 06 - Local LLMs & Observability with Ollama & LangSmith

Running Large Language Models (LLMs) locally provides full data privacy, cost control, and offline development capabilities. This module explores integrating local open-source models with LangChain and monitoring execution flows using LangSmith.

## 📌 Key Architectural Concepts

### 1️⃣ What is Ollama?
- **Ollama** is an open-source tool designed to package, run, and manage local open-weight models (e.g., `Qwen`, `Llama 3`, `Mistral`) using streamlined commands.
- It exposes a standardized REST interface on port `11434`, seamlessly consumed by LangChain via `langchain-ollama`.

### 2️⃣ Advantages of Local Execution:
- **Data Privacy**: Sensitive data remains inside your internal infrastructure.
- **Zero API Costs**: Eliminates token billing during rapid prototyping and experimentation.
- **Offline Reliability**: Run GenAI applications without external cloud dependencies.

### 3️⃣ Observability with LangSmith:
- **Tracing**: Inspecting prompt inputs, model completion steps, execution time, and error stack traces.
- **LangSmith Integration**: Simple environment configuration enables real-time monitoring of local model calls within LCEL chains.

</div>
