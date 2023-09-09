from PySide6 import QtCore
import serial
import re
import json


# from queue import Queue


class arduinoModule(QtCore.QObject):
    def __init__(self,serialPort):
        self.rawData = ''
        self.jsonData = ''


    def __str__(self):
        return ("This class will interact with the arduino through serial. You will need to provide a serial port.")

    def start_arduino_connection(self):
        """ Initiate serial connection with Arduino.

        This method initiates a serial connection to the arduino
        connected.
        **Cinnection**
        * Baudrate = 115200
        * Connection = '/dev/ttyACM0'
        Takes no input.
        Return a serial connection.
        Does not update any global variables.
        """
        try:
            serialConnection = serial.Serial('/dev/ttyACM0', baudrate=115200)
            self.rawData = serialConnection

            return serialConnection
        #            serialConnection.reset_input_buffer()
        except RuntimeError:
            print("Arduino Serial Connection error")



    def read_from_arduino_connection(self,arduino):
        """ Read data from the arduino.

        Function takes in a serial connection as input,
        and it will return a dictionary with the data from Arduino.
        Errors will be raised an error if we have trouble converting the
        data from JSON or converting it into a dictionary.
        """
        try:
            decotedData = arduino.readline().decode('utf-8')

            try:
                arduinoDataDict = json.loads(decotedData)
                if type(arduinoDataDict) is dict:
#                    print(arduinoDataDict)
#                    print(type(arduinoDataDict))
                    return arduinoDataDict

            except RuntimeError:
                print("Error convering to json")
                pass
        except RuntimeError:
            print("Error reading line from serial connection")
            pass

    def get_rpm(self,arduinoDict):
        try:
            print(self.jsonData["Tack"])
            return self.jsonData["Tack"]
        except RuntimeError:
            pass
    def get_fuel(self):
        try:
            return self.jsonData["Fuel"]
        except RuntimeError:
            pass

    def get_temp(self):
        try:
            return self.jsonData["Temp"]
        except RuntimeError:
            pass

    def get_batteru(self):
        try:
            return self.jsonData["Charge"]
        except RuntimeError:
            pass
