from django.urls import path
from . import views

urlpatterns = [
    # Authentication URLs
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    
    # Dashboard
    path('', views.dashboard, name='dashboard'),
    
    # Contact URLs
    path('contacts/', views.ContactListView.as_view(), name='contact_list'),
    path('contacts/add/', views.ContactCreateView.as_view(), name='contact_create'),
    path('contacts/<int:pk>/', views.ContactDetailView.as_view(), name='contact_detail'),
    path('contacts/<int:pk>/edit/', views.ContactUpdateView.as_view(), name='contact_update'),
    path('contacts/<int:pk>/delete/', views.ContactDeleteView.as_view(), name='contact_delete'),
    
    # AJAX URLs
    path('contacts/<int:pk>/toggle-favorite/', views.toggle_favorite, name='toggle_favorite'),
]
