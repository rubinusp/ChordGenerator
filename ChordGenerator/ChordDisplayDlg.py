import sys
from PySide2.QtWidgets import *
from ChordUtil import ChordUtil

class ChordDisplayDlg(QDialog):

    def __init__(self, clickedChord, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Chord displayer")
        self.resize(500, 500)

        self.clickedChord = clickedChord

        print(clickedChord)
        chordUtil = ChordUtil()
        chordUtil.playChord(clickedChord)