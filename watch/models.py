from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model)
    username = models.CharField(max_length =30,null=True) 
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null= True)  
    neighborhood_id = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null= True)
    email = models.EmailField(null=True)

    def save profile(self):
        self.save()

    def delete profile(self):
        self.delete()

    def __str__(self):
        return self.name

    @classmethod
    def find_profile_by_id(cls,user_id):
        profile = cls.objects.get(user_id = user_id)
        return profile

    
