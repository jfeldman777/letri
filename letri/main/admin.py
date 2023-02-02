from django.contrib import admin
from .models import Region, Army, Body, Rang, Ethnos, Education, MobiType,Letter
# Register your models here.
admin.site.register(Region)
admin.site.register(Army)
admin.site.register(Body)
admin.site.register(Education)
admin.site.register(MobiType)
admin.site.register(Rang)
admin.site.register(Ethnos)
admin.site.register(Letter)
