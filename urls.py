from django.conf.urls import url, include

from marketfy.admin import marketfy_admin

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^admin/', include(marketfy_admin.urls)),
]
