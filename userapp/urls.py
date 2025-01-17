
from django.urls import path
from.import views
urlpatterns =[
    path('',views.index),
    path('about',views.about),
    path('service',views.service),
    path('booking',views.booking),
    path('blog',views.blog),
    path('contact',views.contact),
    path('register',views.reg),
    path('login',views.log),
    path('details',views.details),
    path('edit',views.edit),
    path('update',views.update),
    path('prodact',views.upload),
    path('cards',views.cards),
    path('cart/<int:idn>',views.cart,name='addcart'),
    path('viewcart',views.viewcart),
    path('cartdelete/<int:pid>',views.cartdelete,name='cartdelete'),
    path('email',views.email),
    path('e2',views.e2),
    path('regview',views.regview),
    ]
