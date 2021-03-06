from django.shortcuts import HttpResponseRedirect, get_object_or_404

from mainapp.models import Product
from cartapp.models import Cart


def cart_add(request, id_product=None):
    product = get_object_or_404(Product, id=id_product)
    carts = Cart.objects.filter(user=request.user, product=product)

    if not carts.exists():
        cart = Cart(user=request.user, product=product)
        cart.quantity += 1
        cart.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        cart = carts.first()
        cart.quantity += 1
        cart.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def cart_add_item(request, id_product=None):
    cart = Cart.objects.get(id=id_product)
    cart.quantity += 1
    cart.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def cart_remove_item(request, id_product=None):
    cart = Cart.objects.get(id=id_product)

    if cart.quantity > 1:
        cart.quantity -= 1
        cart.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    if cart.quantity == 1:
        cart.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def cart_clear_position(request, id_product=None):
    cart = Cart.objects.get(id=id_product)

    cart.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def cart_clear(request):
    cart = Cart.objects.all()
    cart.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def count_total_price(request):
    carts = Cart.objects.filter(user=request.user)
    total = 0
    for cart in carts:
        total += cart.product.price * cart.product.quantity
    return total
