# 1.Standard Modules

# 2. Extension Modules
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtCharts import *

# 3. Local Modules
from FreqSpectrum import FreqSpectrum
from ChordUtil import ChordUtil

class ChordFreqSpectrumDlg(QDialog):

    """ This class is to display the frequency spectrum of a particular chord in a separated dialog.

    It allows viewing features. """

    def __init__(self, points, chord_id, duration, framerate, rootNote, volume, parent = None):
        super().__init__(parent)

        self.setWindowTitle("Frequency spectrum")
        self.resize(1000, 800)

        # Components
        self.spectrum = None
        self.series = None
        self.axis_x = None
        self.axis_y = None

        # Data
        self.chord_id = chord_id
        self.duration = duration
        self.framerate = framerate
        self.rootNote = rootNote
        self.volume = volume

        self.setup_spectrum(points)

        self.setup_ui()

    def setup_spectrum(self, points):

        self.spectrum = FreqSpectrum()
        self.spectrum.addChordSeriesByPoints(points)

        freqsList = ChordUtil.genSingleNoteFreq(ChordUtil.fromIntToFreq(self.rootNote), self.chord_id, self.duration,
                                                self.framerate, self.volume)

        for name, freqs in zip(freqsList[0::2], freqsList[1::2]):
            self.spectrum.addNoteSeriesByProperties(name, freqs, self.framerate)

        self.spectrum.setup_chart(10, 9, True)
        self.spectrum.legend().show()

    def setup_ui(self):

        spectrum_view = QtCharts.QChartView(self.spectrum)
        spectrum_view.setRubberBand(QtCharts.QChartView.HorizontalRubberBand)

        main_layout = QVBoxLayout()
        main_layout.addWidget(spectrum_view)

        self.setLayout(main_layout)