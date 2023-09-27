from PySide2 import QtWidgets, QtCore
from lasy_common_utils.date_time_utils import DateTime
from lasy_ops.tdb_priorities import Priorities
from lasy_ops.tdb_statuses import Statuses
from lasy_ops.tiny_ops.tasks_ops import TinyOps
from lasy_ui.custom_widgets.custom_fonts_widget import define_font



class TaskProgressBarWDG(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(TaskProgressBarWDG, self).__init__(parent)

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.progress_bar = QtWidgets.QProgressBar()
        self.progress_bar.setMaximumHeight(40)
        self.progress_bar.setMaximumWidth(120)
        self.progress_bar.setTextVisible(False)

        self.remaining_days_lb = QtWidgets.QLabel()
        self.remaining_days_lb.setMinimumWidth(10)
        self.remaining_days_lb.setMinimumHeight(10)
        self.remaining_days_lb.setStyleSheet("background-color: transparent; color: silver;")
        self.remaining_days_lb.setAlignment(QtCore.Qt.AlignCenter)

    def create_layout(self):
        main_layout = QtWidgets.QHBoxLayout(self)
        main_layout.addWidget(self.progress_bar)
        main_layout.addWidget(self.remaining_days_lb)
        main_layout.setContentsMargins(0, 2, 0, 2)

class TaskEntityWDG(QtWidgets.QWidget):
    def __init__(self, task_id, parent=None):
        super(TaskEntityWDG, self).__init__(parent)

        self.task_id = task_id
        self.tops = TinyOps()
        self.create_widgets()

    def create_widgets(self):
        ubuntu_font = define_font()
        self.prog_bar = TaskProgressBarWDG()

        self.task_title_lb = QtWidgets.QLabel("-----------")
        self.task_title_lb.setStyleSheet(f"background-color: transparent; color: black;")
        self.task_title_lb.setFont(ubuntu_font)
        self.task_title_lb.setAlignment(QtCore.Qt.AlignmentFlag.AlignVCenter) #QtCore.Qt.AlignmentFlag.AlignCenter |

        self.status_cb = QtWidgets.QComboBox()
        self.status_cb.wheelEvent = lambda event: None
        self.status_cb.addItems(Statuses().all_statuses)

        self.prio_cb = QtWidgets.QComboBox()
        self.prio_cb.wheelEvent = lambda event: None
        self.prio_cb.addItems(Priorities().all_priorities)

        self.edit_btn = QtWidgets.QPushButton("Edit")
        self.delete_btn = QtWidgets.QPushButton("X")
        self.delete_btn.setStyleSheet("""QPushButton 
        {
        border: 1px solid rgba(33, 37, 43, 180);
        border-radius: 5px;
        text-align: center;
        background-color: rgba(165, 42, 42, 180);
        color: #b1b1b1;
        }""")
        self.delete_btn.setMaximumWidth(20)

    def get_progress_bar_amount(self):
        start_date = self.tops.get_task_start_date(self.task_id)
        end_date = self.tops.get_task_end_date(self.task_id)

        time_left_interval = DateTime().today_to_end_day(end_day=end_date)
        percentage_interval = DateTime().get_time_elapsed(start_day=start_date, end_day=end_date, percentage=True)
        self.prog_bar.remaining_days_lb.setText(str(time_left_interval))
        if percentage_interval <=100:
            self.prog_bar.progress_bar.setValue(int(percentage_interval))
        else:
            self.prog_bar.progress_bar.setValue(100)

        progress_bar_curr_val = self.prog_bar.progress_bar.value()

        if progress_bar_curr_val <= 20:
            self.prog_bar.progress_bar.setStyleSheet("""QProgressBar {border: 1px solid rgba(33, 37, 43, 180);
            border-radius: 5px;
            text-align: center;
            background-color: rgba(33, 37, 43, 180);
            color: black;}
            QProgressBar::chunk {background-color: #335A84;}""")
        elif progress_bar_curr_val <= 40:
            self.prog_bar.progress_bar.setStyleSheet("""QProgressBar {border: 1px solid rgba(33, 37, 43, 180);
            border-radius: 5px;
            text-align: center;
            background-color: rgba(33, 37, 43, 180);
            color: black;}
            QProgressBar::chunk {background-color: #1b8a5a;}""")

        elif progress_bar_curr_val <= 60:
            self.prog_bar.progress_bar.setStyleSheet("""QProgressBar {border: 1px solid rgba(33, 37, 43, 180);
            border-radius: 5px;
            text-align: center;
            background-color: rgba(33, 37, 43, 180);
            color: black;}
            QProgressBar::chunk {background-color: #fbb021;}""")

        elif progress_bar_curr_val <= 80:
            self.prog_bar.progress_bar.setStyleSheet("""QProgressBar {border: 1px solid rgba(33, 37, 43, 180);
            border-radius: 5px;
            text-align: center;
            background-color: rgba(33, 37, 43, 180);
            color: black;}
            QProgressBar::chunk {background-color: #f68838;}""")

        else:
            self.prog_bar.progress_bar.setStyleSheet("""QProgressBar {border: 1px solid rgba(33, 37, 43, 180);
            border-radius: 5px;
            text-align: center;
            background-color: rgba(33, 37, 43, 180);
            color: black;}
            QProgressBar::chunk {background-color: #990000;}""")
        return percentage_interval

    def get_task_title(self):
        get_title = self.tops.get_task_title(task_id=self.task_id)
        self.task_title_lb.setText(get_title)

    def get_task_status(self):
        get_status = self.tops.get_task_status(task_id=self.task_id)
        self.status_cb.setCurrentText(get_status)

    def get_task_prio(self):
        get_prio = self.tops.get_task_prio(task_id=self.task_id)
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