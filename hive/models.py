
from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.
class Image(models.Model):
    """A model class for image properties"""
    
    image = ImageField('image')
    name = models.CharField(max_length=50)
    description = models.TextField()
    location= models.ForeignKey(Location, on_delete=models.CASCADE, default=None)
    category = models.ManyToManyField(C)

    def __str__(self):
        return self.name

    def save_image(self):
        """Method to save image"""
        self.save()

    def delete_image(self):
        """Method to delete image"""
        self.delete()

    @classmethod
    def get_image_by_id(cls, id):
        """Method for sourcing an image by its id"""
        image = cls.objects.filter(id_contains = id)
        return image

    @classmethod
    def get_image_by_category(cls, category):
        """Method for sourcing image by its category"""
        image = cls.objects.filter(category_icontains=category)
        return image

    @classmethod
    def get_image_by_location(cls, location):
        """Method for sourcing an image by its location"""
        image = cls.objects.filter(location_icontains =location)
        return image

    @classmethod
    def search_by_name(cls, search_term):
        """Method for sourcing an image by its name"""
        images = cls.objects.filter(name_icontains = search_term)
        return images


class Location(models.Model):
    """A Model class for image location"""

    name = models.CharField(max_length= 50)

    def __str__(self):
        return self.name

    def save_location(self):
        """Method for saving image location"""
        self.save()

    def delete_location(self):
        """Method for deleting image location"""
        self.delete()


class Category(models.Model):
    """A model class for image category"""
    
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save_category(self):
        """Method to save image catgory"""
        self.save()

    def delete_category(self):
        """Method to delete image category"""
        self.delete()


    



    