import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QLineEdit, QVBoxLayout, QWidget, QHeaderView, \
    QHBoxLayout, QSizePolicy, QLabel
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtCore import Qt, QSortFilterProxyModel, pyqtSignal


class FilterProxyModel(QSortFilterProxyModel):
    filter_changed = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.filters = {}
        self.global_filter = ""

    def setFilter(self, column, pattern):
        if pattern:
            self.filters[column] = pattern
        else:
            self.filters.pop(column, None)
        self.invalidateFilter()
        self.filter_changed.emit()

    def setGlobalFilter(self, pattern):
        self.global_filter = pattern.lower()
        self.invalidateFilter()
        self.filter_changed.emit()

    def filterAcceptsRow(self, source_row, source_parent):
        model = self.sourceModel()

        # Columns to apply global filter on
        global_filter_columns = [2, 3, 6, 7]

        # Check the global filter first
        if self.global_filter:
            match_found = False
            for column in global_filter_columns:
                index = model.index(source_row, column, source_parent)
                data = model.data(index)
                if data is not None:
                    data_str = str(data).lower()
                    if self.global_filter in data_str:
                        match_found = True
                        break
            if not match_found:
                return False

        # Check the column-specific filters
        for column, pattern in self.filters.items():
            index = model.index(source_row, column, source_parent)
            data = model.data(index)
            if data is None:
                return False
            data_str = str(data).lower()
            if pattern.lower() not in data_str:
                return False

        return True


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle('Team Games')
        self.setGeometry(100, 100, 800, 600)

        # Set up the database connection
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('database.db')
        self.db.open()

        # Set up the table model
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('table_team_games')
        self.model.select()

        # Set up the filter proxy model
        self.proxy_model = FilterProxyModel(self)
        self.proxy_model.setSourceModel(self.model)
        self.proxy_model.filter_changed.connect(self.update_message_visibility)

        # Set up the table view
        self.view = QTableView()
        self.view.setModel(self.proxy_model)
        self.view.setSortingEnabled(True)  # Enable sorting

        # Hide the first column (assuming it's an ID column)
        self.view.setColumnHidden(0, True)

        # Set column names
        column_names = ['Dates', 'Player home', 'Team home', 'Home', 'Away', 'Player away', 'Team away']
        for col, name in enumerate(column_names, start=1):
            self.model.setHeaderData(col, Qt.Horizontal, name)

        # Set the header resize mode to stretch
        self.view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Set up the global filter layout
        self.global_filter_edit = QLineEdit(self)
        self.global_filter_edit.setPlaceholderText("Filter specific columns")
        self.global_filter_edit.textChanged.connect(self.proxy_model.setGlobalFilter)
        self.global_filter_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        global_filter_layout = QHBoxLayout()
        global_filter_layout.addWidget(self.global_filter_edit)

        # Set up the column-specific filter layout
        self.filter_layout = QHBoxLayout()
        self.filters = []
        for col in range(1, self.model.columnCount()):
            filter_edit = QLineEdit(self)
            filter_edit.setPlaceholderText(f"Filter {column_names[col - 1]}")
            filter_edit.textChanged.connect(lambda text, col=col: self.proxy_model.setFilter(col, text))
            filter_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
            self.filter_layout.addWidget(filter_edit)
            self.filters.append(filter_edit)

        # Set up the no data label
        self.no_data_label = QLabel("asdfasdfasdf")
        self.no_data_label.setAlignment(Qt.AlignCenter)
        self.no_data_label.setVisible(False)

        # Arrange the global filter, column-specific filters, table view, and no data label in a vertical layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(global_filter_layout)
        main_layout.addLayout(self.filter_layout)
        main_layout.addWidget(self.view)
        main_layout.addWidget(self.no_data_label)

        # Set up the central widget
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        # Connect the sectionResized signal to adjust the filter widths
        self.view.horizontalHeader().sectionResized.connect(self.update_filter_widths)

        # Initial update of filter widths
        self.update_filter_widths()
        self.update_message_visibility()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.update_filter_widths()

    def update_filter_widths(self):
        for col in range(1, self.model.columnCount()):
            width = self.view.columnWidth(col)
            self.filters[col - 1].setFixedWidth(width)
        self.global_filter_edit.setFixedWidth(self.view.width() - self.view.verticalScrollBar().width())

    def update_message_visibility(self):
        if self.proxy_model.rowCount() == 0:
            self.no_data_label.setVisible(True)
            self.view.setVisible(False)
        else:
            self.no_data_label.setVisible(False)
            self.view.setVisible(True)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
