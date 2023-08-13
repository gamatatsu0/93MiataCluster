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
        # Starting the arduino serial connection
        try:
            serialConnection = serial.Serial('/dev/ttyACM1', baudrate=115200)
            self.rawData = serialConnection

            return serialConnection
        #            serialConnection.reset_input_buffer()
        except:
            print("Arduino Serial Connection error")



    def read_from_arduino_connection(self,arduino):
        try:
            decotedData = arduino.readline().decode('utf-8')

            try:
                arduinoDataDict = json.loads(decotedData)
                if type(arduinoDataDict) is dict:
#                    print(arduinoDataDict)
#                    print(type(arduinoDataDict))
                    return arduinoDataDict

            except:
                print("Error convering to json")
                pass
        except:
            print("Error reading line from serial connection")
            pass

    def get_rpm(self,arduinoDict):
        try:
            print(self.jsonData["Tack"])
            return self.jsonData["Tack"]
        except:
            pass
    def get_fuel(self):
        try:
            return self.jsonData["Fuel"]
        except:
            pass

    def get_temp(self):
        try:
            return self.jsonData["Temp"]
        except:
            pass

    def get_batteru(self):
        try:
            return self.jsonData["Charge"]
        except:
            pass
