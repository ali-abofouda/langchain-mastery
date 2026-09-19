<div dir="rtl">

# 📖 الفصل الخامس: معمارية المشاريع العملية والأنظمة الحقيقية (Real-World Systems)

يشرح هذا الفصل الهيكلية الهندسية لبناء تطبيقات الذكاء الاصطناعي والتوليد الإنتاجية ومبادئ التصميم الهندسي للمشاريع الحقيقية.

---

## 📌 1. معمارية تطبيق Football RAG Application

يقوم مشروع **Football RAG** على خط أنابيب متكامل من 5 مراحل أساسية:

```text
[Web Scraping] -> [Text Chunking] -> [HuggingFace Embeddings] -> [FAISS Index] -> [Groq LLM Chain] -> [Streamlit / CLI UI]
```

### التكتيكات البرمجية الهامة:
1. **منع الهلوسة (Anti-Hallucination Guardrails)**:
   صياغة التوجيه لفرض إجابة النموذج فقط من السياق الموفر، والتنصيص الصريح بعبارة "لا أعلم" عند غياب المعلومة.
2. **الرد بنفس اللغة (Multilingual Context Handling)**:
   تعليم النموذج اكتشاف لغة الاستعلام تلقائياً والرد بنفس اللغة سواء كانت عربية أو إنجليزية.
3. **عرض المصادر المرجعية (Source Attribution)**:
   استخراج البيانات الوصفية `metadata['source']` وعرضها للمستخدم لتعزيز الموثوقية الشفافة.

---

## 📌 2. معمارية النشر والتطوير للمشاريع

1. **فصل المنطق عن الواجهة (Decoupled Architecture)**:
   - فصل منطق RAG وسلاسل LCEL في خدمات مستقلة (REST API) باستخدام LangServe.
   - جعل واجهات المستخدم (Web App أو Mobile App) تستهلك الـ Endpoints بشكل آمن.
2. **المرونة بين السحابي والمحلي (Hybrid LLM Strategy)**:
   - استخدام نماذج سريعة سحابياً (مثل `ChatGroq`) للسرعة في الإجابات العامة.
   - استخدام النماذج المحلية (`Ollama`) للبيانات الحساسة أو عند انقطاع الاتصال.

---

## 📌 3. معمارية تطبيق مساعد Web RAG Assistant (`projects/05_web_rag_assistant`)

تعتمد المعمارية الهندسية لمساعد الـ Web RAG على معالجة البيانات غير المهيكلة المستخرجة حياً من الويب:

```text
[Web URL] 🌐 
    ↓ (WebBaseLoader)
[HTML Content Extraction & Cleaning]
    ↓ (RecursiveCharacterTextSplitter: 1000/200)
[Chunks Stream]
    ↓ (HuggingFaceEmbeddings: all-MiniLM-L6-v2)
[Dense Vector Embeddings]
    ↓ (Chroma DB Indexing - HNSW Graph)
[Chroma Retriever (k=3)] 
    ↓ (LCEL Pipeline: context | prompt | ChatGroq)
[Grounded Answer + UI Streamlit Dark Mode / CLI]
```

### التكتيكات المعمارية:
- **التخزين المؤقت للنماذج (`@st.cache_resource`)**: تحسين سرعة إقلاع الواجهة وعدم إعادة تحميل نموذج التضمين مع كل إعادة رسم للصفحة.
- **إعادة التأطير السياقي (Context Re-grounding)**: الحفاظ على السياق الأكاديمي والتقني بدقة من خلال القوالب الموجهة (Strict Prompts).

</div>

