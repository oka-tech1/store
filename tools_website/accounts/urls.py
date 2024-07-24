from django.urls import path
from .views import SignupView, details
from . import views

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('', details.as_view(), name='details'),
    path('saveform/', views.saveform, name='saveform'),
    path('success/', views.success, name='success'),
    path('Email/', views.Email, name='Email'),
    path('profile/', views.profile, name='profile'),    
    path('order/<int:id>/', views.order, name='order'),    
    path('fund/<int:id>/', views.fund, name='fund'),    
    path('forum/', views.forum, name='forum'),    
    
 
]
