from order.models import Cart


def get_user_cart(request):
    return {
        'product_count': Cart.objects.get(user=request.user).product
    }
