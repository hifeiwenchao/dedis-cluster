
from __future__ import absolute_import, unicode_literals

import json
from django.core.serializers.json import DjangoJSONEncoder
try:
    from django.utils.encoding import force_bytes
    from django.utils.encoding import force_text
except ImportError:
    from django.utils.encoding import smart_bytes as force_bytes
    from django.utils.encoding import force_unicode as force_text


from .base import BaseSerializer


class JSONSerializer(BaseSerializer):
    def dumps(self, value):
        return json.dumps(value, cls=DjangoJSONEncoder).encode()
        # return force_bytes(json.dumps(value))

    def loads(self, value):
        return json.loads(value.decode())
        # return json.loads(force_text(value))
