from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from .views import GeneratePdf, GenerateHtmlPdf
#from cart import views as cart_view
#from orders import views as order_view
urlpatterns = [
    path('', GeneratePdf.as_view()),
    path('html', GenerateHtmlPdf.as_view()),
]
