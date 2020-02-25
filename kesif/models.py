from django.utils import timezone

from django.db import models

# Create your models here.



class kesif(models.Model):
 kesifNo=models.CharField(max_length=120, verbose_name='Kesif No')
 tarih=models.DateField(default=timezone.now(),blank=False, null=True,verbose_name='Tarih')
 musteri=models.CharField(max_length=250,verbose_name='Musteri')
 ilgiliKisi=models.CharField(max_length=100,verbose_name='İlgili Kisi')
 tel=models.CharField(max_length=12,verbose_name='Telefon')
 adres=models.TextField(verbose_name='Adres')
 aciklama=models.TextField(verbose_name='Aciklama')


 def __str__(self):
  return self.kesifNo

 def get_absolute_url(self):
  return "/kesif/detay/{}".format(self.id)
