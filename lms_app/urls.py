from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('books/',views.books,name="books"),
    path('update/<str:slug>',views.update,name="update"),
    path('delete/<str:slug>',views.delete,name="delete"),

]
