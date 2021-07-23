from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.blog , name="blog"),
    path('<int:blog_id>', views.detail, name="detail"),
    path('liberal', views.liberal, name="liberal"), #
    path('exter_act', views.exter_act, name="exter_act"), #
    path('inter_act', views.inter_act, name="inter_act"), #
    path('site', views.site, name="site"), #
    path('new', views.new, name="new"),
    path('new_liberal', views.new_liberal, name="new_liberal"), #
    path('new_exter_act', views.new_exter_act, name="new_exter_act"), #
    path('new_inter_act', views.new_inter_act, name="new_inter_act"), #
    path('new_site', views.new_site, name="new_site"), #
    path('create', views.create, name='create'),
    path('delete/<int:blog_id>', views.delete, name='delete'),
    path('delete_site/<int:site_id>', views.delete_site, name='delete_site'),  #
    path('update/<int:blog_id>', views.update, name='update'),
    # path('update_liberal/<int:blog_id>', views.update_liberal, name='update_liberal'),  #
    # Comment
    path('comment/<int:blog_id>', views.comment, name='comment'),
    path('comment/delete/<int:comment_id>', views.comment_delete, name="comment_delete"),
    # Like
    path('like/<int:blog_id>', views.post_like, name="post_like"),

    path('create_liberal', views.create_liberal, name="create_liberal"), #
    path('create_exter', views.create_exter, name="create_exter"), #
    path('create_inter', views.create_inter, name="create_inter"), #
    path('create_site', views.create_site, name="create_site"), #
]

