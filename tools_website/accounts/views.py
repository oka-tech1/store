from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import tools, contactus, profile, order_emails
from .forms import userform, emailform



class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class details(ListView):
    model = tools
    template_name = 'details.html'
    
        
def order(request, id):
    orders = tools.objects.get(id=id)
    template = loader.get_template('order.html')
    context = {
        'orders': orders,
    }
    return HttpResponse(template.render(context, request))
    

def fund(request, id):
    order = tools.objects.get(id=id)
    template = loader.get_template('fundaccount.html')
    context = {
        'order': order,
    }
    return HttpResponse(template.render(context, request))
	

    
def saveform(request):
    context ={}
    form = userform(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "contactform.html", context)

def success(request):
    template = loader.get_template('success.html')
    return HttpResponse(template.render())    


def Email(request):
    if request.method == "POST":  
            form = emailform(request.POST)  
            if form.is_valid():  
                try:  
                    return redirect('/Email')  
                except:  
                    pass  
    else:  
        form = emailform()  
    return render(request,'email.html',{'form':form})  
def profile(request):
    template = loader.get_template('profile.html')
    return HttpResponse(template.render())    



def forum(request):
    template = loader.get_template('forum.html')
    return HttpResponse(template.render())


def profile(request):
    return render(request, 'profile.html')
