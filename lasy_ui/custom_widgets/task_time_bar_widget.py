from PySide2 import QtWidgets, QtCore


class TaskProgressBar(QtWidgets.QProgressBar):
    def __init__(self, parent=None):
        super(TaskProgressBar, self).__init__(parent)

        self.start_date = QtCore.QDateTime.currentDateTime()
        self.end_date = QtCore.QDateTime()
        self.setValue(95)
        self.setTextVisible(False)

    def updateProgress(self, end_date):
        e_time = QtCore.QTime(end_date)

        current_time = QtCore.QDateTime.currentDateTime().time()

        time_left = self.end_time.secsTo(current_time)
        total_time = self.end_time.secsTo(QtCore.QTime(23, 59, 59))
        progress_percentage = (total_time - time_left) / total_time * 100

        color = self.calculate_heatmap_color(progress_percentage)

        style = f"QProgressBar {{ background-color: {color}; }} QProgressBar::chunk {{ background-color: {color}; }}"
        self.progress_bar.setStyleSheet(style)

    def calculate_heatmap_color(self, progress_percentage):
        red = min(int(255 * (progress_percentage / 100)), 255)
        blue = min(int(255 * ((100 - progress_percentage) / 100)), 255)
        color = f"rgb({red}, 0, {blue})"
        return color
