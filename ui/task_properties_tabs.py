from PySide2 import QtWidgets

from ui.task_properties_editor import TaskPropertiesEditorBuild
from ui.task_statistics_viewer import TaskStatisticsBuild
from ui.task_tags_manager import TaskTagManagerBuild

html_path = '/\\scratch\\interactive_gantt_chart.html'


class TaskPropertiesTabsBuild(QtWidgets.QTabWidget):
    def __init__(self, parent=None):
        super(TaskPropertiesTabsBuild, self).__init__(parent)

        self.properties_wdg = QtWidgets.QWidget()

        self.task_properties_wdg = TaskPropertiesEditorBuild()
        self.task_tag_manager_wdg = TaskTagManagerBuild()
        self.task_statistics_wdg = TaskStatisticsBuild(html_path)

        self.addTab(self.task_properties_wdg, "Properties")
        self.addTab(self.task_tag_manager_wdg, "Tags")
        self.addTab(self.task_statistics_wdg, "Statistics")
        self.setTabPosition(QtWidgets.QTabWidget.North)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    test_dialog = TaskPropertiesTabsBuild()
    test_dialog.show()
    sys.exit(app.exec_())
