from django.shortcuts import render
from .models import Product
from .forms import ProductForm, RawProductForm


def product_create_view(request):
	my_form = RawProductForm()
	if request.method == "POST":
		my_form = RawProductForm(request.POST)
		if my_form.is_valid():
			print(my_form.cleaned_data) # this cleaned data is a dictionary
			Product.objects.create(**my_form.cleaned_data)
			my_form = RawProductForm()
		else:
			print(my_form.errors)		
	context = {
		"form": my_form
	}
	return render(request, "products/product_create.html", context)


# def product_create_view(request):
# 	form = ProductForm(request.POST or None)

# 	if form.is_valid():
# 		form.save()
# 		form = ProductForm()

# 	context = {
# 		'form': form
# 	}
# 	return render(request, "products/product_create.html", context)

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