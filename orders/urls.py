from django.urls import path
from .views import (
    home,
    createProduct,
    updateProduct,
    deleteProduct,
    createOrder,
    deleteOrder,
    registerPage,
    loginPage,
    logoutUser
)


urlpatterns = [
    path('register/', registerPage, name="register"),
	path('login/', loginPage, name="login"),  
	path('logout/', logoutUser, name="logout"),


     path('', home, name="home"),
     path('create_product/', createProduct, name="create_product"),
     path('update_product/<pk>/', updateProduct, name="update_product"),
     path('delete_product/<pk>/', deleteProduct, name="delete_product"),
     path('create_order/', createOrder, name="create_order"),
     path('delete_order/<pk>/', deleteOrder, name="delete_order"),
]