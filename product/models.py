from django.db import models
from django.core.files import File
from io import BytesIO
from PIL import Image
# slug is a short label for something, containing only letters, numbers, underscores or hyphens. It's generally used in URLs. This field adds a slug automatically when the name is added.

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    
    # Meta class is used to define the order of the objects, in this case, by name
    class Meta:
        ordering = ('name',)
        

    def __str__(self):
        return self.name
    
    # get_absolute_url is used to get the url of the object
    def get_absolute_url(self):
        return f'/{self.slug}/'
    
class Product(models.Model):
    category= models.ForeignKey(Category,related_name="products" ,on_delete=models.CASCADE)
    name= models.CharField(max_length=200)
    slug= models.SlugField(max_length=200, unique=True)
    description= models.TextField(blank=True,null=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image= models.ImageField(upload_to='uploads/',blank=True,null=True)
    thumbnail= models.ImageField(upload_to='uploads/',blank=True,null=True)
    date_added= models.DateTimeField(auto_now_add=True)
# Meta class is used to define the order of the objects, in this case,by date added "-date_added" means descending order newest first
    class Meta:
        ordering = ('-date_added',)
        

    def __str__(self):
        return self.name
    
    # get_absolute_url is used to get the url of the object
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ""
    def make_thumbnail(self,image, size=(300,200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        thumbnail = File(thumb_io, name=image.name)
        return thumbnail