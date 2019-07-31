# 1.Standard Modules

# 2. Extension Modules
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtCharts import *

# 3. Local Modules
from FreqSpectrum import FreqSpectrum


class ChordFreqSpectrumDlg(QDialog):

    """ This class is to display the frequency spectrum of a particular chord in a separated dialog.

    It allows viewing features. """

    def __init__(self, points, parent = None):
        super().__init__(parent)

        self.setWindowTitle("Frequency spectrum")
        self.resize(1000, 800)

        # Components
        self.spectrum = None
        self.series = None
        self.axis_x = None
        self.axis_y = None

        self.setup_spectrum(points)

        self.setup_ui()

    def setup_spectrum(self, points):

        self.spectrum = FreqSpectrum()
        self.spectrum.addSeriesByPoints(points)
        self.spectrum.setup_chart(10, 9)

    def setup_ui(self):

        spectrum_view = QtCharts.QChartView(self.spectrum)

        main_layout = QVBoxLayout()
        main_layout.addWidget(spectrum_view)

        self.setLayout(main_layout)