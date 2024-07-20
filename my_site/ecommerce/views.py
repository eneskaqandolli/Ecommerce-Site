from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .models import Product, Order
from django.views.generic import DetailView


# Create your views here.
def index(request):
    products = Product.objects.all()
    
    ## search code
    product_name = request.GET.get("product_name")
    if product_name != "" and product_name is not None:
        products = products.filter(title__icontains=product_name)
        
    ## paginator code
    paginator = Paginator(products, 4)
    page = request.GET.get("page")
    products = paginator.get_page(page)
    
    return render(request, "ecommerce/index.html", {"products": products})

class ProductDetailView(DetailView):
    model = Product
    template_name = "ecommerce/product_detail.html"
    context_object_name = "product"
    
def checkout(request):
    if request.method == "POST":
        items = request.POST.get("items", "")
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        address = request.POST.get("address", "")
        city = request.POST.get("city", "")
        state = request.POST.get("state", "")
        zip = request.POST.get("zip", "")
        total = request.POST.get("total", "")
        
        order = Order(items=items, name=name, email=email, address=address, city=city, state=state, zip=zip, total=total)
        order.save()
        return redirect(order_confirmed)
        
    return render(request, "ecommerce/checkout.html", {})

def order_confirmed(request):
    return render(request, "ecommerce/order_confirmed.html")