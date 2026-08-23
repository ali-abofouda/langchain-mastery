# 🧠 03 - Embeddings & Semantic Search Guide

---

<div dir="rtl">

# 🌌 دليل التضمينات النصية والبحث الدلالي (Embeddings & Semantic Search)

## 📌 1. ما هو فضاء التضمين الدلالي (Semantic Vector Space)؟
- **التضمين (Embedding)** هو عملية تحويل النصوص والكلمات والجمل إلى **متجهات عددية عالية الأبعاد (High-Dimensional Dense Vectors)** (مثل 384 أو 768 أو 1536 رقماً).
- الميزة الجوهرية لهذا التحويل هي وضع النصوص داخل فضاء رياضي بحيث تقع **النصوص المتشابهة في المعنى والسياق قريبة جداً من بعضها البعض**، حتى لو كانت الكلمات الحرفية مختلفة تماماً (مثلاً: *"طبيب"* و *"دكتور"* أو *"سيارة"* و *"مركبة"*).

---

## 📐 2. مقاييس المسافة والتشابه الرياضي (Distance Metrics)

| المقياس | الأساس الرياضي | النطاق والقيم | التفسير واستخداماته |
| :--- | :--- | :--- | :--- |
| **تشابه جيب التمام (Cosine Similarity)** | يقيس **الزاوية** بين متجهين بغض النظر عن طولهما. | من `-1.0` إلى `+1.0` | **الأشهر في معالجة اللغات**؛ القيمة `1.0` تعني تطابقاً تاماً في الاتجاه والمعنى. |
| **المسافة الإقليدية (Euclidean L2 Distance)** | يقيس **المسافة الهندسية المستقيمة** بين نقطتين في الفضاء. | من `0.0` إلى ما لا نهاية | القيمة `0.0` تعني تطابقاً تاماً، وكلما **قلت** المسافة كان التشابه أقوى. |
| **الضرب القياسي (Dot / Inner Product)** | يقيس حاصل ضرب العناصر المتقابلة للمتجهات. | أرقام حقيقية | فعال وسريع جداً خصوصاً عند تسوية المتجهات مسبقاً (**Normalized Vectors**). |

---

## 🏷️ 3. تصنيفات محركات ونماذج التضمين

### أ. النماذج المحلية المفتوحة (Local Hugging Face Models)
- **الأشهر**: `sentence-transformers/all-MiniLM-L6-v2` (384 بعداً) و `BAAI/bge-small-en-v1.5`.
- **المميزات**: خصوصية تامة، تعمل محلياً على الجهاز بدون إرسال البيانات لأي جهة خارجية، ومجانية بنسبة 100%.

### ب. المحركات السريعة المحسنة للمعالجات (FastEmbed ONNX)
- محرك تضمين خفيف للغاية مبني على **ONNX Runtime** ومحسن لمعالجات الكمبيوتر العادية (CPU-friendly).
- يتميز بسرعة استدلال فائقة واستهلاك منخفض جداً للذاكرة.

### ج. النماذج السحابية (Cloud API Embeddings)
- مثل نماذج OpenAI (`text-embedding-3-small`) و Cohere و Google.
- تقدم جودة عالية جداً وأبعاداً ضخمة، لكنها تتطلب مفاتيح API وتكلفة مادية مع كل استدعاء.

---

## ⚡ 4. تسريع الأداء وحفظ التضمينات مؤقتاً (Cache-Backed Embeddings)
- حساب التضمينات يتطلب عمليات حسابية مجهدة على المعالج أو كروت الشاشة.
- **آلية الـ Caching**: حفظ المتجهات الناتجة في مخزن محلي (`LocalFileStore`) أو في الذاكرة؛ فإذا طُلب تضمين نفس الفقرة لاحقاً، يتم جلبها فوراً في أجزاء من الميلي ثانية دون إعادة الحساب، مما يوفر الوقت والتكلفة الحسابية.

---

## 🌐 5. البحث الدلالي متعدد اللغات (Multilingual Retrieval)
النماذج اللغوية الحديثة المخصصة للغات المتعددة تقوم بتعيين الكلمات المتكافئة من لغات مختلفة في نفس المنطقة من الفضاء المتجهي، مما يتيح البحث باستعلام باللغة العربية واسترجاع وثائق مكتوبة بالإنجليزية والعكس.

</div>

---

<div dir="ltr">

# 🧠 Vector Embeddings: Semantic Spaces & Similarity Mechanics

## 📌 1. Conceptual Foundation of Embeddings
Text embeddings map discrete lexical tokens and phrases into dense, continuous high-dimensional vector spaces. Geometric proximity in this latent space encodes contextual and conceptual similarity, bypassing the fundamental limitations of keyword-based lexical search.

---

## 📐 2. Geometric Similarity & Distance Metrics

- **Cosine Similarity ($\cos \theta$)**: Quantifies the cosine of the angle between two embedding vectors. Invariant to vector scale. Range $[-1.0, 1.0]$ where $1.0$ indicates parallel semantic alignment.
- **Euclidean Distance ($L_2$)**: Calculates absolute geometric displacement between vector coordinates. Lower values indicate proximity.
- **Dot Product / Inner Product**: Measures directional projection. For unit-normalized vectors ($\|v\| = 1$), dot product is mathematically equivalent to cosine similarity.

---

## 🏷️ 3. Embedding Engine Taxonomy

### A. Local Transformer Models (`Hugging Face / Sentence-Transformers`)
- Pure local execution, zero network egress latency, maximum data privacy.
- Standard benchmark: `all-MiniLM-L6-v2` (384-d, lightweight and highly optimized).

### B. Quantized / Accelerated Engines (`FastEmbed ONNX`)
- Hardware-optimized inference runtime utilizing ONNX quantization for near-instant CPU execution.

### C. Hosted Cloud Endpoints (OpenAI, Cohere, Voyage)
- Scalable, high-dimensional representation models accessed over REST APIs.

---

## ⚡ 4. Performance Optimization via Cache-Backed Layers
Calculating embeddings repeatedly incurs redundant computational overhead. Implementing local key-value stores (`CacheBackedEmbeddings` with persistent byte stores) avoids duplicate embedding calls and reduces processing latency to near zero.

</div>
