from django.conf.urls import url
from django.urls import path
from .views import kesifEkle,kesifGoster,kesifDetay,kesifSilme,kesifGuncelle,export_xls






urlpatterns = [
   # path('',LoginView.as_view(),name="home"),
    path('',kesifGoster,name='GosterUrl'),
    path('detay/<id>',kesifDetay,name='DetayUrl'),
    path('ekle/',kesifEkle,name='EkleUrl'),
    path('<id>/sil/',kesifSilme,name='SilUrl'),
    path('<id>/guncelle/',kesifGuncelle,name='GuncelleUrl'),
    url(r'^xls/$', export_xls, name='export_xls'),


]
