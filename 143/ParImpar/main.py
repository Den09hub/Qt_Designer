import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from par_impar import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_Enviar.clicked.connect(self.verificacaoNumero)

    def verificacaoNumero(self):
        num = int(self.ui.lineEdit_numero.text())

        calculo = num % 2

        if calculo == 1:
            self.ui.label_resposta.setText(f'O número é Impar')

        else:
            self.ui.label_resposta.setText(f'O número é Par')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())