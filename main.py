import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenu, QMenuBar, QLabel, QWidgetAction, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')

        exit_widget = QWidget(self)
        exit_layout = QVBoxLayout(exit_widget)
        exit_label = QLabel('Exit', exit_widget)
        exit_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        exit_layout.addWidget(exit_label)

        exit_action = QWidgetAction(self)
        exit_action.setDefaultWidget(exit_widget)
        exit_action.triggered.connect(self.close)

        file_menu.addAction(exit_action)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menu Bar PBE')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec())