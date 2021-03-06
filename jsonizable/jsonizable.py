from .common import _create_attribute
from .common import _get_att_composed
from .common import _get_att_name
from .read import read
from .write import write


class Jsonizable(object):

    class Meta:
        schema = None
        expose = None

    def __init__(self, json=None):
        if json:
            self.read(json)

    def _isJsonizable(self, obj):
        return issubclass(obj, Jsonizable)

    # Assign read and write function
    read = read
    write = write

    # Assign helpers
    _get_att_composed = _get_att_composed
    _get_att_name = _get_att_name
    _create_attribute = _create_attribute
