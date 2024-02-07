from django.urls import path
from . import views

urlpatterns = [
    path('',views.User_register,name='index'),
    path('delete/<int:pk>',views.user_delete,name='delete'),
    path('update/<int:pk>',views.user_update,name='update'),
    path('search/',views.user_search,name='search'),
]