from django.contrib import admin
from django.urls import path,include
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/' , include('blog.urls')), 
    path('liberal/', include('blog.urls')), 
    path('exter_act/', include('blog.urls')), 
    path('inter_act/', include('blog.urls')), 
    path('site/', include('blog.urls')), 
    path('', include('account.urls')),
]
