from django.urls import path
from . import views

app_name = 'myshop'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('installment', views.installment, name='installment'),
    path('pay', views.payments, name='payments'),
    path('rules', views.rules, name='rules'),
    path('policy', views.policy, name='policy'),
    path('offer', views.offer, name='offer'),
    path('exchange/', views.exchange, name='exchange'),
    path('deliver', views.delivery, name='delivery'),
    #path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    #path('<int:id>/<slug:slug>', views.product_detail, name='product_detail'),

]