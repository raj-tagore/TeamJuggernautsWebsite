from django.shortcuts import render
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static/')]

# Create your views here.
def HomePg(request):
	return render(request, 'index.html', {'filearr' : os.listdir(os.path.join(BASE_DIR, 'static/images/HomePgGallery/'))})

def AboutPg(request):
	return render(request, 'about.html', {'filearr' : os.listdir(os.path.join(BASE_DIR, 'static/images/AboutPg/Members2020/'))})

def GalleryPg(request):
	return render(request, 'gallery.html', {'filearr' : os.listdir(os.path.join(BASE_DIR, 'static/images/GKDC2020/')),
											'filearr2' : os.listdir(os.path.join(BASE_DIR, 'static/images/IGKC2019/'))})
