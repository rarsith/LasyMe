from PySide2 import QtWidgets, QtCore


class ExitingTasksViewerWDG(QtWidgets.QTreeWidget):
    def __init__(self, parent=None):
        super(ExitingTasksViewerWDG, self).__init__(parent)

        self.widget_width = 650
        self.create_widgets()

    def create_widgets(self):

        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDragDropMode(QtWidgets.QTreeWidget.InternalMove)
        self.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)  # Disable selection highlighting
        # self.setSelectionMode(QtWidgets.QTreeWidget.SingleSelection)
        self.setFocusPolicy(QtCore.Qt.NoFocus)

        # self.setRootIsDecorated(False)

        self.setDisabled(False)
        self.setMinimumWidth(self.widget_width)
        # self.setMaximumWidth(self.widget_width)

        self.widget_columns_names = ["Heat", "Task Title", "Status", "Prio", "Delete", "ID"]
        self.setColumnCount(len(self.widget_columns_names))
        self.setHeaderLabels(self.widget_columns_names)
        self.setHeaderHidden(True)

        header = self.header()
        header.setStretchLastSection(False)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        self.setColumnWidth(0, round(self.widget_width*0.30))
        self.setColumnWidth(1, round(self.widget_width*0.60))
        self.setColumnWidth(2, round(self.widget_width*0.10))
        self.setColumnWidth(3, round(self.widget_width*0.10))
        self.setColumnWidth(4, round(self.widget_width*0.05))
        self.setColumnWidth(5, round(self.widget_width*0.005))

        self.setColumnHidden(5, True)
