# 🔗 05 - Chains & LangChain Expression Language (LCEL) Guide

---

<div dir="rtl">

# 🏛️ دليل سلاسل LCEL، نماذج المحادثة وتطبيقات الذكاء الاصطناعي التوليدي

## 📌 1. ما هي لغة التعبير LCEL (LangChain Expression Language)؟
**LCEL** هي لغة توصيفية (Declarative Syntax) ومحرك معمارية السلاسل الحديث في **LangChain 0.3+**. صُممت لتسهيل بناء خطوط أنابيب الذكاء الاصطناعي التوليدي (GenAI Pipelines) من النماذج الأولية إلى بيئات الإنتاج بدون الحاجة لإعادة كتابة الأكواد.

تعتمد LCEL على مشغل الربط القياسي في بايثون `|` (The Pipe Operator) لربط المكونات المختلفة معاً بطريقة تشبه أنابيب يونكس (Unix Pipes)، حيث يمر المخرج من كل خطوة كمدخل للخطوة التالية تلقائياً:

$$\text{Input} \xrightarrow{\quad} \text{Prompt} \xrightarrow{\quad} \text{Chat Model} \xrightarrow{\quad} \text{Output Parser} \xrightarrow{\quad} \text{Result}$$

---

## ⚡ 2. الفروقات الجوهرية بين السلاسل القديمة وبنية LCEL الحديثة

| الخاصية | السلاسل التقليدية القديمة (`LLMChain`, `RetrievalQA`) | سلاسل LCEL الحديثة (LangChain 0.3+) |
| :--- | :--- | :--- |
| **طريقة الربط** | فئات موروثة معقدة مع معاملات خاصة بكل سلسلة (`from_chain_type`). | مشغل موحد وبسيط `|` يربط أي مكونات متوافقة. |
| **البث المباشر (Streaming)** | دعم محدود ويتطلب معالجات مخصصة (Custom Callbacks). | بث مباشر متأصل وتلقائي (First-Class Streaming) من النواة للواجهة. |
| **التنفيذ غير المتزامن (Async)** | يتطلب دوال منفصلة معقدة (`arun`). | دعم كامل لـ `ainvoke`, `astream`, `abatch` افتراضياً بدون إعداد إضافي. |
| **التنفيذ المتوازي (Parallelism)** | يتطلب كتابة كود Multi-threading يدوي. | تنفيذ متوازي تلقائي عبر `RunnableParallel` و القواميس البرمجية `{}`. |
| **التتبع والمراقبة (Observability)** | تسجيل جزئي وتتبع يحتاج إعدادات مكثفة. | تتبع كامل وفوري لكل خطوة ومرحلة في **LangSmith** تلقائياً. |

---

## 🧱 3. المكونات المعمارية الأساسية لسلاسل LCEL

### 1️⃣ نماذج المحادثة (Chat Models)
- نماذج مهيأة للتعامل مع قائمة من الرسائل الهيكلية (`SystemMessage`, `HumanMessage`, `AIMessage`).
- توفر منصات فائقة السرعة مثل **Groq** معالجة فورية للنماذج مفتوحة المصدر (Llama 3, Mixtral, Qwen) مع دعم كامل لمعاملات الضبط مثل `temperature` و `max_tokens`.

### 2️⃣ قوالب التوجيه المنظمة (`ChatPromptTemplate`)
- تفصل بين تعليمات النظام الدائمة (System Instructions) ومدخلات المستخدم الديناميكية (User Queries).
- تضمن عزل السياق وحماية النموذج من حقن التعليمات (Prompt Injection).

### 3️⃣ محللات المخرجات (`Output Parsers`)
- تلتقط استجابة النموذج الخام وتحولها فوراً إلى النوع المطلوب:
  - `StrOutputParser`: استخراج النص الصافي مباشرة من كائن `AIMessage`.
  - `JsonOutputParser` / `PydanticOutputParser`: تحويل المخرجات إلى كائنات بيانات مهيكلة وموثقة السكيما.

### 4️⃣ الـ Runnables وأدوات التحكم في تدفق البيانات
- **`RunnablePassthrough`**: يمرر مدخلات المستخدم الأصلية كما هي دون تعديل للخطوات التالية.
- **`RunnableParallel`**: تشغيل عدة مهام بشكل متزامن متوازي (مثل جلب السياق وتمرير السؤال في نفس اللحظة).
- **الدوال المخصصة (Custom Callables / Lambdas)**: تحويل وتجهيز البيانات (مثل دالة `format_docs` لتجميع المستندات المسترجعة).

---

## 🎯 4. معمارية منظومة الـ RAG المتكاملة عبر LCEL

في تطبيقات التوليد المعزز بالاسترجاع (Retrieval-Augmented Generation)، يتم بناء خط الأنابيب عبر LCEL وفق التسلسل المعماري التالي:

```text
               ┌──────────────────────┐
               │    User Question     │
               └──────────┬───────────┘
                          │
            ┌─────────────┴─────────────┐
            ▼                           ▼
  ┌───────────────────┐       ┌───────────────────┐
  │ Vector Retriever  │       │ RunnablePassthrough│
  └─────────┬─────────┘       └─────────┬─────────┘
            │                           │
            ▼                           │
  ┌───────────────────┐                 │
  │ format_docs(docs) │                 │
  └─────────┬─────────┘                 │
            │  { "context" }            │  { "question" }
            └─────────────┬─────────────┘
                          │
                          ▼
             ┌────────────────────────┐
             │   ChatPromptTemplate   │
             └────────────┬───────────┘
                          │
                          ▼
             ┌────────────────────────┐
             │  Chat Model (Groq LLM) │
             └────────────┬───────────┘
                          │
                          ▼
             ┌────────────────────────┐
             │    StrOutputParser     │
             └────────────┬───────────┘
                          │
                          ▼
             ┌────────────────────────┐
             │ Final Grounded Answer  │
             └────────────────────────┘
```

</div>

---

<div dir="ltr">

# 🏛️ LCEL, Chat Models & GenAI Applications Architectural Guide

## 📌 1. What is LangChain Expression Language (LCEL)?
**LCEL** is a declarative syntax and the core architectural engine in **LangChain 0.3+**. Designed to seamlessly transition generative AI pipelines from initial prototypes to enterprise-grade production without requiring code rewrites.

LCEL leverages the standard Python pipe operator `|` to compose components together in a Unix-like pipeline, automatically passing the output of one component as the input to the next:

$$\text{Input} \xrightarrow{\quad} \text{Prompt} \xrightarrow{\quad} \text{Chat Model} \xrightarrow{\quad} \text{Output Parser} \xrightarrow{\quad} \text{Result}$$

---

## ⚡ 2. Core Differences: Legacy Chains vs Modern LCEL

| Feature | Legacy Chains (`LLMChain`, `RetrievalQA`) | Modern LCEL (LangChain 0.3+) |
| :--- | :--- | :--- |
| **Composition** | Nested classes with specialized factory methods (`from_chain_type`). | Universal pipe operator `|` connecting any compatible components. |
| **Streaming** | Limited, requiring custom callback handlers. | First-class, end-to-end native streaming out of the box. |
| **Asynchronous Execution** | Required separate ad-hoc functions (`arun`). | Unified native async support (`ainvoke`, `astream`, `abatch`). |
| **Parallel Execution** | Required manual multi-threading / async boilerplate. | Automatic parallelism via `RunnableParallel` and dict syntax `{}`. |
| **Observability** | Incomplete logs needing complex instrumentation. | Instant zero-config tracing and visibility in **LangSmith**. |

---

## 🧱 3. Key Building Blocks of LCEL Chains

### 1️⃣ Chat Models
- Purpose-built interfaces structured around message types (`SystemMessage`, `HumanMessage`, `AIMessage`).
- Ultra-low latency platforms like **Groq** provide near-instant inference for leading open-source models with full parameter controls (`temperature`, `max_tokens`).

### 2️⃣ Structured Prompts (`ChatPromptTemplate`)
- Clear separation of system role instructions from dynamic user inputs.
- Prevents context leakage and shields pipelines against prompt injection vulnerabilities.

### 3️⃣ Output Parsers
- Intercepts raw model generation and parses it into clean target types:
  - `StrOutputParser`: Extracts raw string response directly from `AIMessage`.
  - `JsonOutputParser` / `PydanticOutputParser`: Enforces structured, schema-validated JSON outputs.

### 4️⃣ Runnables & Flow Control
- **`RunnablePassthrough`**: Passes input unchanged through pipeline branches.
- **`RunnableParallel`**: Executes concurrent data processing branches simultaneously.
- **Custom Callables / Lambdas**: Handles custom data formatting (such as `format_docs` for aggregating retrieved chunks).

---

## 🎯 4. End-to-End LCEL RAG Architecture

In production Retrieval-Augmented Generation workflows, LCEL orchestrates the entire lifecycle cleanly:
1. **Parallel Context & Query Routing**: The question is forwarded simultaneously to the Vector Retriever and the Prompt input.
2. **Context Aggregation**: Retrieved documents are formatted into a clean context string.
3. **Prompt Injection**: Context and Question populate the structured template.
4. **LLM Generation**: ChatGroq generates a grounded answer strictly constrained by the provided context.
5. **Output Extraction**: `StrOutputParser` delivers a clean textual response ready for downstream consumption.

</div>
