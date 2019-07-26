# 1.Standard Modules

# 2. Extension Modules
from PySide2.QtWidgets import *
from PySide2.QtCore import *

# 3. Local Modules
from ChordUtil import ChordUtil


class ChordDisplayDlg(QDialog):

    def __init__(self, chord_id, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Chord displayer")
        self.resize(500, 500)

        self.clickedChord = chord_id
        ChordUtil.playChord(self.clickedChord)

        # Property
        self.rootNote = None
        self.volume = None

        # List Items For Scale
        self.major7th = None
        self.minor7th = None
        self.domin7th = None
        self.dimin7th = None
        self.majorTri = None
        self.minorTri = None
        self.augmeTri = None
        self.diminTri = None
        self.chordList = None

        # Property Slider
        self.rootNoteSl = None
        self.volumeSl = None

        # Frequency Spectrum Graph
        self.spectrum = None

        # Boxes
        self.propBox = None
        self.chordBox = None
        self.buttonBox = None

        self.setup_ui()

    def setup_ui(self):

        # Setup chord
        self.chordList = QListWidget()

        self.major7th = QListWidgetItem("Major Seventh", self.chordList)
        self.minor7th = QListWidgetItem("Minor Seventh", self.chordList)
        self.domin7th = QListWidgetItem("Dominant Seventh", self.chordList)
        self.dimin7th = QListWidgetItem("Diminished Seventh", self.chordList)
        self.majorTri = QListWidgetItem("Major Triad", self.chordList)
        self.minorTri = QListWidgetItem("Minor Triad", self.chordList)
        self.augmeTri = QListWidgetItem("Augmented Triad", self.chordList)
        self.diminTri = QListWidgetItem("Diminished Triad", self.chordList)

        chord_layout = QVBoxLayout()
        chord_layout.addWidget(self.chordList)

        self.chordBox = QGroupBox("Chord")
        self.chordBox.setLayout(chord_layout)

        # Setup property
        rootNoteLabel = QLabel("Root note:")
        self.rootNoteSl = QSlider(Qt.Horizontal)
        self.rootNoteSl.setMinimum(0)   # A0 frequency
        self.rootNoteSl.setMaximum(88)  # C8 frequency
        self.rootNoteSl.setValue(38)    # C4 frequency
        self.rootNoteSl.valueChanged.connect(self.on_root_note_value_changed)

        volumeLabel = QLabel("Volume:")
        self.volumeSl = QSlider(Qt.Horizontal)
        self.volumeSl.setMinimum(0)
        self.volumeSl.setMaximum(100)
        self.volumeSl.setValue(50)
        self.volumeSl.valueChanged.connect(self.on_volume_value_changed)

        prop_layout = QGridLayout()
        prop_layout.addWidget(rootNoteLabel, 0, 0)
        prop_layout.addWidget(self.rootNoteSl, 0, 1)
        prop_layout.addWidget(volumeLabel, 1, 0)
        prop_layout.addWidget(self.volumeSl, 1, 1)

        self.propBox = QGroupBox("Property")
        self.propBox.setLayout(prop_layout)

        # Setup standard dialog buttons
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal)

        self.buttonBox.accepted.connect(self.on_okay_clicked)
        self.buttonBox.rejected.connect(self.reject)

        # configure dialog layout
        main_layout = QGridLayout()
        main_layout.addWidget(self.chordBox, 0, 0)
        main_layout.addWidget(self.propBox, 0, 1)
        main_layout.addWidget(self.buttonBox, 1, 0, 1, 2)

        # Set dialog layout
        self.setLayout(main_layout)

    def on_root_note_value_changed(self):
        return

    def on_volume_value_changed(self):
        return

    def on_okay_clicked(self):
        return