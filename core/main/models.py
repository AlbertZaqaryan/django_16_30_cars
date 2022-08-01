from django.db import models

# Create your models here.
class Home(models.Model):
    name = models.CharField('Home page name', max_length=50)
    img = models.ImageField('Home page image', upload_to='media')

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField('Car name', max_length=30)
    about = models.TextField('Car about')
    img = models.ImageField('Car image', upload_to='media')
    price = models.IntegerField('Car price')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'


class About(models.Model):
    text = models.TextField('Page about')

    def __str__(self):
        return self.text