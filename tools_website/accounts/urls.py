from django.urls import path
from .views import SignupView, details, wallets
from . import views

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('', details.as_view(), name='details'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'),
    path('wallets', views.wallets, name='wallets'),    
    path('order/<int:id>/', views.order, name='order'),    
    path('fund/', views.fund, name='fund'),    
    path('forum/', views.forum, name='forum'),    
    
 
]
