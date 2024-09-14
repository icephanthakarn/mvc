from django.contrib import admin
from .models import Cow

@admin.register(Cow)
class CowAdmin(admin.ModelAdmin):
    list_display = ('cow_id', 'color', 'age_years', 'age_months', 'milk_bottles_produced', 'is_bsod')
