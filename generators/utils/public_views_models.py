class Property(object):
        def __init__(self, name, type, visibility):
            self.name = name
            self.type = type
            self.visibility = visibility

        @property
        def label(self):
            return self.name.capitalize()

        def __str__(self):
            tip = self.type
            if self.type.__class__.__name__ == 'Reference':
                tip = 'Reference'
            return self.name + ":" + tip + ":" + self.label + ":" + self.visibility


class Item(object):

    def __init__(self, name):
        self.name = name.lower()
        self._properties = []

    @property
    def properties(self):
        return self._properties

    @properties.setter
    def properties(self, value):
        if not isinstance(value, list):
            raise TypeError("Properties must be a list!")
        self._properties = value