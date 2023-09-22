import os

class Envars():

    @property
    def os_root(self):
        return os.environ.get('LASY_ROOT')

    @os_root.setter
    def os_root(self, value):
        os.environ['LASY_ROOT'] = value

    @property
    def lasy_id(self):
        return os.environ.get('LASY_ID')

    @lasy_id.setter
    def lasy_id(self, value):
        os.environ['LASY_ID'] = value

    @property
    def current_tags(self):
        envar_value = os.environ.get('LASY_TAGS')
        delimiter = ","
        if delimiter in envar_value:
            elements = envar_value.split(delimiter)
            return elements
        return [envar_value]

    @current_tags.setter
    def current_tags(self, value: list):
        list_to_str = ','.join(map(str, value))
        os.environ['LASY_TAGS'] = list_to_str

    @property
    def current_prios(self):
        return os.environ.get('LASY_PRIOS')

    @current_prios.setter
    def current_prios(self, value):
        os.environ['LASY_PRIOS'] = value

    @property
    def current_statuses(self):
        return os.environ.get('LASY_STATUSES')

    @current_statuses.setter
    def current_statuses(self, value):
        os.environ['LASY_STATUSES'] = value

    def taget_path(self, *args):
        path = '.'.join(args)
        return path
