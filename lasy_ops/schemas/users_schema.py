from lasy_ops.tdb_attributes_definitions import UsersAttributesDefinitions


class UsersSchema:
    def __init__(self, definitions: UsersAttributesDefinitions):
        self.definitions = definitions

        self.user_name = ""
        self.user_assigned_to = []

    @property
    def name(self):
        return self.user_name

    @name.setter
    def name(self, tga_name):
        self.user_name = tga_name

    @property
    def assigned_to(self):
        return self.user_assigned_to

    @assigned_to.setter
    def assigned_to(self, value):
        self.user_assigned_to = value

    def to_dict(self):
        return {self.definitions.name: self.user_name,
                self.definitions.assigned_to: self.assigned_to
                }
