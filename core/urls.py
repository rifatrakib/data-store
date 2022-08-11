from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    path('automobile/', include('repair_shops.urls')),
    path('property-sales/', include('property_sales.urls')),
    path('business/', include('businesses.urls')),
    path('real-estate/', include('realestate.urls')),
]
