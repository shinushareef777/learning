from email.policy import default
from django.shortcuts import render, redirect
from .models import JobApplication, Position
from .forms import ApplicationForm
from django.contrib import messages


# home page view
def home_page(request):
    jobs = Position.objects.all().order_by("-id")
    content = {"jobs": jobs}
    return render(request, "apply_job/home.html", content)


# view for job application form
def application_page(request):
    form = ApplicationForm()
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully applied!")
            return redirect("myjobs")
    content = {"form": form}
    return render(request, "apply_job/application_form.html", content)


# view for listing applied job
def listing_page(request):
    form = JobApplication.objects.all().order_by("-date_applied")
    content = {"form": form}
    return render(request, "apply_job/listing_page.html", content)


# view for editing page
def edit_form(request, pk):
    application = JobApplication.objects.get(id=pk)
    form = ApplicationForm(instance=application)  # instance of form with filled
    if request.method == "POST":
        # filled out the form with info of that id
        form = ApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully edited your application")
            return redirect("myjobs")
    content = {"form": form}
    return render(request, "apply_job/application_form.html", content)


# view for deleting job application
def delete_form(request, pk):
    # getting saved application from the db with given id
    application = JobApplication.objects.get(id=pk)
    if request.method == "POST":
        application.delete()
        messages.success(request, "Your application has been deleted")
        return redirect("myjobs")
    # when clicking the delete button prompt user to confirm
    return render(request, "apply_job/delete.html", {"obj": application})
