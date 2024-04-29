from django.contrib import admin
from .models import *

db_list = [
    UserList,
]

admin.site.register(db_list)