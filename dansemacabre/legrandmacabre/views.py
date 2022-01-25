from django.shortcuts import render
from django.http import Http404
from .models import Image
from .filters import ImageFilter


def home(request):

    images = Image.objects.all()

    return render(request, "home.html", {"images": images})


def images(request, image_id):
    try:
        images = Image.objects.get(id=image_id)
    except Image.DoesNotExist:
        raise Http404()

    return render(request, "images.html", {"images": images})


def search(request):
    image_list = Image.objects.all()
    image_filter = ImageFilter(request.GET, queryset=image_list)
    return render(request, "searchfilter.html", {"filter": image_filter})
