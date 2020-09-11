from django.shortcuts import render
from .models import Album


def album_data(request):
    data = Album.objects.select_related('artist').all()
    return render(request, "datasets/albums.html", {'data': data})
