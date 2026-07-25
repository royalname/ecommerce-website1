from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Review
from django.db.models import Q


def product_list(request):

    query = request.GET.get("q")

    products = Product.objects.all()

    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )

    return render(
        request,
        "products/products.html",
        {
            "products": products,
            "query": query
        }
    )

def product_detail(request, id):

    product = get_object_or_404(Product, id=id)

    reviews = Review.objects.filter(
        product=product
    ).order_by("-created_at")

    return render(
        request,
        "products/product_detail.html",
        {
            "product": product,
            "reviews": reviews
        }
    )


@login_required
def add_review(request, id):

    product = get_object_or_404(Product, id=id)

    if request.method == "POST":

        rating = request.POST.get("rating")

        comment = request.POST.get("comment")

        Review.objects.create(
            product=product,
            user=request.user,
            rating=rating,
            comment=comment
        )

    return redirect("product_detail", id=id)