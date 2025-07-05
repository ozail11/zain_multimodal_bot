import difflib
from .knowledge_base import knowledge_items

def rag_response(user_query):
    # البحث عن أقرب سؤال مطابق
    questions = [item["question"] for item in knowledge_items]
    closest = difflib.get_close_matches(user_query, questions, n=1, cutoff=0.4)

    if closest:
        for item in knowledge_items:
            if item["question"] == closest[0]:
                return item["answer"]
    
    return "لم أجد معلومة متعلقة بسؤالك في قاعدة المعرفة."
