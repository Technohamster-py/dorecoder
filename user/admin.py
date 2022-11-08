from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['login', 'firstname', 'lastname', 'balance']
    list_filter = ['login', 'firstname', 'lastname', 'balance']
    list_editable = ['balance']

# Register your models here.
