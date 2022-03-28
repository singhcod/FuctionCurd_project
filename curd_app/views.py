from django.shortcuts import render,HttpResponse,redirect
from.forms import StudentRegistration
from.models import User


# Create your views here.
def add_show(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
             name = form.cleaned_data['name']
             email = form.cleaned_data['email']
             password = form.cleaned_data['password']
             fm = User(name=name,email = email,password = password)
             fm.save()
        else:
            return HttpResponse("invalid form data")
    else:
        form = StudentRegistration()
        stdu = User.objects.all()
    return render(request,'addandshow.html',{'form':form,'stdu':stdu},)


#function will update and edit

def update_data(request,id):
    if request.method == "POST":
        pi = User.objects.get(pk = id)
        form = StudentRegistration(request.POST,instance=pi)
        if form.is_valid():
            form.save()
    else:
        pi = User.objects.get(pk=id)
        form = StudentRegistration(instance=pi)

    return render(request,'update.html',{'form':form})



# view for delete
def delete_data(request,id):
   # if request.method == 'POST':
        student = User.objects.get(pk=id)
        student.delete()
        return redirect('/')


