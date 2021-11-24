from django.shortcuts import render
from .models import Image
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
 
def photos(request):
    """Function for Images views functionality"""
    
    categories = Image.objects.distinct().values_list('category_name', flat=True)
    locations = Image.objects.distinct().values_list('location_name', flat=True)
    try:
        images = Image.objects.all()
    except ObjectDoesNotExist:
        raise Http404
    return render(request, photos.html, {'image':images, 'categories':categories, 'locations':locations})

