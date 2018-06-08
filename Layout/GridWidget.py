from PyQt5.QtWidgets import QTableView
from PyQt5.QtCore import QAbstractItemModel

table_view = QTableView()


class GridView:

    def draw_grid(self, data):
        item_model = QAbstractItemModel()
        i = 0
        for key in data:
            item_model.setData(i, {key: data[key]})
        table_view.setModel(item_model)
        table_view.show()
