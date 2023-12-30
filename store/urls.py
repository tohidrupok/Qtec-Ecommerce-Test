from django.urls import path
from . import views

urlpatterns = [
    path('', views.category, name='store'),
    path('category/<slug:category_slug>/', views.category, name='products_by_category'),
    path('seller/<int:seller_id>/', views.products_by_seller, name='products_by_seller'),
    path('warranty/<int:warranty_period_id>/', views.products_by_warranty, name='products_by_warranty'),
    path('type/<int:product_by_id>/', views.products_by_type, name='products_by_type'),
    path('sorting/', views.store2, name='sorting'),
    path('search/', views.search, name='search'),

]