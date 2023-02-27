from django.contrib import admin
from django.urls import path, include
from buyer import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.SignInView.as_view(), name="signin"),
    path("register", views.SignUpView.as_view(),name="signup"),
    path("home", views.HomeView.as_view(), name="home"),
    path("productadd", views.product_create, name="add-product"),
     path("products/details/<int:id>", views.ProductDetailView.as_view(), name="product-detail"),
    #  path('profile', views.profile, name='profile')
    
    
]
 