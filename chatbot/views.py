from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.http import JsonResponse
from .utils.whisper_transcribe import transcribe_audio
from .utils.ocr import extract_text_from_image
import json 
from .utils.rag import rag_response
from .models import Message
from django.shortcuts import render

def main_chatbot(request):
    return render(request, "chatbot/index.html")

def save_user_message(sender, media_type, content=None, media_file=None):
    Message.objects.create(
        sender=sender,
        media_type=media_type,
        content=content,
        media_file=media_file
    )

@method_decorator(csrf_exempt, name='dispatch')
class ChatAPIView(View):
    def post(self, request):
        try:
            # بيانات من form-data (multipart) مع ملفات
            message = request.POST.get("message", "")
            image = request.FILES.get("image")
            audio = request.FILES.get("audio")

            media_type = "text"
            final_input = message

            if audio:
                # تأكد من أن transcribe_audio يقبل FileField أو مسار صحيح
                transcribed = transcribe_audio(audio)
                final_input += " " + transcribed
                media_type = "audio"

            if image:
                extracted = extract_text_from_image(image)
                final_input += " " + extracted
                media_type = "image"

            save_user_message(sender="user", media_type=media_type, content=final_input, media_file=audio or image)

            bot_reply = rag_response(final_input)

            save_user_message(sender="bot", media_type="text", content=bot_reply)

            return JsonResponse({"reply": bot_reply})
        except Exception as e:
            return JsonResponse({"reply": f"حدث خطأ: {str(e)}"})

@csrf_exempt
def api_chat(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode())
            user_msg = data.get("message", "")

            save_user_message(sender="user", media_type="text", content=user_msg)

            bot_reply = rag_response(user_msg)

            save_user_message(sender="bot", media_type="text", content=bot_reply)

            return JsonResponse({"reply": bot_reply})
        except Exception as e:
            return JsonResponse({"reply": f"حدث خطأ: {str(e)}"})
    return JsonResponse({"reply": "فقط طلبات POST مسموحة."})
