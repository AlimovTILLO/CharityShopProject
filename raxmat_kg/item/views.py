from django.contrib import auth
from django.template.context_processors import csrf
from django.core.paginator import Paginator
from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from forms import CommentForm
from item.models import Item, Comments



def index(request):
    return render(request, 'main.html')


def items(request, page_number=1):
    all_items = Item.objects.all()
    current_page = Paginator(all_items, 4)
    return render_to_response('Items.html', {'items': current_page.page(page_number), 'username': auth.get_user(request).username})


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
            comment = form.save(commit=False)
            comment.comments_item = Item.objects.get(id=item_id)
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('/items/get/%s/' % item_id)
