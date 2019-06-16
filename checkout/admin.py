from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.


class OrderLineAdminInline(admin.TabularInline):
    # TabularInline subclass defines the template used to render the Order
    # in the admin interface. StackedInline is another option

    model = OrderLineItem

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )
    # the admin interface has the ability to edit more than one model
    # on a singlr page. This is known as inlines.

admin.site.register(Order, OrderAdmin)