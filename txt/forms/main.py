import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from forms import Ui_MainWindow  

class FormularioApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        
        self.ui.pushButton_enviar.clicked.connect(self.enviar_dados)
        self.ui.pushButton_apagar.clicked.connect(self.apagar_campos)

    def enviar_dados(self):
        nome = self.ui.lineEdit_nome.text()
        sexo = "Masculino" if self.ui.radioButton_masc.isChecked() else "Feminino" if self.ui.radioButton_fem.isChecked() else "Não informado"
        aceite = "Sim" if self.ui.checkBox_termo.isChecked() else "Não"

        if not nome:
            QMessageBox.warning(self, "Atenção", "Por favor, preencha o nome.")
            return

        conteudo = f"Nome: {nome}\nSexo: {sexo}\nAceite: {aceite}"

        caminho = QFileDialog.getSaveFileName(self, "Salvar Arquivo", "", "Text Files (*.txt)")[0]
        if caminho:
            try:
                with open(caminho, 'w', encoding='utf-8') as f:
                    f.write(conteudo)
                QMessageBox.information(self, "Sucesso", "Dados salvos com sucesso!")
            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Erro ao salvar arquivo:\n{str(e)}")

    def apagar_campos(self):
        self.ui.lineEdit_nome.clear()
        self.ui.radioButton_masc.setChecked(False)
        self.ui.radioButton_fem.setChecked(False)
        self.ui.checkBox_termo.setChecked(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormularioApp()
    window.show()
    sys.exit(app.exec_()) 
