# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial

import sys
from pathlib import Path
import datetime

from PySide6.QtCore import QObject, Slot
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, QmlElement
from PySide6.QtQuickControls2 import QQuickStyle


from source.gpsModule.gpsModule import gpsModule
from source.arduino.ArduinoInput import ArduinoModule
from source.helpers.Milage import FuelEfficiency

# To be used on the @QmlElement decorator
# (QML_IMPORT_MINOR_VERSION is optional)
QML_IMPORT_NAME = "io.qt.textproperties"
QML_IMPORT_MAJOR_VERSION = 1


@QmlElement
class Bridge(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.speed = "0"
        self.arduino_data = {}
        self.coordinatesFile = "./Logs/coordinates.csv"
#        self.gpsConnection = gpsModule.start_GPS_connection("/dev/ttyACM0")
        self.arduinoConnection = ArduinoModule().start_arduino_connection()
        self.fuelEffient = FuelEfficiency()
        self.listOfWarnings = []

    @Slot(str, result=str)
    def setGauges(self, s):
        try:
            new_arduino_data = ArduinoModule.read_from_arduino_connection(
                self.arduinoConnection, self.arduinoConnection)
            if type(new_arduino_data) is dict:
                self.arduino_data = new_arduino_data
                print(new_arduino_data)
        except:
            print("It failed")
            pass

    @Slot(str, result=bool)
    def setTurnLeft(self, s):
        print(s)
        # self.setGauges("s")
        """Return the state of the left turn signal.

          Get data from "Arduino data", get the state of the
          left turn signal(boolean) and connect it to the
          back end by using emit.
        """
        try:
            turnLeft = bool(self.arduino_data['Turn_Left'])
            return turnLeft

        except RuntimeError:
            pass

    @Slot(str, result=bool)
    def setTurnRight(self, s):
        # self.setGauges("s")
        """Return the state of the right turn signal.

          Get data from "Arduino data", get the state of the
          right turn signal(boolean) and connect it to the
          back end by using emit.
        """
        try:
            turnRight = bool(self.arduino_data['Turn_Right'])
            return turnRight

        except RuntimeError:
            pass

    @Slot(str, result=bool)
    def setHold(self, s):
        # self.setGauges("s")
        """Return the state of the hold light.

          Get data from "Arduino data", get the state of the
          hold light(boolean) and connect it to the
          back end by using emit.
        """
        try:
            hold = bool(self.arduino_data['Hold'])
            return hold

        except RuntimeError:
            pass

    @Slot(str, result=bool)
    def setAirBag(self, s):
        # self.setGauges("s")
        """Return the state of the airbag light.

            Get data from "Arduino data", get the state of the
            airbag light(boolean) and connect it to the
            back end by using emit.
        """
        try:
            airBag = bool(self.arduino_data['Air_Bag'])
            return airBag

        except RuntimeError:
            pass

    @Slot(str, result=bool)
    def setHazard(self, s):
        # self.setGauges("s")
        """Return the state of the airbag light.

    Get data from "Arduino data", get the state of the
    airbag light(boolean) and connect it to the
    back end by using emit.
    """
        try:
            airBag = bool(self.arduino_data['Air_Bag'])
            return airBag

        except RuntimeError:
            pass

    @Slot(str, result=bool)
    def setRetract(self, s):
        # self.setGauges("s")
        """Return the state of the retract light.

          Get data from "Arduino data", get the state of the
          retract light(boolean) and connect it to the
          back end by using emit.
          The retract light is for the pop-up lights.
        """
        try:
            retract = bool(self.arduino_data['Retract'])
            return retract

        except RuntimeError:
            pass

    @Slot(str, result=bool)
    def setABS(self, s):
        # self.setGauges("s")
        """Return the state of the ABS light.

          Get data from "Arduino data", get the state of the
          ABS light(boolean) and connect it to the
          back end by using emit.
        """
        try:
            ABS = bool(self.arduino_data['ABS'])
            return ABS

        except RuntimeError:
            pass

    @Slot(str, result=bool)
    def setWasher(self, s):
        # self.setGauges("s")
        """Return the state of the washer fluid light.

          Get data from "Arduino data", get the state of the
          washer fluid light(boolean) and connect it to the
          back end by using emit.
        """
        try:
            washer = bool(self.arduino_data['Washer'])
            return washer

        except RuntimeError:
            pass

    @Slot(str, result=bool)
    def setBeam(self, s):
        # self.setGauges("s")
        """Return the state of the beam light.

          Get data from "Arduino data", get the state of the
          beam light(boolean) and connect it to the
          back end by using emit.
          The Beam light is for the brights, the pop-ups will also be on
          momenteraly while they are moving to popped up position.
          If the regular lights are not on but the high beams are, than the
          highbeams will not work.
        """
        try:
            beam = bool(self.arduino_data['Beam'])
            return beam

        except RuntimeError:
            pass

    @Slot(str, result=bool)
    def setBelts(self, s):
        # self.setGauges("s")
        """Return the state of the seatbelt light.

          Get data from "Arduino data", get the state of the
          seatbelt light(boolean) and connect it to the
          back end by using emit.
          """
        try:
            belts = bool(self.arduino_data['Bealts'])
            return belts

        except RuntimeError:
            pass

    @Slot(str, result=bool)
    def setBreak(self, s):
        # self.setGauges("s")
        """Return the state of the washer break light.

          Get data from "Arduino data", get the state of the
          break light(boolean) and connect it to the
          back end by using emit.
          """
        try:
            handBreak = bool(self.arduino_data['Break'])
            return handBreak

        except RuntimeError:
            pass

    @Slot(str, result=bool)
    def setBattery(self, s):
        # self.setGauges("s")
        """Return the state of the battery light.

          Get data from "Arduino data", get the state of the
          battery(boolean) and connect it to the
          back end by using emit. need to add something
          The battery light will also come on when the car is crancking.
          """
        # need to check this on the actual cluster to see of it is an analog value or a bool
        try:
            battery = self.arduino_data['Charge']
            return battery

        except RuntimeError:
            pass

    @Slot(str, result=bool)
    def setCheckHeat(self, s):
        # self.setGauges("s")
        """Return the state of the overheating light.

          Get data from "Arduino data", get the state of the
          overheating(boolean) and connect it to the
          back end by using emit.
          """
        try:
            checkHeat = bool(self.arduino_data["Check_Heat"])
            return checkHeat

        except RuntimeError:
            pass
  #

    @Slot(str, result=str)
    def setTime(self, s):
        # self.setGauges("s")
        """Set the current time on the cluster.

          We use Hours - Minutes - Seconds,
          it is connected to the front end by using the
          emit method.
          """
        now = datetime.datetime.now()
        formated = now.strftime("%H:%M:%S")
        return formated

    @Slot(str, result=str)
    def setMPH(self, s):
        # self.setGauges("s")
        """Set the current time on the cluster.

        We use Hours - Minutes - Seconds,
        it is connected to the front end by using the
        emit method.
        *
        Also updating the the information derived from the GPS
        at the sae time as the clock since the PGS data is a little slow
        to propagate due to multiple GPS sentances. (ABout once per second)
        """
        try:
            gpsData = gpsModule.clean_and_prep_data(
                self.gpsConnection, self.gpsConnection)
        except RuntimeError:
            pass

        try:
            gpsSpeed = str(gpsModule.get_speed(self.gpsConnection, gpsData))
        except RuntimeError:
            pass

        try:
            latitude = gpsModule.get_latitude(self.gpsConnection, gpsData)
        except RuntimeError:
            pass

        try:
            longitude = gpsModule.get_longitude(self.gpsConnection, gpsData)
        except RuntimeError:
            pass

        try:
            gpsModule.store_gps_data(
                self.gpsConnection, latitude, longitude, self.coordinatesFile)
        except RuntimeError:
            pass

        if gpsSpeed != "None":
            self.speed = gpsSpeed

    @Slot(str, result=str)
    def setRPM(self, s):
        # self.setGauges("s")
        """Set the the value of the RPM.

        Get data from "Arduino data", get the value of the
        signal form the Tackometer(Float) and connect it to the
        front end by using emit.
        There may be some noise in the tachometer reading since cars
        are natural noisy systems.
        *
        The Tachometer reading comes from the coil pack when each
        sparkplug fires.
        The signal that the arduino receives is a quarewave.
        """
        try:
            rpm = str(self.arduino_data['Tack'])
            return rpm

        except RuntimeError:
            pass

    @Slot(str, result=str)
    def setTemperature(self, s):
        # self.setGauges("s")
        """Return the value of the temperature sensors.

        Get data from "Arduino data", get the state of the
        temperature sensor(float) located by the thermostat
        and connect it to the front end by using emit.
        """
        try:
            temperature = str(self.arduino_data['Temp'])
            return temperature

        except RuntimeError:
            pass

    @Slot(str, result=int)
    def setFuelLevel(self, s):
        # self.setGauges("s")
        """Return the value of the fuel level.

        Get data from "Arduino data", get the value of the
        the fuel level indicator (float) and connect it to
        the front end by using emit.
        """
        FuelLevel = int(self.arduino_data['Fuel'])
        gallons = self.fuelEffient.convertPercentToGallons(FuelLevel)
        self.fuelEffient.setCurrentGallons(gallons)
        return FuelLevel
#        print(FuelLevel)

    @Slot(str, result=str)
    def setBatteryVolate(self, s):
        # self.setGauges("s")
        """Return the value of the battery voltage level.

        Get data from "Arduino data", get the value of the
        the battery voltage level (float) and connect it to
        the front end by using emit.
        """
        try:
            return (self.arduino_data['Charge'])

        except RuntimeError:
            pass

        def getUnderline(self, s):
            if s.lower() == "underline":
                return True
            else:
                return False

    @Slot(str, result=str)
    def setOilPressure(self, s):
        # self.setGauges("s")
        # print("SSS")
        """Return the value of the oil pressure sensor.

            Get data from "Arduino data", get the value of the
            oil pressure sensor(float) and connect it to
            the front end by using emit.
            """
        try:
            oilPressure = str(self.arduino_data['Oil_psi'])
            return oilPressure
        except RuntimeError:
            pass

    @Slot(str, result=bool)
    def setOilLight(self, s):
        # self.setGauges("s")
        try:
            oilPressure = str(self.arduino_data['Oil_psi'])
            if oilPressure > "95":
                return True
            else:
                False
        except RuntimeError:
            pass

    @Slot(str, result=bool)
    def setFuelLight(self, s):
        # self.setGauges("s")
        return True


    @Slot(str, result=str)
    def setListOfWarnings(self, s):
        # self.setGauges("s")
        # print("SSS")
        """
            """
        try:
            if(len(self.listOfWarnings) != 0):
                return self.listOfWarnings
            else:
                pass
        except RuntimeError:
            pass
# ============== For stuff that needs to be calculated ==============
    @Slot(str, result=int)
    def setAmbientTemperature(self, s):
        # self.setGauges("s")
        return "69"

    @Slot(int, result=int)
    def setAverageSpeed(self, s):
        # self.setGauges("s")
        return "69"

    @Slot(str, result=int)
    def setBatteryVoltage(self, s):
        # self.setGauges("s")
        return "69"

    @Slot(str, result=int)
    def setFuelRange(self, s):
        return self.fuelEffient.getMilesTilEmpty()

    @Slot(str, result=int)
    def setAverageMPG(self, s):
        # self.setGauges("s")
        return "69"

    @Slot(str, result=int)
    def setInteriorTemperature(self, s):
        # self.setGauges("s")
        return "69"

#    @Slot(str, result=str)
#    def setAmbientTemperature(self,s):
#        return "69"


if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    QQuickStyle.setStyle("Material")
    engine = QQmlApplicationEngine()

    # Get the path of the current directory, and then add the name
    # of the QML file, to load it.
    qml_file = Path(__file__).parent / 'main.qml'
    engine.load(qml_file)

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())
