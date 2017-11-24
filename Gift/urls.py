from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve
from .settings import MEDIA_ROOT
from paypal.standard.ipn import urls as paypal_urls
from paypal_store import views as paypal_views
from user_account import views as user_account_views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
    url(r'^a-very-hard-to-guess-url/', include(paypal_urls)),
    url(r'^paypal-return', paypal_views.paypal_return),
    url(r'^paypal-cancel', paypal_views.paypal_cancel),
    url(r'^', include('products.urls', namespace='products')),
    url(r'^register/$', user_account_views.register, name='register'),

]
