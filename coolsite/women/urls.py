from django.urls import path
from women.views import *

import women.views

urlpatterns = [
    path('', index),
    path('cats/<int:catid>/',categories)
]



