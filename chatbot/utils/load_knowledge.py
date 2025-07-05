import os
import sys
import django

# تحديد المسار الجذري للمشروع وإضافته إلى sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)

# تعيين إعدادات Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zain_bot_projects.settings')

# تهيئة بيئة Django
django.setup()

from chatbot.models import KnowledgeItem
from chatbot.knowledge_base import knowledge_items

def load_knowledge():
    for item in knowledge_items:
        KnowledgeItem.objects.update_or_create(
            question=item['question'],
            defaults={"answer": item['answer']}
        )
        print(f"✅ تم تحميل السؤال: {item['question']}")

if __name__ == "__main__":
    load_knowledge()
