
import sys
import os
import datetime

# إعداد المسارات
PROJECT_PATH = "/home/zain4bot/zain_multimodal_bot"
sys.path.append(PROJECT_PATH)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zain_bot_projects.settings")

# تحميل Django
import django
django.setup()

# استدعاء التحديث
from chatbot.utils.prepare_knowledge import build_vectorstore

def run():
    log_path = os.path.join(PROJECT_PATH, "update_log.txt")
    with open(log_path, "a") as log:
        log.write("\n\n=== [🕒] تحديث جديد في: {} ===\n".format(datetime.datetime.now()))
        try:
            build_vectorstore()
            log.write("[✅] تم تحديث قاعدة المعرفة بنجاح.\n")
        except Exception as e:
            log.write("[❌] خطأ أثناء التحديث: {}\n".format(str(e)))

# تنفيذ السكربت
run()
