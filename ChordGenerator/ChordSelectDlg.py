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

        # Radio Button
        self.major7th = None
        self.minor7th = None
        self.domin7th = None
        self.dimin7th = None
        self.majorTri = None
        self.minorTri = None
        self.augmeTri = None
        self.diminTri = None

        # Boxes
        self.chordBox = None
        self.buttonBox = None

        # Next Dialog
        self.chordDisplayDlg = None

        self.setup_ui()

    def setup_ui(self):

        # Create radio button widgets
        self.major7th = QRadioButton("Major Seventh")
        self.minor7th = QRadioButton("Minor Seventh")
        self.domin7th = QRadioButton("Dominant Seventh")
        self.dimin7th = QRadioButton("Diminished Seventh")
        self.majorTri = QRadioButton("Major Triad")
        self.minorTri = QRadioButton("Minor Triad")
        self.augmeTri = QRadioButton("Augmented Triad")
        self.diminTri = QRadioButton("Diminished Triad")

        # Create Button Group for radio buttons
        chord_layout = QVBoxLayout()
        chord_layout.addWidget(self.major7th, ChordID.MAJOR_7TH)
        chord_layout.addWidget(self.minor7th, ChordID.MINOR_7TH)
        chord_layout.addWidget(self.domin7th, ChordID.DOMIN_7TH)
        chord_layout.addWidget(self.dimin7th, ChordID.DIMIN_7TH)
        chord_layout.addWidget(self.majorTri, ChordID.MAJOR_TRI)
        chord_layout.addWidget(self.minorTri, ChordID.MINOR_TRI)
        chord_layout.addWidget(self.augmeTri, ChordID.AUGME_TRI)
        chord_layout.addWidget(self.diminTri, ChordID.DIMIN_TRI)

        # Create group box for chords
        self.chordBox = QGroupBox("Chord")
        self.chordBox.setLayout(chord_layout)

        # Create standard button box
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal)

        # Add button signal
        self.buttonBox.accepted.connect(self.on_okay_clicked)
        self.buttonBox.rejected.connect(self.reject)

        # configure dialog layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.chordBox)
        main_layout.addWidget(self.buttonBox)

        # Set dialog layout
        self.setLayout(main_layout)

        # TODO: disable okay button if no chord is selected initially

    def on_okay_clicked(self):

        self.hide()

        chord_id = self.get_chord_id()
        self.chordDisplayDlg = ChordDisplayDlg(chord_id)
        self.chordDisplayDlg.show()

    def get_chord_id(self):

        if self.major7th.isChecked():
            return ChordID.MAJOR_7TH
        elif self.minor7th.isChecked():
            return ChordID.MINOR_7TH
        elif self.domin7th.isChecked():
            return ChordID.DOMIN_7TH
        elif self.dimin7th.isChecked():
            return ChordID.DIMIN_7TH
        elif self.majorTri.isChecked():
            return ChordID.MAJOR_TRI
        elif self.minorTri.isChecked():
            return ChordID.MINOR_TRI
        elif self.augmeTri.isChecked():
            return ChordID.AUGME_TRI
        else:
            return ChordID.DIMIN_TRI

def main():

    app = QApplication(sys.argv)
    dlg = ChordSelectDlg()
    dlg.show()
    app.exec_()

if __name__ == "__main__":
    main()