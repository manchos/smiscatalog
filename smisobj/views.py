# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from smisobj.models import SmisObj


def smis_objects_all(request):
    SmisObj.objects.all()
