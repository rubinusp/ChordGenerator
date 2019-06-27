# 1.Standard Modules
import sys

# 2. Extension Modules
from PySide2.QtWidgets import *
from PySide2.QtCore import *

# 3. Local Modules
from ChordGenerator.ChordDisplayDlg import ChordDisplayDlg
from ChordGenerator.chord_id import ChordID

class ChordSelectDlg(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select chord")

        # Create radio button widgets
        self.major_seventh = QRadioButton("Major Seventh")
        self.minor_seventh = QRadioButton("Minor Seventh")
        self.dominant_seventh = QRadioButton("Dominant Seventh")
        self.diminished_seventh = QRadioButton("Diminished Seventh")
        self.major_triad = QRadioButton("Major Triad")
        self.minor_triad = QRadioButton("Minor Triad")
        self.augmented_triad = QRadioButton("Augmented Triad")
        self.diminished_triad = QRadioButton("Diminished Triad")

        # Create Button Group for radio buttons
        chordLayout = QVBoxLayout()
        chordLayout.addWidget(self.major_seventh, ChordID.MAJOR_SEVENTH)
        chordLayout.addWidget(self.minor_seventh, ChordID.MINOR_SEVENTH)
        chordLayout.addWidget(self.dominant_seventh, ChordID.DOMINANT_SEVENTH)
        chordLayout.addWidget(self.diminished_seventh, ChordID.DIMINISHED_SEVENTH)
        chordLayout.addWidget(self.major_triad, ChordID.MAJOR_TRIAD)
        chordLayout.addWidget(self.minor_triad, ChordID.MINOR_TRIAD)
        chordLayout.addWidget(self.augmented_triad, ChordID.AUGMENTED_TRIAD)
        chordLayout.addWidget(self.diminished_triad, ChordID.DIMINISHED_TRIAD)

        # Create group box for chords
        self.chordBoxGroup = QGroupBox("Chord")
        self.chordBoxGroup.setLayout(chordLayout)

        # Create standard button box
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal)

        # Add button signal
        self.buttonBox.accepted.connect(self.on_okay_button_clicked)
        self.buttonBox.rejected.connect(self.reject)

        # configure dialog layout
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.chordBoxGroup)
        mainLayout.addWidget(self.buttonBox)

        # Set dialog layout
        self.setLayout(mainLayout)

        # TODO: disable okay button if no chord is selected initially

    def on_okay_button_clicked(self):
        self.hide()
        clickedChord = self.getClickedChordID()
        self.chordDisplayDlg = ChordDisplayDlg(clickedChord)
        self.chordDisplayDlg.show()

    def getClickedChordID(self):
        if self.major_seventh.isChecked():
            return ChordID.MAJOR_SEVENTH
        elif self.minor_seventh.isChecked():
            return ChordID.MINOR_SEVENTH
        elif self.dominant_seventh.isChecked():
            return ChordID.DOMINANT_SEVENTH
        elif self.diminished_seventh.isChecked():
            return ChordID.DIMINISHED_SEVENTH
        elif self.major_triad.isChecked():
            return ChordID.MAJOR_TRIAD
        elif self.minor_triad.isChecked():
            return ChordID.MINOR_TRIAD
        elif self.augmented_triad.isChecked():
            return ChordID.AUGMENTED_TRIAD
        else:
            return ChordID.DIMINISHED_TRIAD

def main():

    app = QApplication(sys.argv)
    dlg = ChordSelectDlg()
    dlg.show()
    app.exec_()

if __name__ == "__main__":
    main()