from django.contrib import admin
from .models import Category, Attribute, AttributeOption, CustomizedItem


admin.site.register(Category)
admin.site.register(Attribute)
admin.site.register(AttributeOption)
admin.site.register(CustomizedItem)
