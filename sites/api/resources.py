__author__ = 'Administrator'
from tastypie.resources import ModelResource
from models import MyModel

class MyModelResource(ModelResource):
    class Meta:
        queryset = MyModel.objects.all()
        allowed_methods = ['get']