import sys
from PySide6 import QtCore, QtWidgets, QtGui
from interface.ui import Windows


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = Windows()
    widget.resize(1024, 756)
    widget.show()

    sys.exit(app.exec())