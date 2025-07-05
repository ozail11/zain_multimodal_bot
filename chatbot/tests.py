from django.test import TestCase

# Create your tests here.
import openai

openai.api_key = "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"  # ضع مفتاحك هنا

try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "مرحبا"}],
        max_tokens=50,
    )
    print(response.choices[0].message.content)
except Exception as e:
    print("OpenAI API Error:", e)