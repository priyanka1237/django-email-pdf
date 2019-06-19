from django.contrib import admin
from django.urls import include, path
from core.views import mail,getpdf,abc,xyz
admin.autodiscover()

urlpatterns = [
    path('admin/',admin.site.urls),
    path("core/",include('core.urls')),
    path('mail',mail),
    path('getpdf',getpdf),
    path('',abc,name='abc'),
    path('xyz',xyz)
    # url(r'^$', 'pro1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


]
