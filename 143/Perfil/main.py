import sys
import webbrowser
from PyQt5.QtWidgets import QApplication, QMainWindow
from denyel import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_github.clicked.connect(self.abrir_github)
        self.ui.pushButton_instagram.clicked.connect(self.abrir_instagram)
        self.ui.pushButton_whatsapp.clicked.connect(self.abrir_whatsapp)

    def abrir_github(self):
        github_link = "https://github.com/"
        webbrowser.open(github_link)

    def abrir_instagram(self):
        instagram_link = "https://www.instagram.com/"
        webbrowser.open(instagram_link)

    def abrir_whatsapp(self):
        whatsapp_link = "https://wa.me/6799999-9999"
        webbrowser.open(whatsapp_link)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())