from django.test import TestCase
from .models import *
# Create your tests here.

class LocationTestClass(TestCase):
    '''
    Tests for Location class.
    '''
    
    def setUp(self):
        '''
        Runs before each test.
        '''
        
        self.location = Location(id = 50, name = 'Africa')
        
        
    def test_instance(self):
        '''
        Checks if object is an instance of the Location class.
        '''
        
        self.assertTrue(isinstance(self.location, Location))
        
        
    def test_save_method(self):
        '''
        Test whether the object is saved in the database.
        '''
        
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)
        
        
    def test_update_method(self):
        '''
        Test if the object can be updated.
        '''
        self.location.save_location()
        self.location = Location.objects.filter(name = 'Africa').update(name = 'East Afric')
        self.updated_location = Location.objects.get(name = 'East Africa')
        self.assertEqual(self.updated_location.name,"East Africa")


    def test_delete_method(self):
        '''
        Test if the object can be deleted from the database.
        '''
        self.location.save_location()
        self.location = Location.objects.get(id = 50)
        self.location.delete_location()
        self.assertTrue(len(Location.objects.all()) == 0)
        
        
        
class CategoryTestClass(TestCase):
    '''
    Tests for Category class.
    '''
    
    def setUp(self):
        '''
        Runs before each test.
        '''
        
        self.category = Category(id = 50, name = 'flaga')
        
        
    def test_instance(self):
        '''
        Checks if object is an instance of the Category class.
        '''
        
        self.assertTrue(isinstance(self.category, Category))
        
      
    def test_save_method(self):
        '''
        Test whether the object is saved in the database.
        '''
        
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)
        
        
    def test_update_method(self):
        '''
        Test if the object can be updated.
        '''
        self.category.save_category()
        self.category = Category.objects.filter(name = 'flaga').update(name = 'flags')
        self.updated_category = Category.objects.get(name = 'flags')
        self.assertEqual(self.updated_category.name,"flags")


    def test_delete_method(self):
        '''
        Test if the object can be deleted from the database.
        '''
        self.category.save_category()
        self.category = Category.objects.get(id = 50)
        self.category.delete_category()
        self.assertTrue(len(Category.objects.all()) == 0)
        
        
         
class ImageTestClass(TestCase):
    '''
    Tests for Image class.
    '''
    
    def setUp(self):
        '''
        Runs before each test.
        '''
        
        self.location = Location(name = 'Africa')
        self.location.save_location()
        self.category = Category(name = 'flaga')
        self.category.save_category()
        
        self.image = Image(id = 50, image_path = 'image/location', image_name = 'Test Image', image_description = 'Testing the setUp of an image', location = self.location, category = self.category)
        
        
    def test_instance(self):
        '''
        Checks if object is an instance of the Image class.
        '''
        
        self.assertTrue(isinstance(self.image, Image))
        
    
    def test_save_image(self):
        '''
        Test whether the object is saved in the database.
        '''
        self.image.save_image()
        self.images = Image.objects.all()
        self.assertTrue(len(self.images) > 0)
        
        
    def test_update_image(self):
        '''
        Test whether the object can be updated.
        '''
        self.image.save_image()
        self.image = Image.objects.filter(id = 50).update(image_path = "new/image/location")
        self.updated_image = Image.get_image_by_id(50)
        self.assertEqual(self.updated_image.image_path,"new/image/location")
        
        
    def test_delete_image(self):
        '''
        Test case to see if the object can be deleted from the database.
        '''
        self.image.save_image()
        self.searched_image = Image.get_image_by_id(50)
        self.searched_image.delete_image()
        self.assertTrue(len(Image.objects.all()) == 0)
        
        
    def test_get_image_by_id(self):
        '''
        Test whether a specific image can be retrieved from the database using its id.
        '''
        self.image.save_image()
        self.image = Image.get_image_by_id(50)
        self.assertTrue(isinstance(self.image,Image))
        
        
    def test_search_by_category(self):
        '''
        Test whether images can be searched based on their category.
        '''
        self.image.save_image()
        self.category = Category(name = "flaga")
        self.category.save_category()
        self.searched_images = Image.search_by_category('flaga')
        self.assertTrue(len(self.searched_images) > 0)
        
        
    def test_filter_by_location(self):
        '''
        Test whether images can be filtered based on their location.
        '''
        self.image.save_image()
        self.searched_images = Image.filter_by_location('Africa')
        self.assertTrue(len(self.searched_images) > 0)