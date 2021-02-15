from django.shortcuts import render
from .models import Product

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