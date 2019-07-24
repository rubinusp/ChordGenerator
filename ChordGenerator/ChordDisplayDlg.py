from PySide2.QtWidgets import *
from ChordUtil import ChordUtil


class ChordDisplayDlg(QDialog):

    def __init__(self, chord_id, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Chord displayer")
        self.resize(500, 500)

        self.clickedChord = chord_id
        ChordUtil.playChord(self.clickedChord)