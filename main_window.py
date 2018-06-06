import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        open_save_file = QAction('打开存档文件', self)
        open_save_file.setShortcut('CTRL+O')
        #open_save_file.triggered.connect()

        open_scenario_file = QAction('打开剧本文件', self)
        open_scenario_file.setShortcut('CTRL+P')
        #open_scenario_file.triggered.connect()

        save_button = QAction('保存', self)
        save_button.setShortcut('Ctrl+S')
        #save_button.triggered.connect()

        exit_button = QAction('退出', self)
        exit_button.setShortcut('Ctrl+Q')
        exit_button.triggered.connect(qApp.quit)

        self.statusBar()

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(open_save_file)
        file_menu.addAction(open_scenario_file)
        file_menu.addAction(save_button)
        file_menu.addAction(exit_button)
        self.setGeometry(300, 150, 800, 600)
        self.setWindowTitle('ZHSGZEditor')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())