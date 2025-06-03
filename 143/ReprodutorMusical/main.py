import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from play import Ui_MainWindow  

class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  
        self.ui.setupUi(self)

        self.player = QMediaPlayer(self)
        self.isPaused = False

        self.ui.pushButton_play1.clicked.connect(self.play)
        self.ui.pushButton_play2.clicked.connect(self.play)
        self.ui.pushButton_play3.clicked.connect(self.play)

        self.ui.pushButton_parar.clicked.connect(self.parar)

        self.ui.pushButton_pausar.clicked.connect(self.pausar)

        self.ui.horizontalSlider_volume.valueChanged.connect(self.controlar_volume)


    def play (self):
        botao = self.sender()

        if botao == self.ui.pushButton_play1:
            caminho_musica = os.path.abspath("Musicas/toque_zelda.mp3")
            print("Local da música:", caminho_musica)
        elif botao == self.ui.pushButton_play2:
            caminho_musica = os.path.abspath("Musicas/toque_souls.mp3")
            print("Local da música:", caminho_musica)
        elif botao == self.ui.pushButton_play3:
            caminho_musica = os.path.abspath("Musicas/toque_metal.mp3")
            print("Local da música:", caminho_musica)

        else:
            return "Inválido!"

        if self.isPaused:
            self.player.play()
            self.isPaused = False

        else:
            url = QUrl.fromLocalFile(caminho_musica)

            if url.isValid():
                self.player.setMedia(QMediaContent(url))
                self.player.play()
                print("Tocando música...")
            else:
                print("Erro: Caminho do arquivo inválido.")

    def parar (self):
        self.player.stop()
        self.isPaused = False
        print("A música parou!")

    def pausar (self):
        self.player.pause()
        self.isPaused = True
        print("A música está pausada!")

    def controlar_volume(self):
        volume = self.ui.horizontalSlider_volume.value()
        self.player.setVolume(volume)
        print(f"Volume ajustado para: {volume}")
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main()
    window.show()
    sys.exit(app.exec_())
