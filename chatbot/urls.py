from django.urls import path
from .views import main_chatbot, api_chat
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', main_chatbot, name="main_chatbot"),
    path('api/chat/', api_chat, name="api_chat"),
]

# أضف دعم ملفات الميديا في حالة التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
