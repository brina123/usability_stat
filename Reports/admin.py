from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Product,Test,Testiranec,Task,Tag,Grade,Tester, Product_part

admin.site.register(Product)
admin.site.register(Test)
admin.site.register(Testiranec)
admin.site.register(Task)
admin.site.register(Tag)
admin.site.register(Grade)
admin.site.register(Tester)
admin.site.register(Product_part)

