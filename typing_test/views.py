import random
import time
from django.shortcuts import render
from .models import TypingText


def typing_test(request):
    if request.method == "POST":
        typed_text = request.POST['typed_text']
        original_text = request.POST['original_text']
        start_time = float(request.POST['start_time'])
        end_time = time.time()

        correct_characters = sum(1 for i, char in enumerate(typed_text) if i < len(original_text) and char == original_text[i])
        accuracy = (correct_characters / len(original_text)) * 100

        elapsed_time = end_time - start_time
        speed = round(len(typed_text) / (elapsed_time / 60))

        context = {
            'original_text': original_text,
            'typed_text': typed_text,
            'accuracy': accuracy,
            'speed': speed,
        }
        return render(request, 'typing_test/result.html', context)
    else:
        texts = TypingText.objects.all()
        text_to_type = random.choice(texts).content
        start_time = time.time()

        context = {
            'text_to_type': text_to_type,
            'start_time': start_time,
        }
        return render(request, 'typing_test/typing_test.html', context)
