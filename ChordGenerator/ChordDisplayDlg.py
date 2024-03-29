# 1.Standard Modules
import copy

# 2. Extension Modules
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtCharts import *

# 3. Local Modules
from chord_id import ChordID
from ChordUtil import ChordUtil
from FreqSpectrum import FreqSpectrum
from ChordFreqSpectrumDlg import ChordFreqSpectrumDlg


class ChordDisplayDlg(QDialog):

    def __init__(self, chord_id, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Chord displayer")
        self.resize(1000, 500)

        # Data Members
        self.chord_id = chord_id
        self.duration = 3
        self.framerate = 44100
        self.rootNote = 23
        self.volume = 50

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

        # Option Buttons
        self.viewBtn = None
        self.exportBtn = None
        self.resetBtn = None

        # Boxes
        self.propBox = None
        self.chordBox = None
        self.optButtonBox = None
        self.dlgButtonBox = None

        # Dialog
        self.chordFreqSpectrumDlg = None

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

        if self.chord_id == ChordID.MAJOR_7TH:
            self.chordList.setCurrentItem(self.major7th)
        elif self.chord_id == ChordID.MINOR_7TH:
            self.chordList.setCurrentItem(self.minor7th)
        elif self.chord_id == ChordID.DOMIN_7TH:
            self.chordList.setCurrentItem(self.domin7th)
        elif self.chord_id == ChordID.DIMIN_7TH:
            self.chordList.setCurrentItem(self.dimin7th)
        elif self.chord_id == ChordID.MAJOR_TRI:
            self.chordList.setCurrentItem(self.majorTri)
        elif self.chord_id == ChordID.MINOR_TRI:
            self.chordList.setCurrentItem(self.minorTri)
        elif self.chord_id == ChordID.AUGME_TRI:
            self.chordList.setCurrentItem(self.augmeTri)
        elif self.chord_id == ChordID.DIMIN_TRI:
            self.chordList.setCurrentItem(self.diminTri)

        self.chordList.currentItemChanged.connect(self.on_chord_changed)

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
        self.rootNoteSl.setTracking(False)
        self.rootNoteSl.valueChanged.connect(self.on_root_note_value_changed)
        self.rootNoteVal = QLabel("C4")

        volumeLabel = QLabel("Volume:")
        self.volumeSl = QSlider(Qt.Horizontal)
        self.volumeSl.setMinimum(0)
        self.volumeSl.setMaximum(100)
        self.volumeSl.setValue(50)
        self.volumeSl.setTracking(False)
        self.volumeSl.valueChanged.connect(self.on_volume_value_changed)
        self.volumeVal = QLabel("50")

        durationLabel = QLabel("Duration:")
        self.durationSl = QSlider(Qt.Horizontal)
        self.durationSl.setMinimum(0)
        self.durationSl.setMaximum(10)
        self.durationSl.setValue(3)
        self.durationSl.setTracking(False)
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
        freqs = ChordUtil.genSynthesizedChordFreqs(ChordUtil.fromIntToFreq(self.rootNote), self.chord_id, self.volume,
                                                   self.duration, self.framerate)
        self.spectrum.addChordSeriesByProperties(freqs, self.framerate)
        self.spectrum.setup_axis(10, 5, False)

        spectrum_view = QtCharts.QChartView(self.spectrum)

        # Setup option buttons
        self.viewBtn = QPushButton("View")
        self.viewBtn.clicked.connect(self.on_view_click)
        self.exportBtn = QPushButton("Export")
        self.exportBtn.clicked.connect(self.on_export_click)
        self.resetBtn = QPushButton("Reset")
        self.resetBtn.clicked.connect(self.on_reset_click)

        opt_button_layout = QHBoxLayout()
        opt_button_layout.addWidget(self.viewBtn)
        opt_button_layout.addWidget(self.exportBtn)
        opt_button_layout.addWidget(self.resetBtn)

        self.optButtonBox = QWidget()
        self.optButtonBox.setLayout(opt_button_layout)

        # Setup standard dialog buttons
        self.dlgButtonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal)

        self.dlgButtonBox.accepted.connect(self.on_okay_clicked)
        self.dlgButtonBox.rejected.connect(self.reject)

        # configure dialog layout
        main_layout = QGridLayout()
        main_layout.addWidget(self.chordBox, 0, 0)
        main_layout.addWidget(self.propBox, 0, 1)
        main_layout.addWidget(spectrum_view, 1, 0, 1, 2)
        main_layout.addWidget(self.optButtonBox, 2, 0)
        main_layout.addWidget(self.dlgButtonBox, 2, 1)

        # Set dialog layout
        self.setLayout(main_layout)

    def on_chord_changed(self):
        chord = self.chordList.currentItem()
        self.chord_id = ChordID.fromTextToChordId(chord.text())

        self.__redrawSeries()
        return

    def on_root_note_value_changed(self):

        val = self.rootNoteSl.value()
        self.rootNoteVal.setText(ChordUtil.fromIntToSPN(val))
        self.rootNote = val

        self.__redrawSeries()
        return

    def on_volume_value_changed(self):

        val = self.volumeSl.value()
        self.volumeVal.setText(str(val))
        self.volume = val

        self.__redrawSeries()
        return

    def on_duration_value_changed(self):
        val = self.durationSl.value()
        self.durationVal.setText(str(val))
        self.duration = val

        self.__redrawSeries()
        return

    def on_view_click(self):

        points = self.spectrum.chordSeries.points()
        self.chordFreqSpectrumDlg = ChordFreqSpectrumDlg(copy.deepcopy(points), self.chord_id,
                                                         self.duration, self.framerate, self.rootNote, self.volume,
                                                         self)
        self.chordFreqSpectrumDlg.show()

    def on_export_click(self):

        ChordUtil.exportChord(self.chord_id)

        msg = QMessageBox()
        msg.setText("The chord has been exported successfully.")
        msg.exec()
        return

    def on_reset_click(self):

        self.rootNoteSl.setValue(23)    # C4 frequency
        self.volumeSl.setValue(50)
        self.durationSl.setValue(3)
        return

    def on_okay_clicked(self):
        return

    def __redrawSeries(self):

        freqs = ChordUtil.genSynthesizedChordFreqs(ChordUtil.fromIntToFreq(self.rootNote), self.chord_id, self.volume,
                                                   self.duration, self.framerate)
        self.spectrum.addChordSeriesByProperties(freqs, self.framerate)
        return
