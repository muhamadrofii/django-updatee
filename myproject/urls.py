"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
import infoapp.views as infoapp_views  # Mengimpor views dengan alias
import contentapp.views as contentapp_views  # Mengimpor views dengan alias
import accountsapp.views as accountsapp_views  # Mengimpor views dengan alias
import subscriptionsapp.views as subscriptionsapp_views  # Mengimpor views dengan alias

# from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', infoapp_views.index, name='index'),
    path('berita/', infoapp_views.berita, name='berita'),
    path('tentangKami/', infoapp_views.tentangKami, name='tentangKami'),
    path('faq/', infoapp_views.faq, name='faq'),
    path('kids/', contentapp_views.kids, name='kids'),
    path('parents/', contentapp_views.parents, name='parents'),
    path('login/', accountsapp_views.login, name='login'),
    path('register/', accountsapp_views.register, name='register'),
    path('langganan/', subscriptionsapp_views.langganan, name='langganan'),
    path('profile/', accountsapp_views.profil, name='profil'),
    path('beranda/', accountsapp_views.beranda, name='beranda'),
    path('landingpage/', accountsapp_views.landingPage, name='landingPage'),
    path('subscribe/', subscriptionsapp_views.subscribe, name='subscribe'),
    path('create-payment-link/', subscriptionsapp_views.create_payment_link, name='create_payment_link'),
    path('video/<str:youtube_id>/', contentapp_views.watch_video, name='watch_video'),  # Tambah URL untuk menonton video
    path('parent/', contentapp_views.parent, name ='parent'),
    # path('quiz', contentapp_views.quiz, name='quiz'),
    path('parents/quiz/<int:quiz_id>/', contentapp_views.quiz_detail, name='quiz_detail'),
    path('create-payment/payment-notification/', subscriptionsapp_views.payment_notification, name='payment_notification'),
    # path('payment-success/', payment_success, name='payment-success'),
    path('quiz/result/<int:quiz_id>/', contentapp_views.quiz_detail, name='quiz_result'),
    re_path(r'^payment-success(?:/.*)?$', subscriptionsapp_views.payment_success, name='payment_success'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)