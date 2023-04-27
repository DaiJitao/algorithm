from typing import List, Optional

from django.http import HttpResponse
from django.urls import path, register_converter
from django.views import View
from django.db import models

class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, World!")

class Person(models.Model):
    name = models.CharField("", max_length=200)

if __name__ == '__main__':
    Person.ob