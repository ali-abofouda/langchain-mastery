<div dir="rtl">

# 📖 الفصل الرابع: سلاسل LCEL والنشر والنماذج المحلية (LCEL, Deployment & Local LLMs)

تمثل **لغة تعبير لانج تشين (LangChain Expression Language - LCEL)** المعمارية الحديثة لبناء وتنسيق التدفقات المعقدة في مشاريع الذكاء الاصطناعي والتوليد.

---

## 📌 1. فلسفة LCEL وعامل الربط Pipe (`|`)

### ما هي LCEL؟
LCEL هي طريقة 선언적 (Declarative) تسمح بربط المكونات المستقلة (Prompts, Models, Output Parsers, Retrievers) بسلسلة واحدة عبر عامل الربط Pipe `|`.

```python
chain = prompt | model | output_parser
```

### المكونات الأساسية في LCEL (`Runnables`):
- **`RunnablePassthrough`**: يمرر البيانات كما هي دون تعديل داخل السلسلة.
- **`RunnableParallel`**: ينفذ عمليات متعددة بالتوازي (مثل استرجاع المستندات وتنسيق التوجيه في نفس الوقت).
- **`StrOutputParser`**: يستخرج النص النظيف المباشر من مخرجات كائنات `AIMessage`.

---

## 📌 2. المخرجات المهيكلة عبر Pydantic (`with_structured_output`)

تتطلب الأنظمة الإنتاجية إجابات ذات بنية برمجية محددة بدلاً من النص الحر.

### الخطوات:
1. تعريف سكيما البيانات باستخدام مكتبة `Pydantic`:
   ```python
   class ExtractionSchema(BaseModel):
       summary: str = Field(description="ملخص الإجابة")
       sources: list[str] = Field(description="قائمة المصادر")
   ```
2. ربط السكيما بالنموذج:
   ```python
   structured_llm = llm.with_structured_output(ExtractionSchema)
   ```

---

## 📌 3. النشر كـ REST API عبر LangServe و FastAPI

تتيح مكتبة **LangServe** تحويل أي سلسلة LCEL إلى خادم شبكي دون الحاجة لكتابة كود FastAPI معقد.

### المميزات التلقائية في LangServe:
- توفير مسارات متطورة: `/invoke`, `/stream`, `/batch`.
- بناء واجهة تجريبية تفاعلية سريعة على `/playground`.
- توليد توثيق Swagger تلقائي.

---

## 📌 4. التشغيل المحلي (Ollama) والتتبع (LangSmith)

### 1️⃣ التشغيل المحلي بـ Ollama:
- يتيح تشغيل نماذج مثل `Qwen 3` أو `Llama 3` محلياً عبر منفذ `11434`.
- يضمن الخصوصية التامة والتكلفة الصفريّة للاستهلاك.

### 2️⃣ التتبع بـ LangSmith:
- بمجرد ضبط `LANGSMITH_TRACING="true"` ومفتاح الـ API، يمكنك رؤية الشجرة الكاملة لتنفيذ السلسلة، زمن الاستجابة، ونصوص التوجيه الدقيقة.

</div>
