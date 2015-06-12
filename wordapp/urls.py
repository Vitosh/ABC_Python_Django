from django.conf.urls import include, url
from django.contrib import admin

from wordcountapp import urls as wordcountapp_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(wordcountapp_urls)),
]
