from django.shortcuts import render, get_object_or_404, redirect
from .models import Product , Category , Top_banner,Deal 
# Create your views here.
from django.contrib.postgres.search import SearchVector , SearchQuery, SearchRank
from .forms import SearchForm , AddToCartForm 
from django.contrib.postgres.search import TrigramSimilarity

from itertools import chain
# for the cart
from cart.cart import Cart
from django.contrib import messages

def home(request):
	top_banner = Top_banner.objects.all()
	latest_products = Product.objects.all()
	product_with_deals = Deal.objects.all()
	categories = Category.objects.all()

	return render(request, 'core/product/home.html',
		{
		'top_banner':top_banner,
		'latest_products':latest_products,
		'product_with_deals':product_with_deals,
		'categories':categories,
		})

def post_search(request):
	form = SearchForm()
	query = None
	total_len = None
	results = []
	if 'query' in request.GET:
		form = SearchForm(request.GET)
		if form.is_valid():
			query = form.cleaned_data['query']
			results = list(chain( Product.objects.annotate(similarity=TrigramSimilarity('name' ,query),
).filter(similarity__gt=0.1).order_by('-similarity') ,
 Product.objects.annotate(similarity=TrigramSimilarity('brand_name' ,query),
).filter(similarity__gt=0.1).order_by('-similarity') ))
		total_len = len(results)

	else:
		form = SearchForm()
	return render(request, 'core/product/search.html',{
		'form': form,
 		'query': query,
 		'results': results,
 		'total_len':total_len
	})

def  detail_view(request , slug):
	cart = Cart(request)
	product = get_object_or_404(Product , slug=slug)	

	if request.method == 'POST':
	    form = AddToCartForm(request.POST)
	    if form.is_valid():
	    	quantity = form.cleaned_data['quantity']
	    	cart.add(product_id=product.id, quantity=quantity, update_quantity=False)
	    	messages.success(request, 'Item is added to your cart')
	    	return redirect('detail', slug=product.slug)

	else:
		form = AddToCartForm()

	cart_items = request.session.get('cart')
	product_is_present = cart_items.get(str(product.id))
	
	latest_products = Product.objects.all()\
	.exclude(id=product.id)
	same_cat_products = latest_products.filter(category = product.category)\
	.exclude(id = product.id)
	product_with_deals = Deal.objects.all()\
	.exclude(id = product.id)
	categories = Category.objects.all()

	return render(request,'core/product/detail.html',
		{
		'product':product,
		'latest_products':latest_products,
		'same_cat_products':same_cat_products,
		'product_with_deals':product_with_deals,
		'categories':categories,
		'AddToCartForm':AddToCartForm ,
		'product_is_present':product_is_present,
		})

def deals_page(request):
	latest_products = Product.objects.all()
	product_with_deals = Deal.objects.all()
	categories = Category.objects.all()


	return render(request, 'core/product/deals.html',
		{
		'latest_products':latest_products,
		'categories':categories,
		'product_with_deals':product_with_deals,
		})


def cat_page(request , category_slug=None):
	category = None
	no_cat = None
	categories = Category.objects.all()
	products = Product.objects.all()

	if category_slug:
		if 1 <= len(Category.objects.filter(slug = category_slug)):
			if category_slug:
				category = get_object_or_404(Category, slug=category_slug)
				products = products.filter(category=category)
		else:
			no_cat = 'no category with this name'

	if category_slug == None :
		title = 'All'
	else:
		title = category_slug
	return render(request,
	'core/product/list.html',
	{'category': category,
	'categories': categories,
	'no_cat':no_cat,
	'title':title,
	'products': products})
