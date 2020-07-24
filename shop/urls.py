from django.urls import path
from . import views

app_name='shop'
urlpatterns = [
    path("", views.index, name="ShopHome"),
    path('blog/',views.Blog, name="Blog"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("productview/<int:myid>", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
    path("handlerequest/", views.handlerequest, name="handlerequest"),

    path('accounts/create/', views.signupView, name='signup'),
    path('accounts/login/', views.signinView, name='signin'),
    path('accounts/logout/', views.signoutView, name='signout'),

]