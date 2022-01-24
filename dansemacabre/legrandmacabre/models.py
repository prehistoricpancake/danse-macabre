from django.db import models


class Artist(models.Model):
    name = models.TextField()   


    def __str__(self):
        return self.name

    
    class Meta:
        ordering = ['name']
    
    
class Category(models.Model):
    name = models.TextField()  
    

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

class Image(models.Model):
    image = models.ImageField(upload_to ='images/')
    title = models.TextField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)    
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.category
    
    @classmethod
    def my_images(cls):
        images = cls.objects.all()
        return images
    
    def delete_images(self):
        self.remove()
    
    def save_images(self):
        self.save()
    
    def search_image(category):
        pass

    def filter_by_artist(artist):
        pass

    def update_image(self, id):
        pass

    def get_image_by_id(id):
        pass
    

   
        

