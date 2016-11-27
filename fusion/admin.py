from django.contrib import admin
from fusion.models import Fruit, Apple, Pineapple, Membrillo, Pen, Fusion


class FruitAdmin(admin.ModelAdmin):
    pass


class AppleAdmin(admin.ModelAdmin):
    pass


class PineappleAdmin(admin.ModelAdmin):
    pass


class MembrilloAdmin(admin.ModelAdmin):
    pass


class PenAdmin(admin.ModelAdmin):
    pass

class FusionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Fruit, FruitAdmin)
admin.site.register(Apple, AppleAdmin)
admin.site.register(Pineapple, PineappleAdmin)
admin.site.register(Membrillo, MembrilloAdmin)
admin.site.register(Pen, PenAdmin)
admin.site.register(Fusion, FusionAdmin)