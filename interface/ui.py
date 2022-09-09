
from PySide6 import QtCore, QtWidgets

from api.manage import *
#from interface.data import data
DEPARTAMENTOS = [
    "AMAZONAS",
    "VICHADA",
    "CAQUETA",
    "META",
    "GUAINIA",
    "ANTIOQUIA",
    "VAUPES",
    "GUAVIARE",
    "CHOCO",
    "CASANARE",
    "NARIÑO",
    "SANTANDER",
    "CAUCA",
    "BOLIVAR",
    "CORDOBA",
    "PUTUMAYO",
    "ARAUCA",
    "TOLIMA",
    "BOYACA",
    "MAGDALENA",
    "CESAR",
    "CUNDINAMARCA",
    "VALLE DEL CAUCA",
    "NORTE DE SANTANDER",
    "LA GUAJIRA",
    "HUILA",
    "SUCRE",
    "CALDAS",
    "RISARALDA",
    "ATLANTICO",
    "QUINDIO",
    "SAN ANDRES Y PROVIDENCIA",
]

class Windows(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # Distribution Windows
        self.layout = QtWidgets.QVBoxLayout(self)

        # Header group
        self.header = QtWidgets.QGroupBox("header")
        self.layout.addWidget(self.header)
        self.header_layout = QtWidgets.QHBoxLayout()
        self.header.setLayout(self.header_layout)

        # footer group
        self.body = QtWidgets.QGroupBox("body")
        self.layout.addWidget(self.body)
        self.body_layout = QtWidgets.QVBoxLayout()
        self.body.setLayout(self.body_layout)

        # texts
        self.text1 = QtWidgets.QLabel("Ejemplo", alignment=QtCore.Qt.AlignRight)
        self.text2 = QtWidgets.QLabel("Ejemplo2", alignment=QtCore.Qt.AlignCenter)

        # Input text
        self.input = QtWidgets.QLineEdit()
        self.input.setMaxLength(5)
        self.input.setPlaceholderText("numero de registros")
        self.input.returnPressed.connect(self.build_tables)

        # combo_box
        self.combo_box = QtWidgets.QComboBox()
        self.combo_box.addItems(DEPARTAMENTOS)

        # Table view
        self.table = QtWidgets.QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(
            ["Cuidad", "Departamento", "Edad", "Tipo", "Estado", "ubicacion","Fecha Reporte Web"]
        )

        # add to Header layout
        self.header_layout.addWidget(self.combo_box, alignment=QtCore.Qt.AlignLeft)
        self.header_layout.addWidget(self.input)
        self.header_layout.setAlignment(QtCore.Qt.AlignCenter)

        # add to body layout
        self.body_layout.addWidget(self.table)

        # self.input = QtWidgets.QInputDialog.getText()
        # self.button = QtWidgets.QPushButton("Click me!")
        # self.text = QtWidgets.QLabel("Hello World",
        #                              alignment=QtCore.Qt.AlignCenter)

        # self.layout = QtWidgets.QVBoxLayout(self)
        # self.layout.addWidget(self.text)
        # self.layout.addWidget(self.button)
        # self.layout.addWidget(self.input)

        # self.button.clicked.connect(self.magic)

    def build_tables(self):
        numero_de_registros = self.input.text()
        
        try: 
            numero_de_registros = int(numero_de_registros)
        except Exception:
            numero_de_registros = 0
            

        departamento = self.combo_box.currentData(0)
        print(f"{departamento} : {numero_de_registros}")
        
        data = get_information(departamento, numero_de_registros)

        self.table.setRowCount(len(data))
        
        print(data)

        for index,element in enumerate(data):
            cuidad = element['ciudad_municipio_nom'] if 'ciudad_municipio_nom' in element else "None"
            departamento_paciente = element['departamento_nom'] if 'departamento_nom' in element else "None"
            ubicacion = element['ubicacion'] if 'ubicacion' in element else "None"
            edad = element['edad'] if 'edad' in element else "None"
            tipo = element['tipo_recuperacion'] if 'tipo_recuperacion' in element else "None"
            estado = element['estado'] if 'estado' in element else "None"
            fecha_reporte_web = element['fecha_reporte_web'] if 'fecha_reporte_web' in element else "None"
            
            item_cuidad = QtWidgets.QTableWidgetItem(cuidad)
            item_departamento_paciente = QtWidgets.QTableWidgetItem(departamento_paciente)
            item_edad = QtWidgets.QTableWidgetItem(edad)
            item_tipo = QtWidgets.QTableWidgetItem(tipo)
            item_estado = QtWidgets.QTableWidgetItem(estado)
            item_ubicacion = QtWidgets.QTableWidgetItem(ubicacion)
            item_fecha_reporte_web = QtWidgets.QTableWidgetItem(fecha_reporte_web)
            
            self.table.setItem(index, 0, item_cuidad)
            self.table.setItem(index, 1, item_departamento_paciente)
            self.table.setItem(index, 2, item_edad)
            self.table.setItem(index, 3, item_tipo)
            self.table.setItem(index, 4, item_estado)
            self.table.setItem(index, 5, item_ubicacion)
            self.table.setItem(index, 6, item_fecha_reporte_web)

        self.table.show()
        


