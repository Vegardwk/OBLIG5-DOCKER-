"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from .views import get_cars
from .views import save_car
from .views import update_car
from .views import delete_car
from .views import order_car
from .views import cancel_car_order
from .views import rent_car
from .views import return_car

urlpatterns = [
    path("admin/", admin.site.urls),
    path("cars/", get_cars),
    path("save_car/", save_car),
    path("update_car/<int:id>", update_car),
    path("delete_car/<int:id>", delete_car),
    path("order_car/<int:customerid>/<int:carid>", order_car),
    path("cancel_car_order/<int:customerid>/<int:carid>", cancel_car_order),
    path("rent_car/<int:customerid>/<int:carid>", rent_car),
    path("return_car/<int:customerid>/<int:carid>", return_car),
]
