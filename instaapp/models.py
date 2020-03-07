from django.db import models

# Create your models here.

class Profile(models.Model):
    bio = models.CharField(max_length =200)
    profile_pic = models.ImageField(upload_to = 'photos/', default='DEFAULT VALUE')
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    followers = models.ManyToManyField('Profile',related_name="profile_followers",blank=True,default=0)
    following = models.ManyToManyField('Profile',related_name="profile_following",blank=True,default=0)
    def __str__(self):
        return self.user
    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()
    @classmethod
    def search_profile(cls,search_term):
        profiles = cls.objects.filter(user__icontains=search_term)
        return profiles
