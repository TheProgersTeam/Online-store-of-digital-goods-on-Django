from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin


class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = Gallery


class ProductAdmin(SummernoteModelAdmin):
    inlines = [GalleryInline]
    description = '__all__'


class FAQAdmin(SummernoteModelAdmin):
    text = '__all__'


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Gallery)
admin.site.register(Slider)
admin.site.register(Comment)
admin.site.register(Support)
admin.site.register(Settings)
admin.site.register(Ban)
admin.site.register(Messenger)
admin.site.register(FAQ, FAQAdmin)
