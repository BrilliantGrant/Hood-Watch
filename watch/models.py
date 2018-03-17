from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    username = models.CharField(max_length =30,null=True) 
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null= True)  
    neighbor_id = models.ForeignKey(Neighbor, on_delete=models.CASCADE, null= True)
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

class Neighbor(models.Model):
      neighbor_name = models.CharField(max_length=100)
      neighbor_location = models.CharField(max_length=100)
      occupy_count = models.PositiveIntegerField()
      admin = models.ForeignKey(User,on_delete=models.CASCADE)

      def __str__(self):
            return self.neighbor_name

      def create_neigbor(self):
            self.save()

      def delete_neigbor(self):
            self.delete()

      @classmethod
      def find_neigbor(cls,neigborhood_id):
            pass

      @classmethod
      def update_neighbor(cls):
        self.neighbor_name = neighbor_name
        self.neighbor_location = neighbor_location
        self.save()
    

      

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
            

    
