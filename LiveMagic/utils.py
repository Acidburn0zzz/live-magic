import os

def find_resource(resource):
    dirs = (
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'misc'),
        '/usr/share/live-magic',
        '/usr/local/share/live-magic',
    )

    tried = []
    for base in dirs:
        path = os.path.join(base, resource)
        if os.path.isfile(path):
            return path
        tried.append(path)

    raise ValueError, 'Cannot find %s resource. Tried: %s' % (resource, tried)
