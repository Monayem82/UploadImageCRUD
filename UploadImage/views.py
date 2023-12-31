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

def imageDelete(request,image_id):
    del_image=ImageStore.objects.get(id=image_id)
    del_image.delete()
    return HttpResponseRedirect('/upload/image/')

def imageUpdateView(request,image_id):
    update_image=ImageStore.objects.get(id=image_id)
    if request.method=="POST":
        data=request.POST
        files=request.FILES
        img_name=data.get('image_name')
        img_file=files.get('image')
        update_image.image_name=img_name
        update_image.image=img_file

        each=int(image_id.isdigit())

        update_image.save()

        print(each)
        return HttpResponseRedirect('/upload/image/')
    else:
        update_image=ImageStore.objects.get(id=image_id)

    return render(request,'uploadImage/updateImage.html',context={"update_image":update_image})