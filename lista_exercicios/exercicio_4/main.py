import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from contagem import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_enviar.clicked.connect(self.exibir_contagem)

    def exibir_contagem(self):
        try:
            num = int(self.ui.lineEdit_input.text())
            resultado_texto = ""

            for i in reversed(range(num + 1)):
                resultado_texto += str(i) + "\n"

            self.ui.label_print.setText(resultado_texto)

        except ValueError:
            self.ui.label_print.setText("Por favor, digite um número inteiro.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

