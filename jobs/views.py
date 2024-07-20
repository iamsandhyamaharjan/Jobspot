from django.shortcuts import render

# Create your views here.

def homepage(request):
    # applications = Application.objects.all().count()
    # print(applications)
    # jobs = Job.objects.order_by("-created_at")[:6]
    # return render(request, "index.html", {"jobs": jobs, "applications": applications})
    return render(request, "index.html")
