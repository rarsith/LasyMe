from PySide2 import QtWidgets, QtCore


class CustomDelegate(QtWidgets.QStyledItemDelegate):
    def sizeHint(self, option, index):
        size_hint = super().sizeHint(option, index)
        size_hint.setHeight(30)
        return size_hint

    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignmentFlag.AlignVCenter

class ExitingTasksViewerWDG(QtWidgets.QTreeWidget):
    def __init__(self, parent=None):
        super(ExitingTasksViewerWDG, self).__init__(parent)

        self.widget_width = 650
        self.create_widgets()

    def create_widgets(self):
        column_index = 1
        item_delegate = CustomDelegate()

        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDragDropMode(QtWidgets.QTreeWidget.InternalMove)
        self.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)  # Disable selection highlighting
        self.setSelectionMode(QtWidgets.QTreeWidget.SingleSelection)
        self.setRootIsDecorated(False)

        self.setFocusPolicy(QtCore.Qt.NoFocus)

        self.setDisabled(False)
        self.setMinimumWidth(self.widget_width)
        # self.setMaximumWidth(self.widget_width)

        self.widget_columns_names = ["Heat", "Task Title", "Status", "Prio", "Delete", "ID", "Data"]
        self.setColumnCount(len(self.widget_columns_names))
        self.setHeaderLabels(self.widget_columns_names)
        self.setHeaderHidden(True)
        self.setItemDelegate(item_delegate)

        self.setItemDelegateForColumn(column_index, CustomDelegate(self))

        header = self.header()
        header.setStretchLastSection(False)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        self.setColumnWidth(0, round(self.widget_width*0.30))
        self.setColumnWidth(1, round(self.widget_width*0.60))
        self.setColumnWidth(2, round(self.widget_width*0.13))
        self.setColumnWidth(3, round(self.widget_width*0.13))
        self.setColumnWidth(4, round(self.widget_width*0.05))
        self.setColumnWidth(5, round(self.widget_width*0.005))
        self.setColumnWidth(6, round(self.widget_width*0.005))

        self.setColumnHidden(5, True)
        self.setColumnHidden(6, True)

    def size_hint_for_row(self, row):
        return 40
