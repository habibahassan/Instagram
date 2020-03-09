from django.contrib.auth.models import User
from .models import Profile
from django.test import TestCase
from .models import Image,Like,Comment

class Intagram_TestCases(TestCase):
    def setUp(self):
        self.user1= User(id=1,username='dev',email='dev12@gmail.com',password='1234')
        self.user1.save()
        self.profile = Profile(user_id=1,bio='amazing',profile_pic='images/travel.jpg')
        self.profile.save_profile()
        self.my_image = Image(id=1,caption='traveling is good', owner=self.user1,profile=self.profile,image='media/get.jpg',image_name='giraff')
        self.my_image.save_image()

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()
        Image.objects.all().delete()

    def test_is_instance(self):
        self.assertTrue(isinstance(self.user1,User))
        self.assertTrue(isinstance(self.profile,Profile))
        self.assertTrue(isinstance(self.my_image,Image))

    def test_save_method(self):
        self.my_image.save_image()
        all_objects = Image.objects.all()
        self.assertTrue(len(all_objects)>0)

    def test_delete_method(self):
        self.my_image.save_image()
        object = Image.objects.filter(id=1)
        Image.delete_image(object)
        all_objects = Image.objects.all()
        self.assertTrue(len(all_objects) == 0)


    def test_get_image_by_id(self):
        self.my_image.save_image()
        image = Image.get_image_by_id(1)
        self.assertEqual(image.id,1)


    def test_update_single_image(self):
        self.my_image.save_image()
        filtered_object =Image.update_image('giraff','life')
        updated = Image.objects.get(image_name='life')
        self.assertEqual(updated.image_name,'life')