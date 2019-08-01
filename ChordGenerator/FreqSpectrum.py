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
        self.axis_x = None
        self.axis_y = None

    def setup_axis(self, count_x, count_y, show_axis_titles):

        # Setting X-axis
        self.axis_x = QtCharts.QValueAxis()
        self.axis_x.setTickCount(count_x)
        if show_axis_titles:
            self.axis_x.setTitleText("Time")

        self.addAxis(self.axis_x, Qt.AlignBottom)
        self.chordSeries.attachAxis(self.axis_x)

        # Setting Y-axis
        self.axis_y = QtCharts.QValueAxis()
        self.axis_y.setTickCount(count_y)
        if show_axis_titles:
            self.axis_y.setTitleText("Amplitude")

        self.addAxis(self.axis_y, Qt.AlignLeft)
        self.chordSeries.attachAxis(self.axis_y)

        if abs(self.axis_y.min()) > abs(self.axis_y.max()):
            self.axis_y.setMax(-self.axis_y.min())
        elif abs(self.axis_y.max()) > abs(self.axis_y.min()):
            self.axis_y.setMin(-self.axis_y.max())

    def addChordSeriesByProperties(self, freqs, framerate):

        if self.chordSeries is None:
            # instantiate the chord series if it is the first time
            self.chordSeries = QtCharts.QLineSeries()
            self.chordSeries.setName("Chord")

            i = 0
            for freq in freqs:
                t = i / framerate
                self.chordSeries.append(t, freq)
                i += 1

            self.addSeries(self.chordSeries)
        else:
            # create QList for the points
            list = []
            i = 0
            for freq in freqs:
                t = i / framerate
                qPoint = QPointF(t, freq)
                list.append(qPoint)
                i += 1

            self.chordSeries.replace(list)

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