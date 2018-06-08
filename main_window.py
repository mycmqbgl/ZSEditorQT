import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication
from Editor import file
from PyQt5.QtWidgets import QFileDialog


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        file_view = file.FileView()
        open_save_file = QAction('打开存档文件', self)
        open_save_file.setShortcut('CTRL+O')
        dialog = QFileDialog()
        open_save_file.triggered.connect(lambda: file_view.open_save_file(dialog))

        open_scenario_file = QAction('打开剧本文件', self)
        open_scenario_file.setShortcut('CTRL+P')
        #open_scenario_file.triggered.connect()

        save_button = QAction('保存', self)
        save_button.setShortcut('Ctrl+S')
        #save_button.triggered.connect()

        exit_button = QAction('退出', self)
        exit_button.setShortcut('Ctrl+Q')
        #exit_button.triggered.connect(qApp.quit)

        edit_person = QAction('编辑人物', self)
        #edit_person.triggered.connect()

        edit_faction = QAction('编辑势力', self)
        #edit_faction.triggered.connect()

        edit_military = QAction('编辑部队', self)
        #edit_military.triggered.connect()

        edit_achitecture = QAction('编辑建筑', self)
        #edit_achitecture.triggered.connect()

        edit_facility = QAction('编辑编队', self)
        #edit_facility.triggered.connect()

        edit_treasure = QAction('编辑宝物', self)
        #edit_treasure.triggered.connect()

        edit_mmilitary_event = QAction('编辑部队事件', self)
        #edit_mmilitary_event.triggered.connect()

        add_new_person = QAction('制作新武将', self)
        #add_new_person.triggered.connect()

        add_new_title = QAction('制作新称号', self)
        #add_new_title.triggered.connect()

        self.statusBar()

        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu('文件')
        file_menu.addAction(open_save_file)
        file_menu.addAction(open_scenario_file)
        file_menu.addAction(save_button)
        file_menu.addAction(exit_button)

        edit_menu = menu_bar.addMenu('编辑')
        edit_menu.addAction(edit_person)
        edit_menu.addAction(edit_faction)
        edit_menu.addAction(edit_military)
        edit_menu.addAction(edit_achitecture)
        edit_menu.addAction(edit_facility)
        edit_menu.addAction(edit_treasure)
        edit_menu.addAction(edit_mmilitary_event)

        new_menu = menu_bar.addMenu('制作')
        new_menu.addAction(add_new_person)
        new_menu.addAction(add_new_title)

        self.setGeometry(300, 150, 800, 600)
        self.setWindowTitle('ZHSGZEditor')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())
