# 1.Standard Modules
import sys

# 2. Extension Modules
from PySide2.QtWidgets import *

# 3. Local Modules
from ChordGenerator.ChordDisplayDlg import ChordDisplayDlg
from ChordGenerator.chord_id import ChordID

class ChordSelectDlg(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select chord")
        self.resize(200, 600)

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
        self.chordButtonGroup = QButtonGroup()
        self.chordButtonGroup.addButton(self.major_seventh, ChordID.MAJOR_SEVENTH)
        self.chordButtonGroup.addButton(self.minor_seventh, ChordID.MINOR_SEVENTH)
        self.chordButtonGroup.addButton(self.dominant_seventh, ChordID.DOMINANT_SEVENTH)
        self.chordButtonGroup.addButton(self.diminished_seventh, ChordID.DIMINISHED_SEVENTH)
        self.chordButtonGroup.addButton(self.major_triad, ChordID.MAJOR_TRIAD)
        self.chordButtonGroup.addButton(self.minor_triad, ChordID.MINOR_TRIAD)
        self.chordButtonGroup.addButton(self.augmented_triad, ChordID.AUGMENTED_TRIAD)
        self.chordButtonGroup.addButton(self.diminished_triad, ChordID.DIMINISHED_TRIAD)

        # TODO:: create a vertical layout which contain button group added into the main layout

        # Create standard button widgets
        self.okayButton = QPushButton("Okay")
        self.cancelButton = QPushButton("Cancel")

        layout = QHBoxLayout()
        layout.addWidget(self.okayButton)
        layout.addWidget(self.cancelButton)

        # Set dialog layout
        self.setLayout(layout)

        # Add button signal
        self.okayButton.clicked.connect(self.on_okay_button_clicked)
        self.cancelButton.clicked.connect(self.reject)

    def on_okay_button_clicked(self):
        self.hide()
        self.chordDisplayDlg = ChordDisplayDlg()
        self.chordDisplayDlg.show()

def main():

    app = QApplication(sys.argv)
    dlg = ChordSelectDlg()
    dlg.show()
    app.exec_()

if __name__ == "__main__":
    main()