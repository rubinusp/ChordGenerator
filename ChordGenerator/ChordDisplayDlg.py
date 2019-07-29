# 1.Standard Modules

# 2. Extension Modules
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtCharts import *

# 3. Local Modules
from ChordUtil import ChordUtil
from FreqSpectrum import FreqSpectrum


class ChordDisplayDlg(QDialog):

    def __init__(self, chord_id, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Chord displayer")
        self.resize(1000, 500)

        # Data Members
        self.rootNote = 23
        self.volume = 50
        self.duration = 3
        self.chord_id = chord_id

        ChordUtil.exportChord(self.chord_id)

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
        self.durationSl = None

        # Property Value Display
        self.rootNoteVal = None
        self.volumeVal = None
        self.durationVal = None

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
        self.rootNoteSl.setMaximum(51)  # C8 frequency
        self.rootNoteSl.setValue(23)    # C4 frequency
        self.rootNoteSl.valueChanged.connect(self.on_root_note_value_changed)
        self.rootNoteVal = QLabel("C4")

        volumeLabel = QLabel("Volume:")
        self.volumeSl = QSlider(Qt.Horizontal)
        self.volumeSl.setMinimum(0)
        self.volumeSl.setMaximum(100)
        self.volumeSl.setValue(50)
        self.volumeSl.valueChanged.connect(self.on_volume_value_changed)
        self.volumeVal = QLabel("50")

        durationLabel = QLabel("Duration:")
        self.durationSl = QSlider(Qt.Horizontal)
        self.durationSl.setMinimum(0)
        self.durationSl.setMaximum(10)
        self.durationSl.setValue(3)
        self.durationSl.valueChanged.connect(self.on_duration_value_changed)
        self.durationVal = QLabel("3")

        prop_layout = QGridLayout()
        prop_layout.addWidget(rootNoteLabel, 0, 0)
        prop_layout.addWidget(self.rootNoteSl, 0, 1)
        prop_layout.addWidget(self.rootNoteVal, 0, 2)
        prop_layout.addWidget(volumeLabel, 1, 0)
        prop_layout.addWidget(self.volumeSl, 1, 1)
        prop_layout.addWidget(self.volumeVal, 1, 2)
        prop_layout.addWidget(durationLabel, 2, 0)
        prop_layout.addWidget(self.durationSl, 2, 1)
        prop_layout.addWidget(self.durationVal, 2, 2)

        self.propBox = QGroupBox("Property")
        self.propBox.setLayout(prop_layout)

        # Setup frequency spectrum
        self.spectrum = FreqSpectrum()
        self.spectrum.genSeriesByProperties(self.rootNote, self.chord_id, self.volume, self.duration)

        spectrum_view = QtCharts.QChartView(self.spectrum)

        # Setup standard dialog buttons
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal)

        self.buttonBox.accepted.connect(self.on_okay_clicked)
        self.buttonBox.rejected.connect(self.reject)

        # configure dialog layout
        main_layout = QGridLayout()
        main_layout.addWidget(self.chordBox, 0, 0)
        main_layout.addWidget(self.propBox, 0, 1)
        main_layout.addWidget(spectrum_view, 1, 0, 1, 2)
        main_layout.addWidget(self.buttonBox, 2, 0, 1, 2)

        # Set dialog layout
        self.setLayout(main_layout)

    def on_root_note_value_changed(self):
        val = ChordUtil.fromIntToSPN(self.rootNoteSl.value())
        self.rootNoteVal.setText(val)

        return

    def on_volume_value_changed(self):
        val = str(self.volumeSl.value())
        self.volumeVal.setText(val)
        return

    def on_duration_value_changed(self):
        val = str(self.durationSl.value())
        self.durationVal.setText(val)
        return

    def on_okay_clicked(self):
        return