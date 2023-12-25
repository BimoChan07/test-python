from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "QuickCare"
admin.site.site_title = "QuickCare Admin Portal"
admin.site.index_title = "Welcome to QuickCare"

urlpatterns = [
    path('admin/', admin.site.urls),
        path('', include('home.urls')),

]
