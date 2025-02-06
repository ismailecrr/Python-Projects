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
        self.ac.clicked.connect(self.dosya_ac)
        self.kaydet.clicked.connect(self.dosya_kaydet)
        self.temizle.clicked.connect(self.yizi_sil)
        self.cikis.clicked(self.cikis_yap)


        self.show()

    def dosya_ac(self):
        dosya=QtWidgets.QFileDialog.getOpenFileName(self,"dosya aç",os.getenv("desktop"))

        with open(dosya[0],"r") as file:
            self.yazi_alani.setText(file.read())
    
    def dosya_kaydet(self):
        dosya=QtWidgets.QFileDialog.getSaveFileName(self,"dosya kaydet",os.getenv("desktop"))
        with open(dosya[0],"w") as file:
            file.write(self.yazi_alani.toPlainText())

    def yazi_sil(self):
        self.yazi_alani.clear()

    def cikis_yap(self):
        quit() 



obje= QtWidgets.QApplication(sys.argv)
kelimeislemci = kelime_islemci()
sys.exit(app.exec_())




