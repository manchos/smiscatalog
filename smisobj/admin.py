# -*- coding: utf-8 -*-
from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
# Register your models here.
from smisobj.models import SmisObj

# import smisobj




class SmisObjAdmin(admin.ModelAdmin):
    list_display = ('smisobj_name', 'smisobj_address', 'smisobj_category')
    list_editable = ('smisobj_address', 'smisobj_category')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':40})},
    }

admin.site.register(SmisObj, SmisObjAdmin)