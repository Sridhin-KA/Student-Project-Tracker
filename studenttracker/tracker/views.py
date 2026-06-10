from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .models import Batch
from .models import Student
from .models import Project

from .forms import BatchForm
from .forms import StudentForm


USERNAME = "admin"
PASSWORD = "123456"


def home(request):
    batches = Batch.objects.all()
    return render(
        request,
        "home.html",
        {"batches": batches}
    )


def batch_detail(request, id):
    batch = get_object_or_404(Batch, id=id)

    return render(
        request,
        "batch_detail.html",
        {"batch": batch}
    )


def student_detail(request, id):
    student = get_object_or_404(Student, id=id)

    return render(
        request,
        "student_detail.html",
        {"student": student}
    )


def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        if (
            username == USERNAME and
            password == PASSWORD
        ):
            request.session["admin"] = True
            return redirect("dashboard")

    return render(request, "login.html")


def logout_view(request):

    request.session.flush()
    return redirect("home")


def dashboard(request):
    if not request.session.get("admin"):
        return redirect("login")

    query = request.GET.get("q")

    batches = Batch.objects.all()
    students = Student.objects.all()

    if query:
        students = students.filter(name__icontains=query)

    return render(
        request,
        "dashboard.html",
        {
            "batches": batches,
            "students": students,
        }
    )

def add_batch(request):

    if not request.session.get("admin"):
        return redirect("login")

    form = BatchForm(
        request.POST or None
    )

    if form.is_valid():
        form.save()
        return redirect("dashboard")

    return render(
        request,
        "batch_form.html",
        {"form": form}
    )


def add_student(request):

    if not request.session.get("admin"):
        return redirect("login")

    form = StudentForm(
        request.POST or None
    )

    if form.is_valid():
        form.save()
        return redirect("dashboard")

    return render(
        request,
        "student_form.html",
        {"form": form}
    )


def delete_batch(request, id):

    if not request.session.get("admin"):
        return redirect("login")

    Batch.objects.get(id=id).delete()

    return redirect("dashboard")


def delete_student(request, id):

    if not request.session.get("admin"):
        return redirect("login")
def edit_batch(request, id):
    if not request.session.get("admin"):
        return redirect("login")

    batch = get_object_or_404(Batch, id=id)

    form = BatchForm(request.POST or None, instance=batch)

    if form.is_valid():
        form.save()
        return redirect("dashboard")

    return render(
        request,
        "batch_form.html",
        {"form": form}
    )


def edit_student(request, id):
    if not request.session.get("admin"):
        return redirect("login")

    student = get_object_or_404(Student, id=id)

    form = StudentForm(request.POST or None, instance=student)

    if form.is_valid():
        form.save()
        return redirect("dashboard")

    return render(
        request,
        "student_form.html",
        {"form": form}
    )
def edit_batch(request, id):
    if not request.session.get("admin"):
        return redirect("login")

    batch = get_object_or_404(Batch, id=id)

    form = BatchForm(request.POST or None, instance=batch)

    if form.is_valid():
        form.save()
        return redirect("dashboard")

    return render(
        request,
        "batch_form.html",
        {"form": form}
    )

def manage_projects(request): 
    if not request.session.get("admin"): return redirect("login")
    projects = Project.objects.select_related( "student", "student__batch" ).order_by( "student__batch__name", "student__name", "title" )
    return render( request, "manage_projects.html", { "projects": projects }, )


from .models import Project
from .forms import ProjectForm

def edit_project(request, id):
    if not request.session.get("admin"):
        return redirect("login")

    project = get_object_or_404(Project, id=id)

    form = ProjectForm(request.POST or None, instance=project)

    if form.is_valid():
        form.save()
        return redirect("manage_projects")

    return render(
        request,
        "project_form.html",
        {
            "form": form
       
    }, )


from django.shortcuts import get_object_or_404, redirect
from .models import Project

def delete_project(request, id):
    if not request.session.get("admin"):
        return redirect("login")

    project = get_object_or_404(Project, id=id)

    project.delete()

    return redirect("manage_projects")



def edit_student(request, id):
    if not request.session.get("admin"):
        return redirect("login")

    student = get_object_or_404(Student, id=id)

    form = StudentForm(request.POST or None, instance=student)

    if form.is_valid():
        form.save()
        return redirect("dashboard")

    return render(
        request,
        "student_form.html",
        {"form": form}
    )
    
from .forms import ProjectForm

def add_project(request):
    if not request.session.get("admin"):
        return redirect("login")

    form = ProjectForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("dashboard")

    return render(
        request,
        "project_form.html",
        {"form": form},
    )