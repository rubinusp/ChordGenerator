# 1.Standard Modules

# 2. Extension Modules
from PySide2.QtWidgets import *
from PySide2.QtCharts import *

# 3. Local Modules


class FreqSpectrum:

    def __init__(self):

        self.chart = QtCharts.QChart()
        self.chart.setAnimationOptions(QtCharts.QChart.AllAnimations)

        series = QtCharts.QSplineSeries()

