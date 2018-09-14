from .read import read
from .write import write
from .common import (
    _create_attribute,
    _get_att_name,
    _get_att_composed,
)

class Jsonizable(object):
    
    class Meta:
        schema = None
        expose = None

    def __init__(self, json):
        self.read(json)

    def _isJsonizable(self, obj):
        return issubclass(obj, Jsonizable)


# Assign read and write function
Jsonizable.read = read
Jsonizable.write = write

# Assign helpers
Jsonizable._get_att_composed = _get_att_composed
Jsonizable._get_att_name = _get_att_name
Jsonizable._create_attribute = _create_attribute
