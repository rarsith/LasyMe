from PySide2 import QtWidgets

from lasy_ui.tasks_properties_editor import TaskPropertiesEditorCore
from lasy_ui.tasks_tags_manager import TaskTagManagerCore


class TaskPropertiesTabsBuild(QtWidgets.QTabWidget):
    def __init__(self, parent=None):
        super(TaskPropertiesTabsBuild, self).__init__(parent)

        self.properties_wdg = QtWidgets.QWidget()

        self.task_properties_wdg = TaskPropertiesEditorCore()
        self.task_tag_manager_wdg = TaskTagManagerCore()

        self.addTab(self.task_properties_wdg, "Properties")
        self.addTab(self.task_tag_manager_wdg, "Tags")
        self.setTabPosition(QtWidgets.QTabWidget.North)

        self.setMaximumWidth(400)


if __name__ == "__main__":
    import sys
    import os

    # os.environ["LASY_DATA_ROOT"] = 'D:\\My_Apps_Repo\\database_testing_sandbox'

    app = QtWidgets.QApplication(sys.argv)
    test_dialog = TaskPropertiesTabsBuild()
    test_dialog.show()
    sys.exit(app.exec_())
