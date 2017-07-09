# Stuff for Stelaris

import collections

class Tile(object):
    """Single tile"""

    def __init__(self, **kwargs):
        self.resources = collections.defaultdict(int)
        for arg in kwargs:
            self.resources[arg] = self.setresource(kwargs[arg])
        pass

    def setresource(self, value):
        """We have only positive resources"""
        return max(0, value)