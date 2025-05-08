from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Photo
from .tasks import test_add


def index(request):
    """
    Рендерит главную страницу.
    """
    template = 'index.html'
    photos = Photo.objects.all()
    paginator = Paginator(photos, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
    }
    if request.method == "POST":
        file = request.FILES.get('file')
        if file:
            photo = Photo.objects.create(
                image_name=file.name,
                file=file,
            )
            test_add.apply_async(args=[photo.id], countdown=20)
    return render(request, template, context)
