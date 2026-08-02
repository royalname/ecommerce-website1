from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Product, Review, Category


def product_list(request):

    query = request.GET.get("q")
    category_id = request.GET.get("category")

    products = Product.objects.all()
    categories = Category.objects.all()

    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )

    if category_id:
        products = products.filter(
            category_id=category_id
        )

    return render(
        request,
        "products/products.html",
        {
            "products": products,
            "categories": categories,
            "query": query,
            "selected_category": category_id,
        }
    )


def product_detail(request, id):

    product = get_object_or_404(Product, id=id)

    reviews = Review.objects.filter(
        product=product
    ).order_by("-created_at")

    related_products = Product.objects.filter(
        category=product.category
    ).exclude(
        id=product.id
    )[:4]

    return render(
        request,
        "products/product_detail.html",
        {
            "product": product,
            "reviews": reviews,
            "related_products": related_products,
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