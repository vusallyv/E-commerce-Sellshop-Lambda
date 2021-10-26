
from order.models import Cart
from django.db.models import Sum


def get_user_cart(request):
    try:
        product_sum = list(Cart.objects.get(user=request.user).product.values_list(
            'product__price').annotate(total_price=Sum('product__price')))[0][1]
        product_count =  Cart.objects.get(user=request.user).product,
    except:
        product_sum = 0
        product_count = 0
    return {
        'product_count': product_count,
        'product_sum': product_sum
    }


# def remove_product_from_cart(request):
#     if request.POST:
#         delete_product = Cart.objects.get(user=request.user).product.remove(1)
#     else:
#         delete_product = None
#     return {
#         'delete_product': delete_product
#     }
