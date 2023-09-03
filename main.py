# This Python file uses the following encoding: utf-8
import sys
import os
import datetime


from source.gpsModule.gpsModule import gpsModule
from source.arduino.ArduinoInput import arduinoModule

from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QObject, Slot, Signal, QTimer


class MainWindow(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.speed = "0"
        self.arduino_data = {}
        self.coordinatesFile = "./Logs/coordinates.csv"
        self.gpsConnection = gpsModule.start_GPS_connection("/dev/ttyACM0")
        self.arduinoConnection = arduinoModule(
            "/dev/ttyACM1").start_arduino_connection()


#       Timer calls the defs that are part of thi class
        self.timer = QTimer()
        self.Atimer = QTimer()
        self.Btimer = QTimer()

        self.timer.timeout.connect(lambda: self.setMPH())
        self.Atimer.timeout.connect(lambda: self.setGauges())
        self.Btimer.timeout.connect(lambda: self.setLights())
        self.timer.start(150)
        self.Atimer.start(100)
        self.Btimer.start(200)

# Signals that will be picked up by GUI
    printTime = Signal(str)
    printMPH = Signal(str)
    printRPM = Signal(str)
    printEngineTemperature = Signal(str)
    printOilPressure = Signal(str)
    printFuelLevel = Signal(str)
    printBatteryVoltage = Signal(str)

    printLights = Signal(str)

    printTurnLeft = Signal(str)
    printTurnRight = Signal(str)
    printHold = Signal(str)
    printAirBag = Signal(str)
    printRetract = Signal(str)
    printABS = Signal(str)
    printWasher = Signal(str)
    printBeam = Signal(str)
    printBelts = Signal(str)
    printBreak = Signal(str)
    printBattery = Signal(str)
    printCheckHeat = Signal(str)

    def setTurnLeft(self):
        """Return the state of the left turn signal.

        Get data from "Arduino data", get the state of the
        left turn signal(boolean) and connect it to the
        back end by using emit.
        """
        try:
            turnLeft = bool(self.arduino_data["Turn_Left"])
            self.printTurnLeft.emit(turnLeft)
        except:
            pass

    def setTurnRight(self):
        """Return the state of the right turn signal.

        Get data from "Arduino data", get the state of the
        right turn signal(boolean) and connect it to the
        back end by using emit.
        """
        try:
            turnRight = bool(self.arduino_data["Turn_Right"])
            self.printTurnRight.emit(turnRight)
        except:
            pass

    def setHold(self):
        """Return the state of the hold light.

        Get data from "Arduino data", get the state of the
        hold light(boolean) and connect it to the
        back end by using emit.
        """
        try:
            hold = bool(self.arduino_data["Hold"])
            self.printHold.emit(hold)
        except:
            pass

    def setAirBag(self):
        """Return the state of the airbag light.

        Get data from "Arduino data", get the state of the
        airbag light(boolean) and connect it to the
        back end by using emit.
        """
        try:
            airBag = bool(self.arduino_data["Air_Bag"])
            self.printAirBag.emit(airBag)
        except:
            pass

    def setRetract(self):
        """Return the state of the retract light.

        Get data from "Arduino data", get the state of the
        retract light(boolean) and connect it to the
        back end by using emit.
        The retract light is for the pop-up lights.
        """
        try:

            retract = bool(self.arduino_data["Retract"])
            self.printRetract.emit(retract)
        except:
            pass

    def setABS(self):
        """Return the state of the ABS light.

        Get data from "Arduino data", get the state of the
        ABS light(boolean) and connect it to the
        back end by using emit.
        """
        try:
            ABS = bool(self.arduino_data["ABS"])
            self.printABS.emit(ABS)
        except:
            pass

    def setWasher(self):
        """Return the state of the washer fluid light.

        Get data from "Arduino data", get the state of the
        washer fluid light(boolean) and connect it to the
        back end by using emit.
        """
        try:
            washer = bool(self.arduino_data["Washer"])
            self.printWasher.emit(washer)
        except:
            pass

    def setBeam(self):
        """Return the state of the beam light.

        Get data from "Arduino data", get the state of the
        beam light(boolean) and connect it to the
        back end by using emit.
        The Beam light is for the brights, the pop-ups will also be on
        momenteraly while they are moving to popped up position.
        """
        try:
            beam = bool(self.arduino_data["Beam"])
            self.printBeam.emit(beam)
        except:
            pass

    def setBelts(self):
        try:
            belts = bool(self.arduino_data["Bealts"])
            self.printBelts.emit(belts)
        except:
            pass

    def setBreak(self):
        try:
            handBreak = bool(self.arduino_data["Break"])
            self.printBreak.emit(handBreak)
        except:
            pass

    def setBattery(self):
       # need to check this on the actual cluster to see of it is an analog value or a bool
        try:
            battery = self.arduino_data["Charge"]
            self.printBattery.emit(battery)
        except:
            pass

    def setCheckHeat(self):
        try:
            checkHeat = bool(self.arduino_data["Cheack_Heat"])
            self.printCheckHeat.emit(checkHeat)
        except:
            pass
#

    def setTime(self):
        now = datetime.datetime.now()
        format = now.strftime("%H:%M:%S")
        print(format)
        self.printTime.emit(format)

    def setGauges(self):
        new_arduino_data = arduinoModule.read_from_arduino_connection(
            self.arduinoConnection, self.arduinoConnection)
        if type(new_arduino_data) is dict:
            self.arduino_data = new_arduino_data
            print(new_arduino_data)
        self.setRPM()
        self.setTemperature()
        self.setFuelLevel()
        self.setOilPressure()
        self.setBatteryVolate()

    def setLights(self):
        self.setTurnLeft()
        self.setTurnRight()
        self.setHold()
        self.setAirBag()
        self.setRetract()
        self.setABS()
        self.setWasher()
        self.setBeam()
        self.setBelts()
        self.setBreak()
        self.setBattery()
        self.setCheckHeat()

    def setMPH(self):
        gpsData = gpsModule.clean_and_prep_data(
            self.gpsConnection, self.gpsConnection)
        gpsSpeed = str(gpsModule.get_speed(self.gpsConnection, gpsData))
        latitude = gpsModule.get_latitude(self.gpsConnection, gpsData)
        longitude = gpsModule.get_longitude(self.gpsConnection, gpsData)
        gpsModule.store_gps_data(
            self.gpsConnection, latitude, longitude, self.coordinatesFile)

        if gpsSpeed != "None":
            self.speed = gpsSpeed
        self.printMPH.emit(self.speed)

    def setRPM(self):
        try:
            rpm = str(self.arduino_data["Tack"])
            self.printRPM.emit(rpm)
        except:
            pass

    def setTemperature(self):
        try:
            temperature = str(self.arduino_data['Temp'])
            self.printEngineTemperature.emit(temperature)
        except:
            pass

    def setOilPressure(self):
        try:
            oilPressure = str(self.arduino_data['Oil_Temp'])
            self.printOilPressure.emit(oilPressure)
        except:
            pass

    def setFuelLevel(self):
        try:
            FuelLevel = (self.arduino_data['Fuel'])
            self.printFuelLevel.emit(FuelLevel)
        except:
            pass

    def setBatteryVolate(self):
        try:
            batteryVolatage = (self.arduino_data['Charge'])
            self.printBatteryVoltage.emit(batteryVolatage)
        except:
            pass


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    main = MainWindow()
    engine.rootContext().setContextProperty("backend", main)
    engine.load(os.path.join(os.path.dirname(__file__), "main.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
