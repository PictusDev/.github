
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from pictususer.models import Profile


# Create your models here.


class Hashtag(models.Model):
    hashtag=models.CharField(max_length=100)

    def __str__(self):
        return self.hashtag

class Post(models.Model):

    Camera_Choice=(
        ('1','Nikon FM2'), ('2','Canon AE-1'),('3','Leica M3'),('4','Pentax Me Super'),('5','Minolta X-300'),
        ('6','Minolta X-700'),('7','Ricoh ff-9d'),('8','Contax T3'),('9','Samsung Kenox M70 super '),
        ('10','olympus mju 2'),('11','Canon autoboy tele'),('12','Canon autoboy luna 35'),('13','Canon autoboy 3'),
        ('14','Canon autoboy 2'),('15','Fuji Klasse W'),('16','Lomo LC-A'),('17','Olympus Pen EE-2'),
        ('18','Yashica Electro 35'),('19','Contax G1'),('20','Konica C35'),('21','Toma m 616')
    )

    Film_Choice=(
        ('1','Kodak colorplus 200'),('2','Kodak gold 200'),('3','Kodak proimage 100'),('4','Kodak ultramax 400'),
        ('5','Kodak ektar 100'),('6','Kodak portra 160'),('7','Fujicolor 100'),('8','Fuji Superia X-TRA 400'),
        ('9','Fujifilm Superia Premium 400'),('10','Fujifilm C200'),('11','Lomography color negative 100'),
        ('12','Lomography color negative 400'),('13','Lomography color negative 800'),('14','Kodak Portra 800'),
        ('15','Kodak Portra 400'),('16','Lomography lomochrome purple xr100_400*'),('17','Kodak Ektachrome E100 '),
        ('18','Fujifilm Velvia 100'),('19','Fujifilm Provia 100F'),('20','Kentmere Pan 400'),('21','Fomapan R100')
    )

    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    image=models.ImageField(null=False, upload_to='pictus_photo')
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    content=models.TextField(null=False)
    created_at=models.DateTimeField(auto_now_add=True)
    film=models.CharField(max_length=2, choices=Film_Choice)
    camera=models.CharField(max_length=2, choices=Camera_Choice)
    like=models.ManyToManyField(User, related_name='liked_posts', blank=True)
    # hashtag=models.ManyToManyField(Hashtag, blank=True)

    def __str__(self):
        return self.image

class Comment(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    content=models.TextField(null=False)


class Scrap(models.Model):
    title=models.CharField(max_length=100, unique=True)
    post=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)


    
