from django.core.serializers import serialize
import json

class SerializeMixin(object):
    def serialize(self,qs):
        json_data = serialize('json',qs)
        p_data = json.loads(json_data)
        final_list =[]
        for obj in p_data:
            menu_data = obj['fields']
            final_list.append(menu_data)
        json_data = json.dumps(final_list)
        return json_data

