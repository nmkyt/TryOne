import random
import time

from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect

from .forms import TextForm
from .models import TypingText


def typing_test(request):
    if request.method == "POST":
        incorrect_characters = request.POST['incorrect_characters']
        original_text = request.POST['original_text']
        start_time = float(request.POST['start_time'])
        end_time = time.time()

        accuracy = 100 - (int(incorrect_characters) / len(original_text)) * 100

        elapsed_time = end_time - start_time
        speed = round(len(original_text) / (elapsed_time / 60))

        context = {
            'original_text': original_text,
            'accuracy': round(accuracy),
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


@login_required
@permission_required('typing_test.add_text', raise_exception=True)
def add_text(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('typing_test')
    else:
        form = TextForm()
    return render(request, 'typing_test/add_text.html', {'form': form})
