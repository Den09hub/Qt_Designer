import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from idade_permitida import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_Enviar.clicked.connect(self.validar)

    def validar(self):
        idade = int(self.ui.lineEdit_idade.text())

        if idade >= 18:
            self.ui.label_resposta.setText(f"Validação: permitida")

        else:
            self.ui.label_resposta.setText(f"Validação: negada")

        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())