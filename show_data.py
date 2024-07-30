import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QLineEdit, QVBoxLayout, QWidget, QHeaderView, QHBoxLayout
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtCore import Qt, QSortFilterProxyModel

class FilterProxyModel(QSortFilterProxyModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.filters = {}

    def setFilter(self, column, pattern):
        if pattern:
            self.filters[column] = pattern
        else:
            self.filters.pop(column, None)
        self.invalidateFilter()

    def filterAcceptsRow(self, source_row, source_parent):
        for column, pattern in self.filters.items():
            index = self.sourceModel().index(source_row, column, source_parent)
            if pattern.lower() not in self.sourceModel().data(index).lower():
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

        # Set up the filter layout
        self.filter_layout = QHBoxLayout()
        self.filters = []
        for col in range(1, self.model.columnCount()):
            filter_edit = QLineEdit(self)
            filter_edit.setPlaceholderText(f"Filter {column_names[col-1]}")
            filter_edit.textChanged.connect(lambda text, col=col: self.proxy_model.setFilter(col, text))
            self.filter_layout.addWidget(filter_edit)
            self.filters.append(filter_edit)

        # Arrange the filters and table view in a vertical layout
        layout = QVBoxLayout()
        layout.addLayout(self.filter_layout)
        layout.addWidget(self.view)

        # Set up the central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Connect the sectionResized signal to adjust the filter widths
        self.view.horizontalHeader().sectionResized.connect(self.update_filter_widths)

        # Initial update of filter widths
        self.update_filter_widths()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.update_filter_widths()

    def update_filter_widths(self):
        for col in range(1, self.model.columnCount()):
            width = self.view.columnWidth(col)
            self.filters[col-1].setFixedWidth(width)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
