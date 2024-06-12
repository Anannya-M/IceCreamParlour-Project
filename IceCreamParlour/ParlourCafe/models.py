from django.db import models

# Create your models here.

class FlavourModel(models.Model):
    flavour_id = models.IntegerField(unique=True)
    flavour_name = models.CharField(max_length=100)
    seasonal = models.BooleanField(default=False)
    ingredients = models.TextField()


    def __str__(self):
        return f'{self.flavour_name} {self.seasonal}'

    class Meta:
        ordering = ['seasonal']


class IngredientModel(models.Model):
    ingredient_name = models.CharField(max_length=100)
    amount_in_stock = models.IntegerField()

    def __str__(self):
        return self.ingredient_name

    class Meta:
        ordering=['-amount_in_stock']


class AllergyModel(models.Model):
    allergy_name = models.CharField(max_length=150)

    def __str__(self):
        return self.allergy_name

class FlavourSuggestionModel(models.Model):
    user_name = models.CharField(max_length=150)
    email = models.EmailField()
    flavour = models.CharField(max_length=100)
    allergy = models.ManyToManyField('AllergyModel', blank=True)
    suggestion = models.TextField()

    def __str__(self):
        return self.suggestion

class CartModel(models.Model):
    fav_products = models.ForeignKey(FlavourModel, on_delete=models.CASCADE)


class UserDb(models.Model):
    email_address = models.EmailField(unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.email_address} {self.password}'
