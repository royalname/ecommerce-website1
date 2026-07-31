from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Sum

from products.models import Product, Category, Review
from orders.models import Order


def home(request):

    products = Product.objects.all()[:8]

    total_products = Product.objects.count()

    total_categories = Category.objects.count()

    total_users = User.objects.count()

    total_orders = Order.objects.count()

    total_reviews = Review.objects.count()

    total_sales = (
        Order.objects.aggregate(
            total=Sum("total_amount")
        )["total"] or 0
    )

    context = {
        "products": products,
        "total_products": total_products,
        "total_categories": total_categories,
        "total_users": total_users,
        "total_orders": total_orders,
        "total_reviews": total_reviews,
        "total_sales": total_sales,
    }

    return render(
        request,
        "home/index.html",
        context
    )