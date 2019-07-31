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
        self.series = None

    def setup_chart(self, count_x, count_y, show_axis_titles):

        # Setting X-axis
        axis_x = QtCharts.QValueAxis()
        axis_x.setTickCount(count_x)
        if show_axis_titles:
            axis_x.setTitleText("Time")

        self.addAxis(axis_x, Qt.AlignBottom)
        self.series.attachAxis(axis_x)

        # Setting Y-axis
        axis_y = QtCharts.QValueAxis()
        axis_y.setTickCount(count_y)
        if show_axis_titles:
            axis_y.setTitleText("Amplitude")

        self.addAxis(axis_y, Qt.AlignLeft)
        self.series.attachAxis(axis_y)

        if abs(axis_y.min()) > abs(axis_y.max()):
            axis_y.setMax(-axis_y.min())
        elif abs(axis_y.max()) > abs(axis_y.min()):
            axis_y.setMin(-axis_y.max())

    def addSeriesByProperties(self, rootNote, chord_id, volume, duration):

        framerate = 44100

        rootFreq = ChordUtil.fromIntToFreq(rootNote)
        freqs = ChordUtil.genFreqList(rootFreq, chord_id, volume, duration, framerate)

        self.series = QtCharts.QLineSeries()
        i = 0
        for freq in freqs:
            t = i / framerate
            self.series.append(t, freq)
            i += 1

        self.addSeries(self.series)

    def addSeriesByPoints(self, points):

        self.series = QtCharts.QLineSeries()
        self.series.append(points)

        self.addSeries(self.series)