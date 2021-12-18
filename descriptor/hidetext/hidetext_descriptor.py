class HideTextDescriptor:
    def __init__(self, instance):
        self.instance = instance

    def __set__(self, instance, value):
        self.instance = value

    def __get__(self, instance, owner):
        return self.instance

    def __delete__(self, instance):
        del instance

    def __repr__(self):
        return self.instance
