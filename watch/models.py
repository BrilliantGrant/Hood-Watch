from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import IntegrityError

class Neighborhood(models.Model):
      neighborhood_name = models.CharField(max_length=100)
      neighborhood_location = models.CharField(max_length=100)
      occupy_count = models.PositiveIntegerField()
      admin = models.ForeignKey(User,on_delete=models.CASCADE)

      def __str__(self):
            return self.neighborhood_name

      def create_neigborhood(self):
            self.save()

      def delete_neigborhood(self):
            self.delete()

      @classmethod
      def find_neighborhood(cls,neighborhood_id):
        found_neighborhood = cls.objects.get(id = neighborhood_id)
        return found_neighborhood


      @classmethod
      def update_neighborhood(cls):
        self.neighborhood_name = neighborhood_name
        self.neighborhood_location = neighborhood_location
        self.save()
    
class Profile(models.Model):
    name = models.CharField(max_length =30,null=True) 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null= True)  
    neighborhood_id = models.ForeignKey(Neighborhood,null=True, on_delete=models.CASCADE)
    email = models.EmailField(null=True)
    

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.name

    @classmethod
    def find_profile_by_id(cls,user_id):
        profile = cls.objects.get(user_id = user_id)
        return profile
      

class Business(models.Model):
      business_name = models.CharField(max_length=100)
      user = models.ForeignKey(User)
      neighborhood_id = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
      business_email = models.CharField(max_length=100)

      def __str__(self):
            return self.business_name

      def create_business(self):
            self.save()

      def delete_business(self):
            self.delete()

      @classmethod
      def find_business(cls,business_id):
         got_business = cls.objects.get(id= business_id)
         return got_business
           

      @classmethod
      def update_business(cls):
        self.business_name = business_name
        self.business_email = business_email
        self.save() 
            

class Post(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE,default=1)
    post = models.TextField(max_length=100)
    image = models.ImageField(upload_to='posts/',null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True,null= True)


    def __str__(self):
      return self.post

     