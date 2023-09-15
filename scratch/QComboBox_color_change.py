import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QComboBox, QVBoxLayout, QWidget

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Change QComboBox Color")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.combo_box = QComboBox(self)
        self.combo_box.addItems(["Red", "Green", "Blue"])
        self.combo_box.currentIndexChanged.connect(self.update_combo_color)

        layout = QVBoxLayout()
        layout.addWidget(self.combo_box)
        self.central_widget.setLayout(layout)

    def update_combo_color(self, index):
        colors = ["#c7dbeb", "#ebe9c7", "#f25f55"]  # Define colors
        selected_color = colors[index] if index >= 0 else "black"  # Default to black if no selection

        # Set the background color using CSS style
        style = f"QComboBox {{ background-color: {selected_color}; }}"
        self.combo_box.setStyleSheet(style)

def main():
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
