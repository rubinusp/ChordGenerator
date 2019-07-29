# 1.Standard Modules

# 2. Extension Modules
from PySide2.QtWidgets import *
from PySide2.QtCharts import *

# 3. Local Modules
from ChordUtil import ChordUtil


class FreqSpectrum(QtCharts.QChart):

    def __init__(self, parent = None):

        super().__init__(parent)

        self.setAnimationOptions(QtCharts.QChart.AllAnimations)
        self.legend().hide()

        series = QtCharts.QLineSeries()
        #self.feedWavToSeries(series)

        self.addSeries(series)
        self.createDefaultAxes()

    def feedWavToSeries(self, series):
        data = ChordUtil.readWav()

        x = 0
        for value in data:
            series.append(x, value)
            x += 1

    def genSeriesByProperties(self, rootNote, chord_id, volume, duration):
        framerate = 44100

        freqs = ChordUtil.genFreqList(rootNote, chord_id, volume, duration, framerate)

        series = QtCharts.QLineSeries()
        t = 0
        for freq in freqs:
            series.append(t, freq)
            t += 1

        self.addSeries(series)
        self.createDefaultAxes()