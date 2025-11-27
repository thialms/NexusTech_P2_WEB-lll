from django.urls import path
from .views import CompraView

urlpatterns = [
    path('<int:item_id>/', CompraView.as_view(), name='compra'),
]