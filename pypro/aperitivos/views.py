from django.db import models
from django.shortcuts import render
from django.urls import reverse


class Video(models.Model):
    slug = models.CharField(max_length=32)
    titulo = models.CharField(max_length=32)
    vimeo_id = models.CharField(max_length=32)

    def get_absolute_url(self):
        return reverse('aperitivos:video', args=(self.slug,))

videos = [
    Video(slug='motivacao', titulo='Video Aperitivo: Motivação',  vimeo_id='682944764'),
    Video(slug='instalacao-windows', titulo='Instalação Windows', vimeo_id='682947239'),
]

videos_dct = {v.slug: v for v in videos}

def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})

class Video:
    def __init__(self, slug, titulo, vimeo_id):
        self.slug = slug
        self.titulo = titulo
        self.vimeo_id = vimeo_id


videos = [
    Video('motivacao', 'Video Aperitivo: Motivação',  682944764),
    Video('instalacao-windows', 'Instalação Windows', 682947239),
]

videos_dct = {v.slug: v for v in videos}

def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})

def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
