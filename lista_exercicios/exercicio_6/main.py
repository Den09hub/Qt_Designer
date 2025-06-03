import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from numero_primo import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_enviar.clicked.connect(self.exibir_numero_primo)

    def exibir_numero_primo(self):
        try:
            num = int(self.ui.lineEdit_input.text())

            if num <= 1:
                self.ui.label_print.setText(f"{num} não é primo.")
            else:
                is_primo = True
                for i in range(2, num):
                    if num % i == 0:
                        is_primo = False
                        break

                if is_primo:
                    self.ui.label_print.setText(f"{num} é primo.")
                else:
                    self.ui.label_print.setText(f"{num} não é primo.")
        
        except ValueError:
            self.ui.label_print.setText("Por favor, digite um número inteiro.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
