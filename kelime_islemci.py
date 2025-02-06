import os
import sys
from PyQt5 import QtWidgets

class kelime_islemci(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.yazi_alani = QtWidgets.QTextEdit()
        self.ac = QtWidgets.QPushButton("aç")
        self.kaydet = QtWidgets.QPushButton("kaydet")
        self.temizle = QtWidgets.QPushButton("temizle")
        self.cikis = QtWidgets.QPushButton("çıkış")
        
        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(self.ac)
        hbox.addWidget(self.kaydet)
        hbox.addWidget(self.temizle)
        hbox.addWidget(self.cikis)

        # vbox nesnesini oluşturduk ve doğru ismi kullandık
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.yazi_alani)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.setWindowTitle("Kelime İşlemci Programı")

        # Düğme tıklamaları bağlanıyor
        self.ac.clicked.connect(self.dosya_ac)
        self.kaydet.clicked.connect(self.dosya_kaydet)
        self.temizle.clicked.connect(self.yazi_sil)
        self.cikis.clicked.connect(self.cikis_yap)

        self.show()

    def dosya_ac(self):
        dosya, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Dosya Aç", os.getenv("HOME"))
        if dosya:
            with open(dosya, "r") as file:
                self.yazi_alani.setText(file.read())

    def dosya_kaydet(self):
        dosya, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Dosya Kaydet", os.getenv("HOME"))
        if dosya:
            with open(dosya, "w") as file:
                file.write(self.yazi_alani.toPlainText())

    def yazi_sil(self):
        self.yazi_alani.clear()

    def cikis_yap(self):
        QtWidgets.qApp.quit()

app = QtWidgets.QApplication(sys.argv)
kelimeislemci = kelime_islemci()
sys.exit(app.exec_())
