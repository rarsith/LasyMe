from PySide2 import QtWidgets, QtCore
from common_utils.date_time import DateTime

from operations.tdb_priorities import Priorities
from operations.tdb_statuses import Statuses
from operations.tiny_ops.tasks_ops import TinyOps


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
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setMaximumHeight(25)
        self.progress_bar.setMaximumWidth(100)
        self.progress_bar.setTextVisible(False)

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
        end_date = self.tops.get_task_end_date(task_id)

        percentage_interval = DateTime().get_time_elapsed(start_day=start_date, end_day=end_date, percentage=True)
        self.progress_bar.setValue(int(percentage_interval))

        progress_bar_curr_val = self.progress_bar.value()

        if progress_bar_curr_val <= 20:
            self.progress_bar.setStyleSheet("""QProgressBar {border: 1px solid rgba(33, 37, 43, 180);
            border-radius: 5px;
            text-align: center;
            background-color: rgba(33, 37, 43, 180);
            color: black;}
            QProgressBar::chunk {background-color: #FFD700;}""")
        elif progress_bar_curr_val <= 30:
            self.progress_bar.setStyleSheet("""QProgressBar {border: 1px solid rgba(33, 37, 43, 180);
            border-radius: 5px;
            text-align: center;
            background-color: rgba(33, 37, 43, 180);
            color: black;}
            QProgressBar::chunk {background-color: #00e1ff;}""")
        else:
            self.progress_bar.setStyleSheet("""QProgressBar {border: 1px solid rgba(33, 37, 43, 180);
            border-radius: 5px;
            text-align: center;
            background-color: rgba(33, 37, 43, 180);
            color: black;}
            QProgressBar::chunk {background-color: #ff3700;}""")
        return percentage_interval

    def get_task_title(self, task_id):
        get_title = self.tops.get_task_title(task_id=task_id)
        self.task_title_lb.setText(get_title)

    def get_task_status(self, task_id):
        get_status = self.tops.get_task_status(task_id=task_id)
        self.status_cb.setCurrentText(get_status)

    def get_task_prio(self, task_id):
        get_prio = self.tops.get_task_prio(task_id=task_id)
        self.prio_cb.setCurrentText(get_prio)


class TaskEntityCore(TaskEntityWDG):
    def __init__(self, parent=None):
        super(TaskEntityCore, self).__init__(parent)

        self.create_connections()

    def create_connections(self):
        pass


if __name__=="__main__":
    import sys



    app = QtWidgets.QApplication(sys.argv)
    test_dialog = TaskEntityWDG()
    test_dialog.show()
    sys.exit(app.exec_())