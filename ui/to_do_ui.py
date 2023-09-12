import sys
from PySide2 import QtWidgets

from ui.exiting_tasks_viewer import ExitingTasksViewerBuild
from ui.task_properties_tabs import TaskPropertiesTabsBuild
from ui.task_user_input import InputTaskBuild
from ui.task_user_input_preview import TaskPreviewPropertiesBuild



class ToDoMeMainWDG(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ToDoMeMainWDG, self).__init__(parent)

        self.setWindowTitle("LASY ME")
        self.setGeometry(500, 500, 800, 600)

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.tasks_viewer_wdg = ExitingTasksViewerBuild()
        self.task_input_wdg = InputTaskBuild()
        self.task_preview_properties_wdg = TaskPreviewPropertiesBuild()
        self.task_properties_tabs_wdg = TaskPropertiesTabsBuild()

    def create_layout(self):
        viewer_and_input_layout = QtWidgets.QVBoxLayout()
        viewer_and_input_layout.addWidget(self.tasks_viewer_wdg)
        viewer_and_input_layout.addWidget(self.task_preview_properties_wdg)
        viewer_and_input_layout.addWidget(self.task_input_wdg)

        main_layout = QtWidgets.QHBoxLayout(self)
        main_layout.addLayout(viewer_and_input_layout)
        main_layout.addWidget(self.task_properties_tabs_wdg)


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    test_dialog = ToDoMeMainWDG()
    test_dialog.show()
    sys.exit(app.exec_())
