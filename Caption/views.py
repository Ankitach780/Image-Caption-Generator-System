from django.shortcuts import render
from .forms import ImageUploadForm
from .models import CaptionHistory
from .caption_generator import generate_caption
from collections import defaultdict
from datetime import datetime

def index(request):
    caption = None
    image_url = None
    history_grouped = {}

    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)

            if request.user.is_authenticated:
                obj.user = request.user
            else:
                obj.user = None

            obj.save()

            image_path = obj.image.path

            try:
                caption_words = generate_caption(image_path)
                if caption_words:
                    caption_text = ' '.join(caption_words).capitalize() + '.'
                    obj.caption = caption_text
                else:
                    obj.caption = "Caption generation failed"
                obj.save()
                caption = obj.caption
                image_url = obj.image.url
            except Exception as e:
                obj.caption = f"Error generating caption: {e}"
                obj.save()

            # Grouped history only if user is authenticated
            if request.user.is_authenticated:
                history = CaptionHistory.objects.filter(user=request.user).order_by('-created_at')[:10]
            else:
                history = []

            history_grouped = defaultdict(list)
            for entry in history:
                date_str = entry.created_at.strftime("%d %B %Y")
                history_grouped[date_str].append(entry)

            return render(request, 'index.html', {
                'form': form,
                'caption': caption,
                'image_url': image_url,
                'history_grouped': dict(history_grouped)
            })

    else:
        form = ImageUploadForm()

    # GET request: Load form and history
    if request.user.is_authenticated:
        history = CaptionHistory.objects.filter(user=request.user).order_by('-created_at')[:10]
    else:
        history = []

    history_grouped = defaultdict(list)
    for entry in history:
        date_str = entry.created_at.strftime("%d %B %Y")
        history_grouped[date_str].append(entry)

    return render(request, 'index.html', {
        'form': form,
        'caption': None,
        'image_url': None,
        'history_grouped': dict(history_grouped)
    })
