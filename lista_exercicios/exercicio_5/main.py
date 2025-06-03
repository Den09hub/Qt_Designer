import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from menor_maior_numero import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_enviar.clicked.connect(self.exibir_menor_maior)

    def exibir_menor_maior(self):
        try:
            armazenar_num = []

            num1 = int(self.ui.lineEdit_input_1.text())
            armazenar_num.append(num1)
            num2 = int(self.ui.lineEdit_input_2.text())
            armazenar_num.append(num2)
            num3 = int(self.ui.lineEdit_input_3.text())
            armazenar_num.append(num3)
            num4 = int(self.ui.lineEdit_input_4.text())
            armazenar_num.append(num4)
            num5 = int(self.ui.lineEdit_input_5.text())
            armazenar_num.append(num5)

            menor_num = str(min(armazenar_num))
            maior_num = str(max(armazenar_num))

            mensagem = f"O menor número é {menor_num}\nO maior número é {maior_num}"
            
            self.ui.label_print.setText(mensagem)
            

        except ValueError:
            self.ui.label_print.setText("Por favor, digite um número inteiro.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
