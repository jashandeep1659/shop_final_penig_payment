from django.urls import path
from . import views 

urlpatterns = [
	path('',views.home , name="home"),
	path('Top-deals/',views.deals_page , name="deals_page"),
	path('search/', views.post_search, name='post_search'),
	path('all/', views.cat_page, name='cat_page'),
	path('all/<slug:category_slug>/', views.cat_page, name='cat_page'),
	path('<slug:slug>/',views.detail_view , name="detail"),
]