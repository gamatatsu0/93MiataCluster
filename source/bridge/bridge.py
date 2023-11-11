# This Python file uses the following encoding: utf-8
import sys
from pathlib import Path

from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine

#New Imports after download
from PySide6.QtCore import QObject, Slot
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, QmlElement
from PySide6.QtQuickControls2 import QQuickStyle


QML_IMPORT_NAME = "io.qt.textproperties"
QML_IMPORT_MAJOR_VERSION = 1


@QmlElement

# The bridge class is being used to connect the python
# backend to the QML Front end
class Bridge(QObject):

    @Slot(str, result=str)
    # Passing RPM worked
    def getRPM(self,rpm):
        return rpm # works

    @Slot(str, result=str)
    def getMPH(self,speed):
        return speed

    @Slot(bool, result=str)
    def getMPHorKM(self,mph):
        #True for MPH
        if  mph is True:
            return "MPH"
        else:
            return "KPH"

    @Slot(str, result=str)
    def getAverageSpeed(self,s):
        return "75"

    # tempretature
    @Slot(str, result=str)
    def getEngineTemperature(self,s):
        return s

    @Slot(str, result=str)
    def getAmbientTemp(self,s):
        return s

    @Slot(bool, result=str)
    def getCelciusorFarenheit(self,celsius = False):
        """Variable being passed is a boolean.

        If the variable is true the temperature
        will be in Celcius, otherwise it will Fahreheit.
        By default it will be false.
        """
        #True for Celcius
        if celsius is True:
            return "C"
        else:
            return "F"

    # Fuel
    @Slot(str, result=str)
    def getRange(self,s):
        return s

    @Slot(str, result=str)
    def getMPG(self,s):
        return s

    @Slot(str, result=str)
    def getTankLevel(self,s):
        return str(s)

    # Lights
    @Slot(bool, result=bool)
    def getHighBeam(self,s):
        return True

    @Slot(bool, result=bool)
    def getLowBeam(self,s):
        return s

    @Slot(bool, result=bool)
    def getPopUps(self,s):
        return True

    @Slot(bool, result=bool)
    def getLeftBlinker(self,s):
        return True

    @Slot(bool, result=bool)
    def getRightBlinker(self,s):
        return True
