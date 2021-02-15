from django.shortcuts import render
from .models import Product
from .forms import ProductForm

def product_create_view(request):
	form = ProductForm(request.POST or None)

	if form.is_valid():
		form.save()

	context = {
		'form': form
	}
	return render(request, "products/product_create.html", context)

# Create your views here.
def product_detail_view(request):
	obj	= Product.objects.get(id=1)
	context = {
		'object': obj
	}
	# context = {
	# 'title': obj.title,
	# 'features' = obj.features
	# 'description': obj.description,
	# 'price' = obj.price,
	# 'summary' = obj.summary,
	# 'features' = obj.features,
	# }

	return render(request, "products/product_detail.html", context)