class Department:

    def __init__(self, name, location):
        self.name = name
        self.location = location

    @property
    def email(self):
        return '{}@skylark.org'.format(self.name)
