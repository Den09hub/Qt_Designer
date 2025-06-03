import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from play_musica import Ui_MainWindow  

class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  
        self.ui.setupUi(self)

        self.player = QMediaPlayer(self)
        self.isPaused = False

        self.ui.pushButton_man.clicked.connect(self.play)
        self.ui.pushButton_invisible.clicked.connect(self.play)
        self.ui.pushButton_duvet.clicked.connect(self.play)
        self.ui.pushButton_eyes.clicked.connect(self.play)
        self.ui.pushButton_rises.clicked.connect(self.play)

        self.ui.pushButton_parar.clicked.connect(self.parar)

        self.ui.pushButton_pausar.clicked.connect(self.pausar)

        self.ui.horizontalSlider_volume.valueChanged.connect(self.controlar_volume)


    def play (self):
        botao = self.sender()

        if botao == self.ui.pushButton_man:
            caminho_musica = os.path.abspath("Musicas/song_man.mp3")
            print("Local da música:", caminho_musica)
        elif botao == self.ui.pushButton_invisible:
            caminho_musica = os.path.abspath("Musicas/song_invisible.mp3")
            print("Local da música:", caminho_musica)
        elif botao == self.ui.pushButton_duvet:
            caminho_musica = os.path.abspath("Musicas/song_duvet.mp3")
            print("Local da música:", caminho_musica)
        elif botao == self.ui.pushButton_eyes:
            caminho_musica = os.path.abspath("Musicas/song_eyes.mp3")
            print("Local da música:", caminho_musica)
        elif botao == self.ui.pushButton_rises:
            caminho_musica = os.path.abspath("Musicas/song_rises.mp3")
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
