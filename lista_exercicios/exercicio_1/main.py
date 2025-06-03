import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from fatorial import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_Enviar.clicked.connect(self.exibir_fatorial)

    def exibir_fatorial(self):
            
            try:
                num = int(self.ui.lineEdit_input.text())
                
                if num > 1:
                    res = 1
                    for i in range(1, num + 1):
                        res *= i

                    self.ui.label_print.setText(f"O fatorial: {res}.")

                else:
                     self.ui.label_print.setText("Digite um número inteiro.")
                

            except ValueError:
                 self.ui.label_print.setText("Por favor. Digite um número inteiro.")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
