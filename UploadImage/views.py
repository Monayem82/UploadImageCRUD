from django.shortcuts import render
from .forms import ImageStoreForm
from UploadImage.models import ImageStore

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

