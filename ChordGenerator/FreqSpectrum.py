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

    def setup_chart(self, count_x, count_y):

        # Setting X-axis
        axis_x = QtCharts.QValueAxis()
        axis_x.setTickCount(count_x)
        self.addAxis(axis_x, Qt.AlignBottom)
        self.series.attachAxis(axis_x)

        # Setting Y-axis
        axis_y = QtCharts.QValueAxis()
        axis_y.setTickCount(count_y)
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
        t = 0
        for freq in freqs:
            self.series.append(t / framerate, freq)
            t += 1
            if t == 1000:
                break

        self.addSeries(self.series)

    def addSeriesByPoints(self, points):

        self.series = QtCharts.QLineSeries()
        self.series.append(points)

        self.addSeries(self.series)