#!/usr/bin/env python
import json


class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list({"name": entry.name, "version": entry.version} for entry in obj)
        return json.JSONEncoder.default(self, obj)
