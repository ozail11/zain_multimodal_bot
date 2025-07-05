import os
import difflib

def load_knowledge_base():
    base_file = os.path.join(os.path.dirname(__file__), 'knowledge.txt')
    if not os.path.exists(base_file):
        return []
    try:
        with open(base_file, encoding='utf8') as f:
            return [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"خطأ أثناء تحميل knowledge.txt: {e}")
        return []

def rag_response(user_input):
    docs = load_knowledge_base()
    if not docs:
        return "حدث خطأ: تعذر تحميل قاعدة المعرفة."
    # استخدم difflib لحساب التشابه
    matches = difflib.get_close_matches(user_input, docs, n=3, cutoff=0.4)
    if not matches:
        return "لم أجد معلومة متعلقة بسؤالك في قاعدة المعرفة."
    return "\n".join(matches)