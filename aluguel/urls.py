"""vcar URL Configuration

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


from django.urls import path
from aluguel.views import listar_carro,cadastrar_carro,atualizar_carro,deletar_carro,detalhar_carro,listar_cliente,detalhar_cliente,cadastrar_cliente,atualizar_cliente,deletar_cliente



urlpatterns = [
    path('carro/',listar_carro,name='listar_carro' ),
    path('carro/<int:pk>',detalhar_carro,name='detalhar_carro' ),
    path('carro/cadastrar',cadastrar_carro,name='cadastrar_carro' ),
    path('carro/atualizar/<int:pk>',atualizar_carro,name='atualizar_carro' ),
    path('carro/deletrar/<int:pk>',deletar_carro,name='deletar_carro' ),
   
    path('cliente/',listar_cliente,name='listar_cliente' ),
    path('cliente/<int:pk>',detalhar_cliente,name='detalhar_cliente' ),
    path('cliente/cadastrar',cadastrar_cliente,name='cadastrar_cliente' ),
    path('cliente/atualizar/<int:pk>',atualizar_cliente,name='atualizar_cliente' ),
    path('cliente/deletrar/<int:pk>',deletar_cliente,name='deletar_cliente' ),
    
    # path('alugar/',listar_carro,name='listar_' ),
    # path('alugar/<int:pk>',listar_carro,name='detalhar_carros' ),
    # path('alugar/cadastrar',listar_carro,name='cadastrar_carro' ),
    # path('alugar/atualizar/<int:pk>',listar_carro,name='atualizar_carro' ),
    # path('alugar/deletrar/<int:pk>',listar_carro,name='deletar_carro' ),
    
    
    
]