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
        self.feedDataToSeries(series)

        self.addSeries(series)
        self.createDefaultAxes()

    def feedDataToSeries(self, series):
        data = ChordUtil.readWav()

        x = 0
        for value in data:
            series.append(x, value)
            x += 1



