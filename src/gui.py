import sys
import musicVisualizers
from PyQt5.QtWidgets import *


"""
Desc: Main window for GUI application.
"""
class GUIMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RR Music Visualizer")
        self.setCentralWidget(GUIMain())
        self.show()


"""
Desc: Main GUI widget for importing music file and selecting visualizer method.
"""
class GUIMain(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        # Audio File Widgets
        self.btn = QPushButton("Import audio file")
        self.btn.clicked.connect(self.getFile)	
        self.layout.addWidget(self.btn)

        # Visualizer Method Widgets
        self.layout.addWidget(QLabel('Select a visualizer method:'))
        self.custom1 = QRadioButton("Custom1")
        self.layout.addWidget(self.custom1)

        self.custom2 = QRadioButton("Custom2")
        self.layout.addWidget(self.custom2)

        self.custom3 = QRadioButton("Custom3")
        self.layout.addWidget(self.custom3)

        # Visualizer Generation Widgets
        self.generate = QPushButton("Generate")
        self.generate.clicked.connect(self.generateVisual)
        self.layout.addWidget(self.generate)

        self.setLayout(self.layout)
        self.show()


"""
Desc: Checks which music visualization method is selected.
"""
    def checkSelection(self):
        if self.custom1.isChecked():
            musicVisualizers.custom1()
        elif self.custom2.isChecked():
            musicVisualizers.custom2()
        elif self.custom3.isChecked():
            musicVisualizers.custom3()

"""
Desc: Calls music visualization method based on user selection.
"""
    def generateVisual(self):
        self.checkSelection()


"""
Desc: Opens file dialog menu to select audio file.
"""
    def getFile(self):
        self.fname = QFileDialog.getOpenFileName(self, 'Open file', 
         'c:\\',"Audio Files (*.mp3 *.wav)")


def main():
    app = QApplication([])
    gui = GUIMainWindow()
    app.exec()

if __name__ == "__main__":
    main()
