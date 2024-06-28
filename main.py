import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt6.uic import loadUi
from PyQt6.QtCore import Qt
from pytube import YouTube
#Youtube Downloader#
#Autor: @PetusoTwo#
class YouTubeDownloader(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('Mp4ToMp3.ui', self)
        
        # borrar los iconos de maximizar, minimizar y cerrar
        # borrar la barra de titulo y los boprder blancos al aplicar los estilos
        
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint) 
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setWindowOpacity(5)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.in_convertir.clicked.connect(self.convertir_a_mp3)
        self.in_ruta.clicked.connect(self.elegir_ruta)
        self.in_close.clicked.connect(self.close)
        self.ruta = ''

#Metodo para poder elegir la ruta donde se descargara el archivo

    def elegir_ruta(self):
        self.ruta = QFileDialog.getExistingDirectory(self, "Elige la ruta")
        if self.ruta:
            QMessageBox.information(self, 'Ruta', f'Ruta seleccionada: {self.ruta}')
    
#Metodo para convertir el video a mp3

    def convertir_a_mp3(self):
        link = self.in_url.text()
        if not link:
            QMessageBox.warning(self, 'Error', 'Por favor ingresa un enlace válido')
            return
        if not self.ruta:
            QMessageBox.warning(self, 'Error', 'Por favor elige una ruta de destino')
            return
#Para los errores

        try:
            archivo_descargado = self.downloadMp3(link)
            self.in_url.clear()
            QMessageBox.information(self, 'Éxito', f'Archivo descargado: {archivo_descargado}')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Error al descargar: {e}')

#Script para descargar el mp3

    def downloadMp3(self, link):
        yt = YouTube(link)
        video = yt.streams.filter(only_audio=True).first()
        outFile = video.download(output_path=self.ruta)
        base, ext = os.path.splitext(outFile)
        new_file = base + '.mp3'
        os.rename(outFile, new_file)
        return new_file

if __name__ == '__main__':
    app = QApplication(sys.argv)
    downloader = YouTubeDownloader()
    downloader.show()
    sys.exit(app.exec())
#Autor: @PetusoTwo#