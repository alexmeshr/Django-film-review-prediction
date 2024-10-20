from django.contrib import admin
from .models import Review

# Register your models here.
class MyModelAdmin(admin.ModelAdmin):
    class Meta:
        model = Review

admin.site.register(Review, MyModelAdmin)
