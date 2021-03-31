from django.urls import path,include
from . import views as jobsviews

urlpatterns = [
    path('',jobsviews.home,name='home'),
    path('detail/<int:job_id>/',jobsviews.detail_view,name='detail'),
    path('post/',jobsviews.update,name='post'),    
    path('update/<int:id>/',jobsviews.update,name='update'),
    path('delete/<int:id>',jobsviews.delete_job,name='delete'),
]