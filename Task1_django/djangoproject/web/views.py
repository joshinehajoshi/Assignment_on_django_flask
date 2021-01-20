from django.shortcuts import render, redirect
from web.forms import StudentsForm
from web.models import Students



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
    students = Students.objects.get(id=id)
    return render(request,"edit.html",{'students': students})

def update(request, id):
    students = Students.objects.get(id=id)
    form = StudentsForm(request.POST, instance = students)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request,"edit.html",{'students': students})
    


def delete(request, id):
    students = Students.objects.get(id=id)
    students.delete()
    return redirect('/show')