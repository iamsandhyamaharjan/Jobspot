"""
URL configuration for jobboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.auth.views import LogoutView
from users.views import(
    UserLoginView,
    signup_view,
    contactus,
    )


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include("jobs.urls", namespace="jobs")),
    # path('employer/', include("employer.urls", namespace="employer")),
    # path('users/', include("users.urls", namespace="user")),
    path('login/',UserLoginView, name='login'),
    # path("logout/", LogoutView.as_view(), name="logout"),
    # path("contact/", contactus, name="contact"),
    # path('register/', signup_view, name='register'),
  

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Job Board Admin"
admin.site.site_title = "Job Board Admin"
