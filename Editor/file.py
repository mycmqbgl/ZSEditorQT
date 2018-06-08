import configparser
import os
import json
from PyQt5.QtWidgets import QMessageBox

from Layout.GridWidget import GridView
from Model.save_data import SaveDataModel


save_data = SaveDataModel()


class FileView:
    def open_save_file(self, dialog):
        config = configparser.ConfigParser()
        config.read('Configuration', 'utf-8-sig')
        default_save_path = config.get('defaultPath', 'saveData')
        env_user_profile = os.environ.get("USERPROFILE")
        save_path = env_user_profile + default_save_path
        save_file_json, filetype = dialog.getOpenFileName(dialog,
                                                          "打开存档文件",
                                                          save_path if os.path.exists(save_path) else env_user_profile,
                                                          "Json Files (*.json)")
        if filetype != "Json Files (*.json)":
            alert = QMessageBox(QMessageBox.warning, "文件类型错误！", "请打开后缀名为.json的中华三国志存档文件")
            alert.show()
            return
        if save_file_json == '' or os.path.exists(save_path):
            alert = QMessageBox(QMessageBox.warning, "文件路径错误！", "请重新选择中华三国志存档文件")
            alert.show()
            return

        FileHandler.analyze_json(save_file_json)
        grid = GridView()
        grid.draw_grid(save_data)


class FileHandler:

    @staticmethod
    def analyze_json(file_path):
        json_file_str = open(file_path, encoding='utf-8').read()
        json_str = json.loads(json_file_str)
        save_data.__dict__ = json_str



