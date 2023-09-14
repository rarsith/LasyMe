import getpass
from common_utils.date_time import DateTime
from operations.tdb_attributes_definitions import TagsAttributesDefinitions


class TagsSchema:
    def __init__(self, definitions: TagsAttributesDefinitions):
        self.definitions = definitions

        self.tag_name = ""
        self.tag_created_by = getpass.getuser()
        self.tag_date_created = DateTime().curr_date
        self.tag_time_created = DateTime().curr_time
        self.tag_assigned_to = []

    @property
    def name(self):
        return self.tag_name

    @name.setter
    def name(self, tga_name):
        self.tag_name = tga_name

    @property
    def created_by(self):
        return self.tag_created_by

    @created_by.setter
    def created_by(self, value):
        self.tag_created_by = value

    @property
    def assigned_to(self):
        return self.tag_assigned_to

    @assigned_to.setter
    def assigned_to(self, value):
        self.tag_assigned_to = value

    def to_dict(self):
        return {self.definitions.name: self.tag_name,
                self.definitions.created_by: self.tag_created_by,
                self.definitions.date_created: self.tag_date_created,
                self.definitions.time_created: self.tag_time_created,
                self.definitions.assigned_to: self.assigned_to

                }
