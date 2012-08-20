#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.core.urlresolvers import resolve


def index(request):
    current_url = resolve(request.get_full_path()).url_name
    ctx = {'current_url':current_url}
    return render(request, 'index.html', ctx)

def newfeatures(request):
    current_url = resolve(request.get_full_path()).url_name
    ctx = {'current_url':current_url}
    return render(request, 'newfeatures.html', ctx)

def userprofile(request):
    current_url = resolve(request.get_full_path()).url_name
    ctx = {'current_url':current_url}
    return render(request, 'userprofile.html', ctx)

def helpcenter(request):
    current_url = resolve(request.get_full_path()).url_name
    ctx = {'current_url':current_url}
    return render(request, 'helpcenter.html', ctx)

def aboutus(request):
    current_url = resolve(request.get_full_path()).url_name
    ctx = {'current_url':current_url}
    return render(request, 'aboutus.html', ctx)

def contactus(request):
    current_url = resolve(request.get_full_path()).url_name
    ctx = {'current_url':current_url}
    return render(request, 'contactus.html', ctx)

def onlineservice(request):
    current_url = resolve(request.get_full_path()).url_name
    ctx = {'current_url':current_url}
    return render(request, 'onlineservice.html', ctx)

def reportissue(request):
    current_url = resolve(request.get_full_path()).url_name
    ctx = {'current_url':current_url}
    return render(request, 'reportissue.html', ctx)

def logout(request):
    ctx = {'current_url':'idx'}
    return render(request, 'index.html', ctx)
