from decimal import Decimal
from django.contrib import auth
from django.contrib.auth.models import User
from django.http.response import JsonResponse, Http404
from django.template.context_processors import csrf
from django.core.paginator import Paginator
from django.shortcuts import render_to_response, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

from forms import CommentForm
from models import Item, Comments, ItemCategory


def index(request):
    return items(request)


def items(request, page_number=1):
    all_items = Item.objects.filter(item_active=True)
    current_page = Paginator(all_items, 8)
    return render_to_response('Items.html',
                              {'items': current_page.page(page_number), 'username': auth.get_user(request).username})


def item(request, item_id):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['item'] = Item.objects.get(id=item_id)
    args['comments'] = Comments.objects.filter(comments_item_id=item_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render_to_response('item.html', args)


def addcomment(request, item_id):
    if request.POST and ("pause" not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            user_id = User.objects.all()
            comment = form.save(commit=False)
            comment.comments_item = Item.objects.get(id=item_id)
            comment.comments_from = User.objects.get(id=user_id)
            form.save()
            request.session.set_expiry(30)
            request.session['pause'] = True
    return redirect('/items/get/%s/' % item_id)


def funds(request):
    return render_to_response('foundations.html', {'username': auth.get_user(request).username})


def itemcategory(request):
    all_categories = ItemCategory.objects.all()
    return render_to_response('category.html',
                              {'all_categories': all_categories, 'username': auth.get_user(request).username})


class CategoryProduct(ListView):
    template_name = "category_product.html"
    model = Item

    def get_context_data(self, **kwargs):
        context = super(CategoryProduct, self).get_context_data(**kwargs)
        all_categories = ItemCategory.objects.all()
        context['all_categories'] = all_categories
        context['username'] = auth.get_user(self.request).username
        # context['username'] = auth.get_user(self.request).username
        context['items'] = Item.objects.filter(item_category=self.kwargs['pk'])
        return context


@csrf_exempt
def GetAjaxCategoryProduct(request):
    if request.is_ajax():
        category = ItemCategory.objects.values_list('id', 'item_category_name')
        return JsonResponse({"category": dict(category)})
    else:
        raise Http404


def commission(request):
    item_commission = Item.objects.filter(item_active=True)
    item_commission = Item.item_price * 0.15
    commissioned_price = Item.item_price - item_commission
    charity_value = commissioned_price * (Item.item_charity / Decimal(100.0))
    return render_to_response(
        {'item_commission': item_commission, 'commissioned_price': commissioned_price, 'charity_value': charity_value})
