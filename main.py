# This Python file uses the following encoding: utf-8
import sys
import os
import datetime


from source.gpsModule.gpsModule import gpsModule
from source.arduino.ArduinoInput import ArduinoModule

from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QObject, Slot, Signal, QTimer


class MainWindow(QObject):

    def __init__(self):
        QObject.__init__(self)
        self.speed = "0"
        self.arduino_data = {}
        self.coordinatesFile = "./Logs/coordinates.csv"
#        self.gpsConnection = gpsModule.start_GPS_connection("/dev/ttyACM0")
        self.arduinoConnection = ArduinoModule().start_arduino_connection()


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
        except RuntimeError:
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
        except RuntimeError:
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
        except RuntimeError:
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
        except RuntimeError:
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
        except RuntimeError:
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
        except RuntimeError:
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
        except RuntimeError:
            pass

    def setBeam(self):
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
            beam = bool(self.arduino_data["Beam"])
            self.printBeam.emit(beam)
        except RuntimeError:
            pass

    def setBelts(self):
        """Return the state of the seatbelt light.

        Get data from "Arduino data", get the state of the
        seatbelt light(boolean) and connect it to the
        back end by using emit.
        """
        try:
            belts = bool(self.arduino_data["Bealts"])
            self.printBelts.emit(belts)
        except RuntimeError:
            pass

    def setBreak(self):
        """Return the state of the washer break light.

        Get data from "Arduino data", get the state of the
        break light(boolean) and connect it to the
        back end by using emit.
        """
        try:
            handBreak = bool(self.arduino_data["Break"])
            self.printBreak.emit(handBreak)
        except RuntimeError:
            pass

    def setBattery(self):
        """Return the state of the battery light.

        Get data from "Arduino data", get the state of the
        battery(boolean) and connect it to the
        back end by using emit. need to add something 
        The battery light will also come on when the car is crancking.
        """
       # need to check this on the actual cluster to see of it is an analog value or a bool
        try:
            battery = self.arduino_data["Charge"]
            self.printBattery.emit(battery)
        except RuntimeError:
            pass

    def setCheckHeat(self):
        """Return the state of the overheating light.

        Get data from "Arduino data", get the state of the
        overheating(boolean) and connect it to the
        back end by using emit.
        """
        try:
            checkHeat = bool(self.arduino_data["Cheack_Heat"])
            self.printCheckHeat.emit(checkHeat)
        except RuntimeError:
            pass
#

    def setTime(self):
        """Set the current time on the cluster.

        We use Hours - Minutes - Seconds,
        it is connected to the front end by using the
        emit method.
        """
        now = datetime.datetime.now()
        format = now.strftime("%H:%M:%S")
        self.printTime.emit(format)

    def setGauges(self):
        """Set the values for the gauges.

        Call the functions that pull the multiple data fields from
        the arduino.
        The fields being pulled update
        (RPM, Fuel, Oil Pressure, Battery Voltage)
        """
        try:
            new_arduino_data = ArduinoModule.read_from_arduino_connection(
                self.arduinoConnection, self.arduinoConnection)
            try:
                if isinstance(new_arduino_data, dict):
                    self.arduino_data = new_arduino_data
                    print(new_arduino_data)

            except RuntimeError:
                self.arduino_data = []
        except RuntimeError:
            pass

        self.setRPM()
        self.setTemperature()
        self.setFuelLevel()
        self.setOilPressure()
        self.setBatteryVolate()

    def setLights(self):
        """Refresh multiple lights at the sametime.

        Function calls the other function to update multiple warning lights.
        I used this so i didn't have to make and call seperate functions.
        The function is called multiple times persecond, so I don't think it
        would make a difference.
        """
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
            gpsModule.store_gps_data(self.gpsConnection, latitude, longitude, self.coordinatesFile)
        except RuntimeError:
            pass

        if gpsSpeed != "None":
            self.speed = gpsSpeed
        self.printMPH.emit(self.speed)

    def setRPM(self):
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
            rpm = str(self.arduino_data["Tack"])
            self.printRPM.emit(rpm)
        except RuntimeError:
            pass

    def setTemperature(self):
        """Return the value of the temperature sensors.

        Get data from "Arduino data", get the state of the
        temperature sensor(float) located by the thermostat
        and connect it to the front end by using emit.
        """
        try:
            temperature = str(self.arduino_data['Temp'])
            self.printEngineTemperature.emit(temperature)
        except RuntimeError:
            pass

    def setOilPressure(self):
        """Return the value of the oil pressure sensor.

        Get data from "Arduino data", get the value of the
        oil pressure sensor(float) and connect it to
        the front end by using emit.
        """
        try:
            oilPressure = str(self.arduino_data['Oil_Temp'])
            self.printOilPressure.emit(oilPressure)
        except RuntimeError:
            pass

    def setFuelLevel(self):
        """Return the value of the fuel level.

        Get data from "Arduino data", get the value of the
        the fuel level indicator (float) and connect it to
        the front end by using emit.
        """
        try:
            FuelLevel = (self.arduino_data['Fuel'])
            self.printFuelLevel.emit(FuelLevel)
        except RuntimeError:
            pass

    def setBatteryVolate(self):
        """Return the value of the battery voltage level.

        Get data from "Arduino data", get the value of the
        the battery voltage level (float) and connect it to
        the front end by using emit.
        """
        try:
            batteryVolatage = (self.arduino_data['Charge'])
            self.printBatteryVoltage.emit(batteryVolatage)
        except RuntimeError:
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
