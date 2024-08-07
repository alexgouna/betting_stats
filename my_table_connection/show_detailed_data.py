import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Detailed Data')

        # # set vertical layout
        # self.setLayout(qtw.QVBoxLayout())

        # set layout
        layout_top = qtw.QFormLayout()
        self.setLayout(layout_top)

        # set top frame layout
        label_search=qtw.QLabel('Search :  ')
        label_search.setFont(qtg.QFont('',15))


        # set top frame search entry
        entry_search = qtw.QLineEdit(self)
        entry_search.setObjectName('Search')

        entry_search2 = qtw.QLineEdit(self)
        entry_search2.setObjectName('Search')

        layout_top.addRow(label_search,entry_search)
        layout_top.addRow('label_search', entry_search2)

        # appear items on top frame
        # self.layout().addWidget(label_search)
        # self.layout().addWidget(entry_search)















        self.show()



















def main():
    app = qtw.QApplication([])
    mw = MainWindow()
    app.exec_()


main()




