from PySide2 import QtWidgets, QtCore
from common_utils.date_time import DateTime

from operations.tdb_priorities import Priorities
from operations.tdb_statuses import Statuses
from operations.tiny_ops import TinyOps


class TaskProgressBarWDG(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(TaskProgressBarWDG, self).__init__(parent)

        self.ui_progress_bar_wdg()

    def ui_progress_bar_wdg(self):
        widget_item = QtWidgets.QProgressBar()

        # widget_item.setMaximumHeight(10)
        widget_item.setTextVisible(False)
        widget_item.setValue(50)
        widget_item.setOrientation(QtCore.Qt.Vertical)



class TaskEntityWDG(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(TaskEntityWDG, self).__init__(parent)
        self.tops = TinyOps()
        self.create_widgets()

    def create_widgets(self):
        self.progress_bar = QtWidgets.QProgressBar()
        self.progress_bar.setValue(20)
        self.progress_bar.setMaximumHeight(20)
        self.progress_bar.setMaximumWidth(10)
        self.progress_bar.setOrientation(QtCore.Qt.Vertical)

        self.task_title_lb = QtWidgets.QLabel("This is a sample Task Title Text......................XXXXXXXX")

        self.status_cb = QtWidgets.QComboBox()
        self.status_cb.addItems(Statuses().all_statuses)

        self.prio_cb = QtWidgets.QComboBox()
        self.prio_cb.addItems(Priorities().all_priorities)

        self.edit_btn = QtWidgets.QPushButton("Edit")
        self.delete_btn = QtWidgets.QPushButton("X")
        self.heat_bar_lb = QtWidgets.QLabel()

        self.heat_bar_lb.setStyleSheet("background-color: lightgreen")

    def get_progress_bar_amount(self, task_id):
        start_date = self.tops.get_task_start_date(task_id)
        print(start_date)
        end_date = self.tops.get_task_end_date(task_id)
        current_time = DateTime().curr_date
        percentage_interval = DateTime().get_time_elapsed(start_day=start_date, end_day=end_date, percentage=True)
        self.progress_bar.setValue(int(percentage_interval))
        return percentage_interval

    def get_task_title(self, task_id):
        get_title = TinyOps().get_task_title(task_id=task_id)
        self.task_title_lb.setText(get_title)

    def get_task_status(self, task_id):
        get_status = TinyOps().get_task_status(task_id=task_id)
        self.status_cb.setCurrentText(get_status)

    def get_task_prio(self, task_id):
        get_prio = TinyOps().get_task_status(task_id=task_id)
        self.prio_cb.setCurrentText(get_prio)


class TaskEntityCore():
    def __init__(self, parent=None):
        super(TaskEntityCore, self).__init__(parent)




if __name__=="__main__":
    import sys
    tops = TinyOps()
    task_progress = tops.get_task_task_details(1)
    print(task_progress)


    app = QtWidgets.QApplication(sys.argv)
    test_dialog = TaskEntityWDG()
    test_dialog.show()
    sys.exit(app.exec_())