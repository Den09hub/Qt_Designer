import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from numeros_naturais import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.exibir_numerosNaturais)

    def exibir_numerosNaturais(self):
        try:
            num = int(self.ui.lineEdit_input.text())
            if num > 0:
                somando_naturais = num * (num + 1) // 2
                self.ui.label_print.setText(f"A soma dos {num} números naturais é {somando_naturais}.")

            else:
                self.ui.label_print.setText("Digite um número inteiro positivo.")

        except ValueError:
            self.ui.label_print.setText("Entrada inváliada! Digite um número inteiro.")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())