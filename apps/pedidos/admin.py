from django.contrib import admin


from .models import Item, Pedido

admin.site.register(Pedido)
admin.site.register(Item)