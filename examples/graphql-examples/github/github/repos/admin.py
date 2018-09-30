from __future__ import unicode_literals
from django.contrib import admin
from github.repos.models import Repo#, Owner


# Register your models here.
admin.site.register(Repo)
#admin.site.register(Owner)