from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name='products'),
    path('<int:bd>/', mainapp.products, name='product')
]