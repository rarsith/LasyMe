from PySide2 import QtWidgets


class SeparatorWDG(QtWidgets.QFrame):
    def __init__(self, parent=None):
        super(SeparatorWDG, self).__init__(parent)

        self.setFrameShape(QtWidgets.QFrame.HLine)
        self.setFrameShadow(QtWidgets.QFrame.Sunken)
