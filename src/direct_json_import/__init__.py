import sys
import os
import json
from importlib.abc import MetaPathFinder, Loader
from importlib.util import spec_from_loader


EXT_JSON  = '.json'

__all__ = []


class JsonLoader(Loader):
    def __init__(self, full_path):
        self._full_path = full_path

    def create_module(self, spec):
        try:
            with open(self._full_path) as json_file:
                self._data = json.load(json_file)
        except Exception:
            raise ImportError
        return None

    def exec_module(self, module):
        module.__dict__.update({"data": self._data})
        return None

class JsonMetaPathFinder(MetaPathFinder):
    def find_spec(self, fullname, path, target=None):
        mod_name = fullname.split('.')[-1]
        paths = path if path else [os.path.abspath(os.curdir)]
        for check_path in paths:
            full_path = os.path.join(check_path, mod_name + EXT_JSON)
            if os.path.exists(full_path):
                return spec_from_loader(fullname,  JsonLoader(full_path))
        return None


sys.meta_path.insert(0, JsonMetaPathFinder())

