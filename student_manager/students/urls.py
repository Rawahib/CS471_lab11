from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('new/', views.student_create, name='student_create'),
    path('<int:pk>/edit/', views.student_update, name='student_update'),
    path('<int:pk>/delete/', views.student_delete, name='student_delete'),

    path('m2m/', views.student2_list, name='student2_list'),
    path('m2m/new/', views.student2_create, name='student2_create'),
    path('m2m/<int:pk>/edit/', views.student2_update, name='student2_update'),
    path('m2m/<int:pk>/delete/', views.student2_delete, name='student2_delete'),
    path('m2m/address/new/', views.address2_create, name='address2_create'),

    path('<int:student_id>/profile/', views.student_profile_view, name='student_profile_view'),
    path('<int:student_id>/profile/create/', views.student_profile_create, name='student_profile_create'),
    path('<int:student_id>/profile/edit/', views.student_profile_update, name='student_profile_update'),
]


