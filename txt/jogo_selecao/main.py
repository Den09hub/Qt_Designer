import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from selecao import Ui_MainWindow

class FormularioApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_salvar.clicked.connect(self.salvar_dados)

    def salvar_dados(self):
        nome_completo = self.ui.lineEdit_nome_completo.text()
        nome_usuario = self.ui.lineEdit_nome_usuario.text()
        idade = self.ui.lineEdit_nome_usuario.text()
        email = self.ui.lineEdit_nome_usuario.text()
        senha = self.ui.lineEdit_nome_usuario.text()
        personagem = "Scorpion" if self.ui.radioButton_scorpion.isChecked() else "Sub-Zero" if self.ui.radioButton_sub.isChecked() else "Kitana" if self.ui.radioButton_kitana.isChecked() else "Milena" if self.ui.radioButton_milena.isChecked() else "Boss" if self.ui.radioButton_secreto.isChecked() else "Não informado"

        if not (nome_completo and nome_usuario) and ((idade and email) and senha):
            QMessageBox.warning(self, "Atenção", "Por favor, preencha o nome.")
            return

        conteudo = f"Nome Completo: {nome_completo}\nNome de Usuário: {nome_usuario}\nIdade: {idade}\nE-mail: {email}\nSenha: {senha}"

        caminho = QFileDialog.getSaveFileName(self, "Salvar Arquivo", "", "Text Files (*.txt)")[0]
        if caminho:
            try:
                with open(caminho, 'w', encoding='utf-8') as f:
                    f.write(conteudo)
                QMessageBox.information(self, "Sucesso", "Dados salvos com sucesso!")
            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Erro ao salvar arquivo:\n{str(e)}")

    def apagar_campos(self):
        self.ui.lineEdit_nome_completo.clear()
        self.ui.lineEdit_nome_usuario.clear()
        self.ui.lineEdit_idade.clear()
        self.ui.lineEdit_email.clear()
        self.ui.lineEdit_senha.clear()
        self.ui.radioButton_scorpion.setChecked(False)
        self.ui.radioButton_sub.setChecked(False)
        self.ui.radioButton_kitana.setChecked(False)
        self.ui.radioButton_milena.setChecked(False)
        self.ui.radioButton_secreto.setChecked(False)
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormularioApp()
    window.show()
    sys.exit(app.exec_())