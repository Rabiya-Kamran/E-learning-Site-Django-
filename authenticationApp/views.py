from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import reverse
from django.views.generic import TemplateView, FormView

from .forms import ContactForm

# Create your views here.
def register_view(request):
    if request.method=='POST':
       form=UserCreationForm(request.POST)
       if form.is_valid():
           user=form.save()
           login(request,user)
           return redirect('dashboard')
    else:
        initial_data={'username':'', 'password1':'', 'password2':''}
        form=UserCreationForm(initial=initial_data)
    return render(request, 'auth/register.html', {'form': form})

def login_view(request):
    if request.method=='POST':
       form=AuthenticationForm(request,data=request.POST)
       if form.is_valid():
           user=form.get_user()
           login(request,user)
           return redirect('dashboard')
    else:
        initial_data={'username':'', 'password':''}
        form=AuthenticationForm(initial=initial_data)
    return render(request, 'auth/login.html', {'form': form})



def dashboard_view(request):
    return render(request,'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')


def contactUs_view(request):
    if request.method=='GET':
       form=AuthenticationForm(request,data=request.POST)
       if form.is_valid():
           user=form.get_user()
           login(request,user)
           return redirect('dashboard')
    else:
        initial_data={'username':'', 'password':''}
        form=AuthenticationForm(initial=initial_data)
    return render(request, 'auth/login.html', {'form': form})




class ContactView(FormView):
    form_class = ContactForm
    template_name = "contact.html"

    def get_success_url(self):
        return reverse("contact")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        subject = form.cleaned_data.get("subject")
        message = form.cleaned_data.get("message")

        full_message = f"""
            Received message below from {email}, {subject}
            ________________________


            {message}
            """
        send_mail(
            subject="Received contact form submission",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL],
        )
        return super(ContactView, self).form_valid(form)