from PySide2.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem, QMainWindow
from PySide2.QtCore import Qt
import sys
from datetime import datetime, timedelta

def get_insertion_date(item):
    # Get the item's insertion date from a custom data role
    insertion_date = item.data(0, Qt.UserRole)
    return insertion_date

def sort_tree_by_insertion_date(tree_widget):
    # Sort the tree by insertion date
    tree_widget.sortItems(0, Qt.AscendingOrder, key=get_insertion_date)

app = QApplication(sys.argv)
window = QMainWindow()

treeWidget = QTreeWidget()
treeWidget.setHeaderLabels(["Date Inserted", "Item"])  # Add headers

# Add items with insertion dates
item1 = QTreeWidgetItem(treeWidget, [datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Item 1"])
item1.setData(0, Qt.UserRole, datetime.now())  # Store insertion date as custom data

item2 = QTreeWidgetItem(treeWidget, [datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Item 2"])
item2.setData(0, Qt.UserRole, datetime.now() + timedelta(days=1))  # Store insertion date as custom data

item3 = QTreeWidgetItem(treeWidget, [datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Item 3"])
item3.setData(0, Qt.UserRole, datetime.now() - timedelta(days=1))  # Store insertion date as custom data

# Sort the tree by insertion date
sort_tree_by_insertion_date(treeWidget)

window.setCentralWidget(treeWidget)
window.show()

sys.exit(app.exec_())
