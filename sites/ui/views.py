#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.core.urlresolvers import resolve

def index(request):
    current_url = resolve(request.get_full_path()).url_name
    ctx = {'current_url':current_url}
    return render(request, 'ui/index.html', ctx)

def basecss(request):
    current_url = resolve(request.get_full_path()).url_name
    ctx = {'current_url':current_url}
    return render(request, 'ui/basecss.html', ctx)

def bootstrapexamples(request):
    current_url = resolve(request.get_full_path()).url_name
    ctx = {'current_url':current_url}
    return render(request, 'ui/bootstrapexamples.html', ctx)

def button(request):
    current_url = resolve(request.get_full_path()).url_name
    ctx = {'current_url':current_url}
    return render(request, 'ui/button.html', ctx)

def compontents(request):
    current_url = resolve(request.get_full_path()).url_name
    ctx = {'current_url':current_url}
    return render(request, 'ui/components.html', ctx)

def customize(request):
    current_url = resolve(request.get_full_path()).url_name
    ctx = {'current_url':current_url}
    return render(request, 'ui/customize.html', ctx)

def javascript(request):
    current_url = resolve(request.get_full_path()).url_name
    ctx = {'current_url':current_url}
    return render(request, 'ui/javascript.html', ctx)

def less(request):
    current_url = resolve(request.get_full_path()).url_name
    ctx = {'current_url':current_url}
    return render(request, 'ui/javascript.html', ctx)

def scaffolding(request):
    current_url = resolve(request.get_full_path()).url_name
    ctx = {'current_url':current_url}
    return render(request, 'ui/scaffolding.html', ctx)

def upgradebootstrap2(request):
    current_url = resolve(request.get_full_path()).url_name
    ctx = {'current_url':current_url}
    return render(request, 'ui/upgradebootstrap2.html', ctx)