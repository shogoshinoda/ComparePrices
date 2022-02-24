from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('cprice/', include('compare_prices_app.urls')),
]
