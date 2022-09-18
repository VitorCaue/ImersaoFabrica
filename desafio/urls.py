from django.contrib import admin
from django.urls import path
from atv.views import home, loja, nova_compra, nova_compra1, nova_compra2, nova_compra3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('loja/', loja),
    path('selecao/', nova_compra, name='op1'),
    path('selecao2/',nova_compra1,name='op2'),
    path('selecao3/',nova_compra2,name='op3'),
    path('selecao4/',nova_compra3,name='op4'),
]
