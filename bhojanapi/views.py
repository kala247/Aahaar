from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from bhojan.models import Partymenu
from bhojanapi.utils import is_json
from bhojanapi.mixins import SerializeMixin
import json
from django.core.serializers import serialize
from bhojan.db import p_menu
# Create your views here.

class BhojanCRUDCBV(SerializeMixin,View):
    def get_resource_by_id(self,id):
        try:
            menu = Partymenu.objects.get(id=id)
        except Partymenu.DoesNotExist:
            menu =None
        return menu

    def get(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({"msg":"You requested invalid format of data"})
            return HttpResponse(json_data,content_type='application/json',status=400)
        p_data = json.loads(data)
        given_id = p_data.get('id',None)
        if given_id is not None:
            menu = self.get_resource_by_id(given_id)
            # print(menu)
            if menu is None:
                json_data = json.dumps({"msg": "You requested Id not matched with any data"})
                return HttpResponse(json_data, content_type='application/json', status=404)
            json_data = self.serialize(menu)
            return HttpResponse(json_data, content_type='application/json', status=200)
        qs = Partymenu.objects.all()
        json_data = self.serialize(qs)
        return HttpResponse(json_data, content_type='application/json',status=200)








