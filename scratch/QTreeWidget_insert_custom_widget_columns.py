import sys
import random
from PySide2.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem, QPushButton, QLineEdit, QWidget, QVBoxLayout, QCheckBox, QComboBox

class TreeWidgetExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Custom Widget in QTreeWidget Example")
        self.setGeometry(100, 100, 600, 400)

        self.tree_widget = QTreeWidget(self)
        self.tree_widget.setHeaderLabels(["Column 0", "Column 1"])
        self.setCentralWidget(self.tree_widget)

        root_item = QTreeWidgetItem(self.tree_widget, ["Root Item"])

        child01 = self.addCustomWidget(root_item, "Child Item 1")
        self.addCustomWidget(child01, "Child Item 2")

        self.tree_widget.expandAll()

    def addCustomWidget(self, parent_item, name):
        child_item = QTreeWidgetItem(parent_item, [name])

        # Create a custom widget container for column 1
        custom_widget_container = QWidget()
        custom_layout = QVBoxLayout(custom_widget_container)

        # Add a delete button
        delete_button = QPushButton("Delete")
        custom_layout.addWidget(delete_button)

        # Add a checkbox
        checkbox = QCheckBox("Done")
        custom_layout.addWidget(checkbox)

        # Add a combobox with options
        combo_box = QComboBox()
        combo_box.addItems(["Done", "Work in Progress", "In Progress"])
        custom_layout.addWidget(combo_box)

        self.tree_widget.setItemWidget(child_item, 1, custom_widget_container)

        # Create a QLineEdit with random text for column 0
        line_edit = QLineEdit()
        line_edit.setText(f"Random Text: {random.randint(1, 100)}")
        self.tree_widget.setItemWidget(child_item, 0, line_edit)
        return child_item

def main():
    app = QApplication(sys.argv)
    window = TreeWidgetExample()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
