"""myanalyzer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from myanalyzer.views import hello, current_datetime,hours_ahead,checkposneg
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

print("URL class")
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello$', hello),
    url(r'^datetime/plus/(\d{1,2})$', hours_ahead),
    url(r'^datetime$', current_datetime),
    url(r'^analyzedata$',checkposneg),
    url(r'^', TemplateView.as_view(template_name="index.html")),
]
