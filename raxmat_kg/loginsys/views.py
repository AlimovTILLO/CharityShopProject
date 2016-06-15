# -*-coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.template import RequestContext
from django.template.context_processors import csrf


def login(request):
    args = {}
    args.update(csrf(request))
    print "test"
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "Пользватель не найден"
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'],
                                        password=newuser_form.cleaned_data['password1'])
            auth.login(request, newuser)
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render_to_response('register.html', args)


def settings(request, templates='settings.html'):
    """
    Processes requests for the settings page, where users
    can edit their profiles.
    """
    page_title = 'Account Settings'
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = UserChangeForm(instance=request.user)
    title = 'Settings'
    return render_to_response(templates, locals(), context_instance=RequestContext(request))
