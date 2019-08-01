# 1.Standard Modules

# 2. Extension Modules
from PySide2.QtCore import *
from PySide2.QtCharts import *

# 3. Local Modules
from ChordUtil import ChordUtil


class FreqSpectrum(QtCharts.QChart):

    def __init__(self, parent = None):

        super().__init__(parent)

        self.setAnimationOptions(QtCharts.QChart.AllAnimations)
        self.legend().hide()

        # Components
        self.chordSeries = None

    def setup_chart(self, count_x, count_y, show_axis_titles):

        # Setting X-axis
        axis_x = QtCharts.QValueAxis()
        axis_x.setTickCount(count_x)
        if show_axis_titles:
            axis_x.setTitleText("Time")

        self.addAxis(axis_x, Qt.AlignBottom)
        self.chordSeries.attachAxis(axis_x)

        # Setting Y-axis
        axis_y = QtCharts.QValueAxis()
        axis_y.setTickCount(count_y)
        if show_axis_titles:
            axis_y.setTitleText("Amplitude")

        self.addAxis(axis_y, Qt.AlignLeft)
        self.chordSeries.attachAxis(axis_y)

        if abs(axis_y.min()) > abs(axis_y.max()):
            axis_y.setMax(-axis_y.min())
        elif abs(axis_y.max()) > abs(axis_y.min()):
            axis_y.setMin(-axis_y.max())

    def addChordSeriesByProperties(self, freqs, framerate):

        self.chordSeries = QtCharts.QLineSeries()
        self.chordSeries.setName("Chord")

        i = 0
        for freq in freqs:
            t = i / framerate
            self.chordSeries.append(t, freq)
            i += 1

        self.addSeries(self.chordSeries)

    def addChordSeriesByPoints(self, points):

        self.chordSeries = QtCharts.QLineSeries()
        self.chordSeries.setName("Chord")
        self.chordSeries.append(points)

        self.addSeries(self.chordSeries)

    def addNoteSeriesByProperties(self, name, freqs, framerate):

        noteSeries = QtCharts.QLineSeries()
        noteSeries.setName(name)

        i = 0
        for freq in freqs:
            t = i / framerate
            noteSeries.append(t, freq)
            i += 1

        self.addSeries(noteSeries)