from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, ListView, TemplateView, DetailView
from buyer.forms import LoginForm, RegistrationForm, UserCreationForm, ProductAddForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from buyer.models import Products, UserProfile
from django.contrib.auth.models import User
from .forms import UserProfile

# Create your views here.

class HomeView(ListView):
    template_name = "index.html"
    context_object_name = "products"
    model = Products

class SignUpView(CreateView):
    template_name = "signup.html"
    form_class = RegistrationForm
    success_url = reverse_lazy("signin")

    def form_valid(self, form) :
        messages.success(self.request,"Account Created Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Account Creation failed")
        return super().form_invalid(form)



class SignInView(FormView):
    template_name = "login.html"
    form_class = LoginForm


    def post(self, request, *args, **kwargs) :
         form = LoginForm(request.POST)
         if form.is_valid():
            uname = form.cleaned_data.get("username")
            pwd = form.cleaned_data.get("password")
            usr = authenticate(request, username = uname, password = pwd)
            if usr:
                login(request, usr)
                messages.success(request, "Logined Successfully")
                return redirect("home")
            else:
                messages.error(request, "Invalid Credentials")
                return render(request, "login.html", {"form":form})



def product_create(request):
    if request.method == 'POST':
        form = ProductAddForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            return redirect('home')
    else:
        form = ProductAddForm()
    return render(request, 'productadd_form.html', {'form': form})



class ProductDetailView(DetailView):
    template_name = "product_detail.html"
    context_object_name = "product"
    pk_url_kwarg = "id"
    model= Products




    
