# 🗄️ 04 - Vector Stores & Retrievers Guide

---

<div dir="rtl">

# 🏛️ دليل مستودعات المتجهات واستراتيجيات الاسترجاع (Vector Stores & Retrievers)

## 📌 1. ما هو مستودع المتجهات (Vector Store)؟
مستودع المتجهات هو قاعدة بيانات متخصصة مصممة خصيصاً للتعامل مع متجهات التضمين (**Embedding Vectors**). 
على عكس قواعد البيانات التقليدية (SQL) التي تبحث عن تطابق النصوص الحرفي (`WHERE name = 'X'`)، يقوم مستودع المتجهات بإجراء **البحث التقريبي لأقرب الجيران (Approximate Nearest Neighbor - ANN)** للعثور على المستندات الأكثر شبهاً في المعنى والسياق في أجزاء من الميلي ثانية بين ملايين العناصر.

---

## 🏗️ 2. مقارنة معمارية شاملة لمستودعات المتجهات

| المستودع | وسيط التخزين | لغة المحرك | أبرز الميزات ونقاط القوة | متى تستخدمه؟ |
| :--- | :--- | :--- | :--- | :--- |
| **`InMemoryVectorStore`** | RAM فقط | Python | خفيف جداً، مدمج في نواة `langchain_core`، بدون أي اعتماديات خارجية. | الاختبارات السريعة، الـ Unit Tests، والجلسات المؤقتة. |
| **`FAISS`** (Meta AI) | ذاكرة + ملفات قرص ثنائية (`.faiss` / `.pkl`) | C++ | سرعة خرافية، قدرة على فهرسة مليارات المتجهات، وإمكانية دمج الفهارس (`merge_from`). | التطبيقات المحلية، الأنظمة المعزولة، والبحث عالي الكثافة. |
| **`Chroma DB`** | قرص محلي (SQLite + HNSW) | C++ / Python | سهولة فائقة، إدارة متقدمة للمجموعات، ودعم واسع للمصفوفات والـ CRUD. | النماذج الأولية المتقدمة والتطبيقات المستقلة. |
| **`Qdrant`** | ذاكرة، قرص محلي، أو خادم سحابي | Rust | كفاءة استهلاك الذاكرة، أداء فائق بالتزامن (Concurrency)، وفلترة متقدمة للـ Payload. | البيئات الإنتاجية الضخمة (Production-Ready). |
| **`Scikit-Learn`** | ملفات JSON / Parquet | Python | استخدام خوارزميات `NearestNeighbors` بدون قواعد بيانات خارجية. | الأنظمة المبنية بالكامل على بيئة Scikit-Learn. |

---

## 🎯 3. تشريح الـ Retrievers واستراتيجيات البحث في LangChain

المُسترجِع (**Retriever**) هو واجهة برمجية موحدة تأخذ نص الاستعلام وتُرجع قائمة بالمستندات الأكثر صلة. يمكن تحويل أي مستودع متجهات إلى Retriever واختيار استراتيجية البحث المناسبة:

### 1. استرجاع التشابه القياسي (`similarity`)
- **الآلية**: جلب أعلى `k` مستندات ذات أقرب مسافة متجهات.
- **التحدي**: قد يُرجع مقاطع مكررة في المعنى بصيغ مختلفة، مما يهدر مساحة نافذة السياق لدى النموذج.

### 2. استرجاع التنوع الأقصى (**`MMR - Maximal Marginal Relevance`**)
- **الآلية**: يحل مشكلة التكرار؛ حيث يفحص مجموعة أولية من المرشحات (`fetch_k`) ويختار المستندات التي تحقق توازناً بين **الصلة بالاستعلام** و**التنوع والتباين فيما بينها**.
- **المعاملات**:
  - `k`: عدد النتائج النهائية المختارة.
  - `fetch_k`: عدد المستندات الأولية التي يتم جلبها للفحص.
  - `lambda_mult`: معامل الموازنة (1.0 = صلة تامة فقط، 0.0 = أقصى تنوع، 0.5 = توازن مثالي).

### 3. استرجاع حد الثقة الأدنى (`similarity_score_threshold`)
- **الآلية**: استبعاد أي مستندات تقل درجة تطابقها عن حد أدنى محدد مسبقاً (مثل `0.75`).
- **الميزة**: حماية النموذج من استرجاع معلومات عشوائية أو غير ذات صلة عند طرح أسئلة خارج النطاق.

---

## 🔗 4. دمج المسترجعات في سلاسل الـ LCEL
في بنية LangChain الحديثة، يتم ربط الـ Retriever داخل السلسلة باستخدام عامل الربط `|`:
```text
Retriever ➔ Format Documents ➔ Prompt Template ➔ LLM Model ➔ Output Parser
```
هذه المعمارية تضمن تدفق البيانات بسلاسة فائقة وسرعة استجابة عالية مع الاستشهاد بالمصادر بدقة.

</div>

---

<div dir="ltr">

# 🏛️ Vector Stores & Retrievers: Architecture & Search Paradigms

## 📌 1. Conceptual Role of Vector Stores in RAG
Vector Stores are purpose-built database engines optimized for indexing and executing Approximate Nearest Neighbor (ANN) vector queries. They map embedding spaces onto specialized indexing structures (e.g., HNSW graphs, Inverted File indexes) to enable millisecond retrieval across dense vector collections.

---

## 🏗️ 2. Architectural Comparison Matrix

- **`InMemoryVectorStore`**: Pure ephemeral RAM storage in LangChain Core. Zero setup overhead; ideal for unit testing and transient sessions.
- **`FAISS` (Meta AI)**: Industrial-grade C++ dense vector library. Supports local persistence, sub-millisecond clustering, and dynamic index merging.
- **`Chroma DB`**: Developer-first embedded AI database with native SQLite metadata storage and intuitive collection isolation.
- **`Qdrant`**: High-performance vector engine implemented in Rust with advanced hardware quantization and rich payload filtering.
- **`Scikit-Learn Vector Store`**: Native scikit-learn nearest-neighbors execution serialized directly to JSON or Parquet formats.

---

## 🎯 3. Retrieval Strategies & Algorithmic Mechanics

### A. Top-K Similarity Search (`similarity`)
Direct nearest-neighbor projection returning the top $k$ closest items based on vector distance metric.

### B. Maximal Marginal Relevance (`MMR`)
Algorithmic balance between query relevance and result set diversity. Penalizes redundant vectors to prevent context window saturation with duplicate information:
$$\text{MMR} = \arg\max_{D_i \in R \setminus S} \left[ \lambda \cdot \text{Sim}_1(D_i, Q) - (1 - \lambda) \max_{D_j \in S} \text{Sim}_2(D_i, D_j) \right]$$

### C. Similarity Score Thresholding (`similarity_score_threshold`)
Strict quality filter excluding any candidates below a minimum confidence boundary, mitigating hallucinations on out-of-domain queries.

---

## 🔗 4. LCEL Pipeline Composition
Modern LangChain integrates retrievers directly as standard Runnables in declarative LCEL pipelines, piping retrieved context directly into grounded prompt templates.

</div>
