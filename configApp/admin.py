from django.contrib import admin
from .models import *

admin.site.register([Organization,Region,ManagerOrganization,Student])