from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from .models import kesif
from .forms import KesifForm
import xlwt
# Create your views here.


def kesifEkle(request):


    # if request.method=='POST':
    #     form=KesifForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    # else:
    #     form=KesifForm()

    form=KesifForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('GosterUrl'))
    context={
        'Kesif_Ekle':form
    }

    return render(request,template_name='kesif/kesifekle.html',context=context)



def kesifGoster(request):

    kesifAll=kesif.objects.all()

    context={
        'kesifAll':kesifAll
    }
    return render(request,template_name='kesif/liste.html',context=context)

def kesifDetay(request,id):

    kesif1=get_object_or_404(kesif ,id=id  )
    context={
        'kesif':kesif1
    }



    return render(request,template_name="kesif/detay.html",context=context)

def kesifGuncelle(request,id):
    kesifGuccelle=get_object_or_404(kesif, id=id )

    form=KesifForm(request.POST or None, instance=kesifGuccelle)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('GosterUrl'))

    context={
        'Kesif_Ekle':form
    }

    return render(request,template_name='kesif/kesifekle.html',context=context)

def kesifSilme(request ,id):
    kesifSil=get_object_or_404(kesif, id=id)
    kesifSil.delete()

    return HttpResponseRedirect(reverse('GosterUrl'))



def export_csv(request):
  response = HttpResponse(content_type='text/csv')
  response['Content-Disposition'] = 'attachment; filename="kesifdataAll.csv"'
  writer = csv.writer(response)
  writer.writerow(['kesifNo', 'tarih', 'musteri', 'ilgiliKisi','tel','adres','aciklama'])
  kesifall = kesif.objects.all().values_list('kesifNo', 'tarih', 'musteri', 'ilgiliKisi','tel','adres','aciklama')

  for kesifs in kesifall:
      writer.writerow(kesifs)

  return response




def export_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="KesifsAll.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Kesifs')

    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['kesifNo', 'tarih', 'musteri', 'ilgiliKisi','tel','adres','aciklama', ]
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    rows = kesif.objects.all().values_list('kesifNo', 'tarih',   'musteri', 'ilgiliKisi','tel','adres','aciklama')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response



