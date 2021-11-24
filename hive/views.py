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
    """Function for Image searching/sourcing"""

    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        searched_images =Image.search_by_name(search_term)
        message = f'{search_term}'

        return render(request, 'search.html', {'message': message, 'images':searched_images})
    else:
        message = "Kindly Feed in a valid Input!"
        return render(request, 'search.html', {'message':message})

def  view_category(request, category):
    """Function for filtering Images according to their categories"""

    categories = Image.objects.distinct().values_list('category_name', flat=True)
    image = Image.objects.filter(category_name = category)
    return render(request, 'category.html', {"image":image, 'categories': categories})

def view_location(request, location):
    """Function for filtering Images according to their Locations"""

    locations = Image.objects.distinct().values_list('locations_name', flat= True)
    categories = Image.objects.distinct().values_list('categories_name', flat= True)
    image = Image.objects.filter(location_name= location)
    return render(request, 'category.html', {"image":image, "locations":locations, 'categories':categories})
    
