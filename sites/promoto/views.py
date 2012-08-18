#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.shortcuts import render

def index(request):
    ctx = {}
    return render(request, 'index.html', ctx)