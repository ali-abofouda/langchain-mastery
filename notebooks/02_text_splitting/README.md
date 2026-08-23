# ✂️ 02 - Text Splitting & Chunking Strategies Guide

---

<div dir="rtl">

# 📑 دليل تقنيات تقسيم النصوص (Text Splitting & Chunking)

## 📌 1. لماذا نحتاج إلى تقسيم النصوص؟
تمتلك النماذج اللغوية ونماذج التضمين قيوداً صارمة على **نافذة السياق (Context Window Limits)** ومقدار النصوص التي تستطيع استيعابها في المرة الواحدة. بالإضافة إلى ذلك:
1. **التركيز الدلالي (Semantic Specificity)**: عندما نقوم بتضمين مستند ضخم كامل في متجه واحد، تتلاشى المعاني الدقيقة وتصبح المتجهات "مبهمة". تقسيم النص إلى مقاطع مركزة يجعل كل متجه يمثل فكرة محددة بوضوح تام.
2. **تقليل التشويش والتكلفة (Noise Reduction & Efficiency)**: يسمح لنظام الـ RAG باسترجاع الفقرات المحددة التي تجيب على استفسار المستخدم فقط وإرسالها للنموذج، بدلاً من إرسال مئات الصفحات غير المفيدة مما يوفر التكلفة وسرعة الاستجابة.

---

## ⚙️ 2. تشريح عملية التقطيع: `chunk_size` و `chunk_overlap`
- **حجم القطعة (`chunk_size`)**: أقصى عدد من المحارف (أو التوكنز) التي تحتويها كل قطعة نصية.
- **نسبة التداخل (`chunk_overlap`)**: مقدار المحارف المشتركة التي يتم تكرارها بين نهاية القطعة الحالية وبداية القطعة التي تليها.
  - **أهمية التداخل**: يمنع **انقطاع السياق** في منتصف جملة أو فكرة مهمة عند حدود الفصل، بحيث تظل الكلمات المترابطة مفهومة للنموذج.

---

## ⚖️ 3. معضلة تحديد حجم القطعة (The Chunk Size Trade-Off)

| حجم القطعة | الإيجابيات | السلبيات | أفضل الاستخدامات |
| :--- | :--- | :--- | :--- |
| **قطع صغيرة (100 - 300 حرف)** | دقة فائقة جداً في البحث الدلالي ومطابقة الكلمات المفتاحية. | قد تفقد السياق العام الأكبر للفقرة وتتطلب استرجاع عدد أكبر من القطع. | المعاجم، الأسئلة الشائعة (FAQ)، والحقائق الرقمية المعزولة. |
| **قطع متوسطة (400 - 800 حرف)** | توازن مثالي بين حفظ السياق والتركيز الدلالي. | الاستهلاك المعتدل للتوكنز. | **الخيار الموصى به لمعظم أنظمة الـ RAG والمحادثة العامة.** |
| **قطع كبيرة (1000 - 2000+ حرف)** | الحفاظ على السياق الكامل للمقالات والأفكار المترابطة. | قد تحتوي على معلومات مضللة أو غير ذات صلة بالاستعلام مما يزيد تشويش النموذج. | التلخيص، المستندات القانونية الطويلة، والتحليلات العميقة. |

---

## 🛠️ 4. استراتيجيات ومقسمات النصوص الرئيسية

### أ. المقسم التكراري الذكي (`RecursiveCharacterTextSplitter`)
- **الخيار الافتراضي الأقوى**: يتبع خوارزمية تدرج ذكية تعتمد على قائمة فواصل مرتبة حسب الأولوية اللغوية:
  1. `\n\n` (محاولة التقسيم عند حدود الفقرات أولاً).
  2. `\n` (إذا كانت الفقرة أطول من اللازم، ينتقل للتقسيم عند حدود الجمل).
  3. ` ` (إذا كانت الجملة طويلة، يقسم عند المسافات بين الكلمات).
  4. `""` (الملاذ الأخير لتقطيع الكلمات الطويلة حرفياً دون تجاوز الحد).
- **النتيجة**: قطع نصية متماسكة لغوياً تحافظ على بنية الجمل الطبيعية.

### ب. المقسم المباشر بالحرف (`CharacterTextSplitter`)
- يعتمد على فاصل واحد فقط (مثل السطر الجديد `\n\n`) دون محاولة التدرج الذكي في حال كانت الفقرة أطول من الحجم المحدد.

### ج. مقسمات الويب الهيكلية (`HTMLHeaderTextSplitter`)
- مصمم خصيصاً لمواقع الإنترنت؛ يقوم بتقسيم المحتوى وفقاً لوسوم العناوين (`<h1>`, `<h2>`, `<h3>`).
- **الميزة الكبرى**: يضيف مسار العناوين التي تتبع لها الفقرة في الميتاداتا تلقائياً، مما يمنح النموذج سياقاً أصلياً للفقرة حتى بعد اقتطاعها.

### د. مقسم البيانات المتداخلة (`RecursiveJsonSplitter`)
- يتعامل مع هياكل الـ JSON المعقدة من خلال تقطيع القوائم والكائنات الداخلية مع الحفاظ التام على المفاتيح (`keys`) والأقواس السليمة.

</div>

---

<div dir="ltr">

# 📑 Text Chunking: Strategies, Algorithms & Trade-Offs

## 📌 1. The Core Necessity of Text Splitting
Splitting large documents into smaller semantic units is required due to model context limitations, embedding dimensionality resolution, and token cost economics. Cohesive, granular chunks produce distinct vector representations that improve vector retrieval accuracy.

---

## ⚙️ 2. Mechanics of `chunk_size` and `chunk_overlap`
- **`chunk_size`**: The hard/soft upper bound of tokens or characters permitted per discrete chunk.
- **`chunk_overlap`**: The sliding window buffer shared across consecutive chunk boundaries. It prevents semantic severing of contiguous clauses and entity relationships.

---

## ⚖️ 3. Chunk Sizing Trade-Off Matrix

- **Small Chunks (< 300 chars)**: Maximize vector specificity and fine-grained retrieval; risk losing overarching context.
- **Medium Chunks (400 - 800 chars)**: The golden standard for standard RAG architectures, providing high semantic signal-to-noise ratio.
- **Large Chunks (> 1000 chars)**: Ideal for comprehensive document synthesis and multi-hop legal reasoning, but consume larger context budgets.

---

## 🛠️ 4. Structural Splitting Algorithms

### A. Recursive Character Splitting (`RecursiveCharacterTextSplitter`)
Hierarchical descent over natural language delimiters (`["\n\n", "\n", " ", ""]`). Prioritizes paragraph preservation before sentence and word-level fragmentation.

### B. HTML Header & Section Splitters (`HTMLHeaderTextSplitter`)
Structural DOM-aware splitting that captures structural hierarchy (`H1 -> H2 -> H3`) and injects parental metadata into child chunks.

### C. Recursive JSON Splitting (`RecursiveJsonSplitter`)
Structured object traversal that respects nested key-value invariants without breaking JSON serialization integrity.

</div>
