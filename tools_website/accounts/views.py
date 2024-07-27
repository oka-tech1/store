from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import tools, contactus, profile, order_emails
from .forms import UserForm, emailform



class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class details(ListView):
    model = tools
    template_name = 'details.html'
    
        
def order(request, id):
    orders = tools.objects.get(id=id)
    profile = request.user.profile
    if profile.account_detals >= orders.price:
        profile.account_detals -= orders.price
        profile.save()
        return render(request, 'order_suc.html', {'orders': orders, 'remaining_balance': profile.account_detals})
    else:
        return render(request, 'insuf_fund.html',  {'orders':orders,})
                 

def fund(request, id):
    order = tools.objects.get(id=id)
    template = loader.get_template('fundaccount.html')
    context = {
        'order': order,
    }
    return HttpResponse(template.render(context, request))
	

    
def saveform(request):
    if request.method =='POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/credit/')
    else:
        form = UserForm()
    return render(request, 'contactform.html', {'form':form})
    

def success(request):
    template = loader.get_template('success.html')
    return HttpResponse(template.render())    



def credit(request):
    template = loader.get_template('credit.html')
    return HttpResponse(template.render())




def Email(request):
    if request.method == "POST":  
            form = emailform(request.POST)  
            if form.is_valid():  
                form.save()
                return HttpResponseRedirect('/accounts/success/')
    else:
        form = emailform()
    return render(request, 'email.html', {'form':form}) 
 
def forum(request):
    template = loader.get_template('forum.html')
    return HttpResponse(template.render())


def profile(request):
    return render(request, 'profile.html')

