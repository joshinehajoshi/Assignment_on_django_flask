from django.shortcuts import render, redirect
from webapp.forms import StudentsForm
from webapp.models import Students



def stu(request):
    if request.method == "POST":
        form = StudentsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form = StudentsForm()
    return render(request, "index.html", {'form':form})


def show(request):
    studentvar = Students.objects.all()
    return render(request,"show.html",{'studentvar': studentvar})

def edit(request, id):
    studentedit = Students.objects.get(id=id)
    return render(request,"edit.html",{'studentedit': studentedit})

def update(request, id):
    studentedit = Students.objects.get(id=id)
    form = StudentsForm(request.POST, instance = studentedit)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request,"edit.html",{'studentedit': studentedit})
    


def delete(request, id):
    studentedit = StudentsForm.objects.get(id=id)
    studentedit.delete()
    return redirect('/show')