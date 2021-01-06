from django.contrib.gis import admin
from django.urls import path, include
from allauth.account.views import confirm_email
from django.conf.urls import url
urlpatterns = [
    path('admin/', admin.site.urls),

    # authentications
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^account/', include('allauth.urls')),
    url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$',
        confirm_email, name='account_confirm_email'),

    # api app
    path('api/', include('api.urls'))
]
