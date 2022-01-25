from django.test import TestCase
from .models import Category, Image

# Create your tests here.


class ImageTestClass(TestCase):
    def setUp(self):
        self.images = Image(image="image", title="name", description="describe")

    # Testign instance
    def test_instance(self):
        self.assertTrue(isinstance(self.images, Image))


# Testing save Method
def test_save_method(self):
    self.images.save_images()
    image = Image.objects.all()
    self.assertTrue(len(image) > 0)
