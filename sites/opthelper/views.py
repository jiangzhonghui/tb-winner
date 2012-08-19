#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.core.urlresolvers import resolve

def index(request):
    current_url = resolve(request.get_full_path()).url_name
    ctx = {'current_url':current_url}
    return render(request, 'opthelper.html', ctx)