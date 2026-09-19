<div dir="rtl">

# 🎯 الفصل السادس: بنك أسئلة وأجوبة المقابلات الشخصية (Interview Q&A Guide)

مرحباً بك في الذخيرة المعرفية الشاملة لإتقان المقابلات الشخصية الخاصة بوظائف **مهندس RAG (RAG Engineer)** و **مطور الذكاء الاصطناعي (AI Application Developer)**. يغطي هذا الفصل أكثر من 40 سؤاالاً تقنياً متعمقاً مقسماً بحسب المحاور التكنولوجية.

---

## 📌 1. مفاهيم الـ RAG وتقسيم النصوص (RAG & Chunking Fundamentals)

### س1: ما هو الـ RAG ولماذا نلجأ إليه بدلاً من إعادة تدريب النموذج (Fine-Tuning)؟
- **الإجابة**:
  - **الـ RAG (Retrieval-Augmented Generation)**: هو أسلوب يربط النموذج بقواعد بيانات ومعرفة خارجية مسترجعة لحظياً أثناء الاستعلام.
  - **لماذا نرجحه على Fine-Tuning؟**:
    1. **التكلفة والسرعة**: الـ RAG لا يتطلب استهلاك طاقة كمبيوتر ضخمة لإعادة تدريب الأوزان.
    2. **تحديث البيانات الحظي**: تحديث المعلومات في الـ RAG يتطلب إضافة ملف لقاعدة المتجهات فقط، بينما الـ Fine-Tuning يتطلب إعادة التدريب.
    3. **منع الهلوسة والشفافية**: الـ RAG يوفر مرجعية ومصادر محددة للإجابة.

### س2: ما الفرق بين `chunk_size` و `chunk_overlap`؟ وما تأثير زيادة أو نقصان كل منهما؟
- **الإجابة**:
  - **`chunk_size`**: الحجم الأقصى للقطعة النصية.
    - إذا كان صغيراً جداً: تضيع الفكرة المكتملة والسياق اللغوي.
    - إذا كان كبيراً جداً: يحتوي على معلومات مشتتة قد تقلل من دقة التضمين (Embedding Noise) وتستهلك نافذة السياق.
  - **`chunk_overlap`**: حجم الأحرف المتداخلة بين القطع المتجاورة.
    - يمنع ضياع المفهوم أو قطع الجملة في المنتصف، ويضمن وجود سياق رابط بين القطع.

### س3: كيف يعمل `RecursiveCharacterTextSplitter` في LangChain ولماذا يُعد الخيار القياسي الأول؟
- **الإجابة**:
  يعمل تكرارياً بناءً على قائمة مرتبة من الفواصل `["\n\n", "\n", " ", ""]`. يبدأ بمحاولة التقسيم عند الفقرات أولاً، ثم الأسطر، ثم الكلمات، مما يحافظ على السياق اللغوي وسلامة الفقرات قدر الإمكان مقارنة بالتقسيم المباشر عند عدد أحرف ثابت.

---

## 📌 2. التضمين ومستودعات المتجهات (Embeddings & Vector Databases)

### س4: ما الفرق بين البحث بـ Cosine Similarity والبحث بـ Euclidean Distance (L2)؟
- **الإجابة**:
  - **Cosine Similarity**: يقيس الزاوية بين المتجهين بغض النظر عن طول المتجه. ممتاز للنصوص والكلمات لأن المهم هو اتجاه المعنى وليس طول المستند.
  - **Euclidean Distance (L2)**: يقيس المسافة الخطية المباشرة بين نقطتين في الفضاء. يتأثر بطول وشحنة المتجهات.

### س5: قارن بين FAISS و Chroma DB و Qdrant متى تختار كلاً منهم في مشاريعك؟
- **الإجابة**:
  - **FAISS**: مكتبة محددة من Meta سريعة جداً بالفهرسة بالذاكرة محلياً، ممتازة للتطبيقات المحلية والسريعة.
  - **Chroma DB**: مستودع متجهات خفيف يدعم التخزين الدائم على القرص بسهولة، ممتاز للمشاريع الصغيرة والمتوسطة.
  - **Qdrant**: محرك متجهات فائق الأداء بلغة Rust، يدعم التوسع السحابي (Distributed)، والفلترة المتقدمة بالـ Payload، وهو الخيار الأنسب للمؤسسات والأنظمة الضخمة.

### س6: ما هي تقنية `CacheBackedEmbeddings` ومتى تستخدمها؟
- **الإجابة**:
  هي تقنية لحفظ المتجهات التي تم حسابها سابقاً في مخزن كاش (مثل `LocalFileStore`). تُستخدم لتجنب إعادة حساب المتجهات لنفس المستندات مراراً وتكراراً، مما يوفر الوقت والتكلفة المالية بشكل كبير.

---

## 📌 3. معمارية LCEL والـ Modern LangChain Standards

### س7: ما هي LCEL وما الميزة التي تقدمها مقارنة بالسلاسل القديمة (مثل LLMChain)؟
- **الإجابة**:
  **LCEL (LangChain Expression Language)** هي لغة تعبير حديثة قائمة على مشغل الربط `|`.
  - **المميزات**:
    1. تدعم البث الحي (Streaming) والتنفيذ غير التزامني (Async) تلقائياً.
    2. توفر تنفيذ العمليات بالتوازي (Parallel Execution).
    3. سهولة الصيانة والتتبع (Observability) والدمج المباشر مع LangSmith.

### س8: كيف تعمل خاصية `with_structured_output` مع Pydantic؟
- **الإجابة**:
  تقوم بتقييد نموذج اللغة التوليدي لإرجاع البيانات بصيغة JSON مطابقة لسكيما معرفة عبر Pydantic (`BaseModel`)، حيث يتم إرسال مواصفات الحقول والـ Types في الـ System Prompt أو عبر Function Calling الخاصة بالنموذج.

---

## 📌 4. النماذج المحلية والأنظمة الإنتاجية (Ollama, LangServe & System Design)

### س9: ما فائدة استخدام LangServe والنشر كـ REST API؟
- **الإجابة**:
  يفصل منطق الـ AI المكتوب بـ LangChain عن واجهات المستخدم (مواقع، تطبيقات جوال). يتيح التفاعل عبر مسارات قياسية مثل `/invoke` و `/stream` مع إنشاء واجهة تجريبية تلقائية `/playground`.

### س10: كيف تمنع الهلوسة (Anti-Hallucination) في مشاريع الـ RAG؟
- **الإجابة**:
  1. صياغة Prompt موجه صارم يلزم النموذج بالرد فقط من واقع الـ Context الموفر.
  2. توجيه النموذج للرد بـ "لا أعلم" عند غياب المعلومة في السياق.
  3. حجب المستندات ذات نسبة التشابه المنخفضة باستخدام `similarity_score_threshold`.
  4. استخدام تقنيات الـ Reranking لإعادة ترتيب النتائج قبل إرسالها للنموذج.

### س11: كيف تتعامل مع إدارة الذاكرة وسجل المحادثات (Chat History) في LangChain 0.3+؟
- **الإجابة**:
  استخدام الفئة القياسية `RunnableWithMessageHistory` مع دالة إرجاع السجل `get_session_history` وتضمين `MessagesPlaceholder(variable_name="messages")` داخل التوجيه. يتم التحكم بالفصل التام بين الجلسات بمرور `session_id` مختلف في الـ `configurable`.

### س12: ما هي خوارزمية HNSW المستعملة في Chroma DB وكيف تختلف عن التفتيش الخطي (Flat Search)؟
- **الإجابة**:
  - **HNSW (Hierarchical Navigable Small World)**: تبني رسماً بيانياً متعدد الطبقات يربط النقاط القريبة ببعضها على هيئة شبكة عالمية صغيرة.
  - **الفارق**: التفتيش الخطي يفحص كل المتجهات بشرط $O(N \cdot D)$ وهو بطيء مع زيادة المستندات، بينما HNSW تبحث في طبقات الشبكة في زمن تعقيدي $O(\log N)$ مع الحفاظ على دقة مطابقة تتجاوز 98%.

### س13: ما دور الاستعلام الجماعي المتوازي (`retriever.batch`) وكيف يحسن أداء الخوادم الإنتاجية؟
- **الإجابة**:
  يتيح إرسال قائمة من الأسئلة المتعددة دفعة واحدة وتوسيع نطاق المعالجة المتوازية (Async / Multi-threading)، مما يرفع من إنتاجية الخادم (Throughput) ويقلل من التأخير المتراكم (Latency) مقارنة بالمرور التكراري لكل سؤال على حدة (`invoke`).

</div>

---

<div dir="ltr">

## 📌 5. Technical Interview Cheat-Sheet (English Q&A)

### Q14: What is Maximal Marginal Relevance (MMR) and why is it useful in RAG?
- **Answer**:
  MMR optimizes for both **relevance** to the user query and **diversity** among the retrieved documents. It prevents returning duplicate or redundant document chunks that convey the same information in slightly different phrasing.

### Q15: How do you handle Arabic text chunking and embeddings efficiently?
- **Answer**:
  1. Ensure UTF-8 encoding across loaders (`encoding="utf-8"`).
  2. Use multilingual embedding models such as `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` or `bge-m3`.
  3. Avoid aggressive character splitters that break Arabic word roots.

### Q16: How do you manage memory window overflow when chat history grows too large?
- **Answer**:
  1. Summarization: Periodically summarize past messages using an LLM chain and inject the summary into the system prompt.
  2. Window Truncation: Retain only the last $N$ messages or tokens using message trimming utilities (`trim_messages`).

### Q17: What is the primary difference between FAISS IVF and Chroma DB HNSW indexing?
- **Answer**:
  - **FAISS IVF (Inverted File)** clusters vectors into Voronoi cells using k-means and searches only candidate centroids, reducing search scope but requiring explicit training.
  - **Chroma HNSW (hnswlib)** builds a multi-layer graph dynamically on data insertion, allowing incremental real-time indexing without separate training phases.

</div>

