"""OmahPortfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from portfolio import views as portfolioView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', portfolioView.home_view,name='home'),
    path('about/', portfolioView.about_view,name='about'),
    path('portfolio-details/', portfolioView.portfolio_detail_view,name='portfolioDetail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Omah Portfolio Portal"
admin.site.site_title = "Omah Portfolio Portal Administration"
admin.site.index_title = "Welcome To Omah Portfolio Portal Administration"