from django.urls import path
from AppCoder.views import visualizar_familiares

urlpatterns = [

    path("familiares/", visualizar_familiares),

]