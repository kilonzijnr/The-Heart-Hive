from django.core.checks import messages
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

def search_images(request):
    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        searched_images =Image.search_by_name(search_term)
        message = f'{search_term}'

        return render(request, 'search.html', {'message': message, 'images':searched_images})
    else:
        message = "Kindly Feed in a valid Input!"
        return render(request, 'search.html', {'message':message})

    
