from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .forms import CheckoutForm
from .models import Item, OrderItem, Order, Category
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone


# Create your views here.
class HomeView(ListView):
    model = Item
    paginate_by = 9
    template_name = "item_list.html"
    context_object_name = 'items'


class ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"
    context_object_name = 'item'


@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "Кол-во товара обновлено")
            return redirect("core:order-summary")
        else:
            messages.info(request, "Этот товар был добавлен в вашу корзину.")
            order.items.add(order_item)
            return redirect("core:order-summary")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "Этот товар был добавлен в вашу корзину.")
        return redirect("core:order-summary")


# удаление товара из корзины на странице товара
@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False)[0]
            order.items.remove(order_item)
            messages.info(request, "Товар был удален из вашей корзины.")
            return redirect("core:order-summary")
        else:
            # заказ не содержит этого товара
            messages.info(request, "Этого товара нет в вашей корзине.")
            return redirect("core:order-summary")
    else:
        # нет заказа
        messages.info(request, "У вас нет активного заказа.")
        return redirect("core:order-summary")


@login_required
def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(request, "Кол-во товара обновлено")
            return redirect("core:order-summary")
        else:
            # заказ не содержит этого товара
            messages.info(request, "Этого товара нет в вашей корзине.")
            return redirect("core:order-summary")
    else:
        # нет заказа
        messages.info(request, "У вас нет активного заказа.")
        return redirect("core:order-summary")


class OrderSummeryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order,
            }
            return render(self.request, 'order_summer.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, "У вас нету активного заказа")
            return redirect("/")


class Post_By_Category(ListView):
    template_name = 'item_list.html'
    context_object_name = 'items'
    paginate_by = 9
    allow_empty = False

    def get_queryset(self):
        return Item.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


class CheckoutView(View):
    def get(self, *args, **kwargs):
        order = Order.objects.get(user=self.request.user, ordered=False)
        form = CheckoutForm()
        context = {
            'form': form,
            'object': order,
        }
        return render(self.request, "checkout.html", context)

    def post(self, *args, **kwargs):
        order = Order.objects.get(user=self.request.user, ordered=False)
        order.ordered = True
        order.save()
        return redirect('core:item_list')
  