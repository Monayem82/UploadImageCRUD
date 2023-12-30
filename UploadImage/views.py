from django.shortcuts import render
from .forms import ImageStoreForm
from UploadImage.models import ImageStore
from django.http import HttpResponseRedirect

def uploadImageView(request):
    if request.method=="POST":
        frm=ImageStoreForm(request.POST,request.FILES)
        if frm.is_valid():
            frm.save()
            frm=ImageStoreForm()
    else:
        frm=ImageStoreForm()
    image=ImageStore.objects.all()
    return render(request,'uploadImage/uploadimage.html',context={"form":frm,"Images":image})

def imageDescriveView(request,image_id):
    image=ImageStore.objects.get(id=image_id)
    return render(request,'uploadImage/describeimage.html',context={"Images":image})