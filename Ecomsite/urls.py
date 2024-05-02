"""
URL configuration for Ecomsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.base,name='base'),
    path('',views.index,name='index'),
    path('about-us/',views.about_us,name='aboutus'),
    path('contact-us/',views.contact_us,name='contactus'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('faq/',views.faq,name='faq'),
    path('my-account/',views.myaccount,name='myaccount'),
    path('checkout-cart/',views.checkout_cart,name='checkoutcart'),
    path('add-cart/<int:id>',views.checkout_cart,name='addtocart'),
    path('show-cart/',views.show_cart,name='showcart'),
    path('pluscart/',views.plus_cart,name='pluscart'),
    path('minuscart/',views.minus_cart,name='minuscart'),
    path('removecart/',views.remove_cart,name='removecart'),


    path('checkout-info/',views.checkout_info,name='checkoutinfo'),
    path('shipping-address/',views.shipping_address,name='shipping'),
    path('charge/',views.charge,name='charge'),
    path('checkout-payment/',views.checkout_payment,name='checkoutpayment'),
    # path('checkout-session/',views.create_checkout_session,name='checkoutsession'),

    path('checkout-complete/',views.checkout_complete,name='checkoutcomplete'),
    path('product-detail/',views.product_detail,name='productdetail'),
    path('product-detail/<int:id>',views.product_detail,name='productinfo'),
    path('product/',views.product,name='product'),
    path('product-category/<str:product_category>/',views.product,name='product_category'),
    path('search-results/',views.search_results,name='searchresults'),
]


urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)