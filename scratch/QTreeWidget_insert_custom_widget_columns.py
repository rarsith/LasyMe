import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem, QPushButton, QLineEdit, QWidget, QVBoxLayout, QCheckBox, QComboBox
from PySide2.QtCore import Signal, QObject

class TreeWidgetExample(QMainWindow):
    # Define a custom signal
    comboSelectionChanged = Signal(int, str)

    def __init__(self):
        super().__init__()

        self.setWindowTitle("QTreeWidget Cell Value Example")
        self.setGeometry(100, 100, 600, 400)

        self.tree_widget = QTreeWidget(self)
        self.tree_widget.setHeaderLabels(["Column 0", "Column 1"])
        self.setCentralWidget(self.tree_widget)

        root_item = QTreeWidgetItem(self.tree_widget, ["Root Item"])

        child01 = self.addCustomWidget(root_item, "Child Item 1")
        self.addCustomWidget(child01, "Child Item 2")

        self.tree_widget.expandAll()

        # Create a QComboBox for row selection
        self.row_combo = QComboBox()
        self.row_combo.addItems([str(i) for i in range(self.tree_widget.topLevelItemCount())])
        self.row_combo.setCurrentIndex(0)

        layout = QVBoxLayout()
        layout.addWidget(self.row_combo)
        self.setLayout(layout)

        # Connect the combo box selection to emit the custom signal
        self.row_combo.currentIndexChanged.connect(self.emit_combo_selection)

    def addCustomWidget(self, parent_item, name):
        child_item = QTreeWidgetItem(parent_item, [name])

        # Create a custom widget container for column 1
        custom_widget_container = QWidget()
        custom_layout = QVBoxLayout(custom_widget_container)

        # Add a delete button
        delete_button = QPushButton("Delete")
        delete_button.clicked.connect(self.on_delete_button_clicked)
        custom_layout.addWidget(delete_button)

        # Add a checkbox
        checkbox = QCheckBox("Done")
        custom_layout.addWidget(checkbox)

        # Add a combobox with options
        combo_box = QComboBox()
        combo_box.addItems(["Done", "Work in Progress", "In Progress"])
        custom_layout.addWidget(combo_box)

        # Connect the combo box to emit the custom signal when its selection changes
        combo_box.currentIndexChanged.connect(self.emit_combo_selection)

        self.tree_widget.setItemWidget(child_item, 1, custom_widget_container)

        # Create a QLineEdit with random text for column 0
        line_edit = QLineEdit()
        line_edit.setText(f"Random Text: {name}")
        self.tree_widget.setItemWidget(child_item, 0, line_edit)

        return child_item

    def on_delete_button_clicked(self):
        # Handle delete button click here
        pass

    def emit_combo_selection(self):
        # Emit the custom signal with the selected row and combo box value
        selected_row = int(self.row_combo.currentText())
        selected_value = self.sender().currentText()
        self.comboSelectionChanged.emit(selected_row, selected_value)

def main():
    app = QApplication(sys.argv)
    window = TreeWidgetExample()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
