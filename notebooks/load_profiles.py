"""Notebook helper for loading pipeline profiles."""


def load_profiles(path):
    import json

    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)
