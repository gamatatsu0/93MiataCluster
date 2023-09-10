import json

import serial
from PySide6 import QtCore


# from queue import Queue


class ArduinoModule(QtCore.QObject):
    def __init__(self):
        self.raw_data = {}
        self.json_data = ''
        self.last_fuel = None
        self.last_temp = None

    def __str__(self):
        """ Return basic information about the class.

        Return basic explanation of what the function does.
        """
        return ("This class will interact with the arduino through serial" +
                "You will need to provide a serial port.")

    def start_arduino_connection(self):
        """Initiate serial connection with Arduino.

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
            serial_connection = serial.Serial('/dev/ttyACM0', baudrate=115200)
            self.raw_data = serial_connection

            return serial_connection
        #            serial_connection.reset_input_buffer()
        except RuntimeError:
            print("Arduino Serial Connection error")

    def read_from_arduino_connection(self, arduino):
        """Read data from the arduino.

        Function takes in a serial connection as input,
        and it will return a dictionary with the data from Arduino.
        Errors will be raised an error if we have trouble converting the
        data from JSON or converting it into a dictionary.
        """
        try:
            decoted_data = arduino.readline().decode('utf-8')

            try:
                arduino_data_dict = json.loads(decoted_data)
                if type(arduino_data_dict) is dict:
                    #                    print(arduino_data_dict)
                    #                    print(type(arduino_data_dict))
                    return arduino_data_dict

            except RuntimeError:
                print("Error convering to json")

        except RuntimeError:
            print("Error reading line from serial connection")

    def get_rpm(self, arduino_dict):
        """Get the RPM value.

        Function takes in    a dictionary as input,
        and it returns the tachometer value from
        the dictionary.
        """
        try:
            return self.json_data["Tack"]
        except RuntimeError:
            pass

    def get_fuel(self, arduino_dict):
        """Get the fuel value.

        Function takes in a dictionary as input.
        and it returns the fuel level value from
        the dictionary.
        The dictionary is a class property.
        """
        fuel = self.json_data["Fuel"]
        try:
            return fuel
        except RuntimeError:
            return self.last_fuel
        finally:
            self.last_fuel = fuel

    def get_temp(self, arduino_dict):
        """Get the temperature value.

        Function takes in a dictionary as input.
        and it returns the temperature level value from
        the dictionary.
        The dictionary is a class property.
        """
        temp = self.json_data["Temp"]
        try:
            return temp
        except RuntimeError:
            return self.last_temp
        finally:
            self.last_temp = temp

    def get_battery(self, arduino_dict):
        """Get the battery level value.

        Function takes in a dictionary as input.
        and it returns the battery level value from
        the dictionary.
        The dictionary is a class property.
        """
        try:
            return self.json_data["Charge"]
        except RuntimeError:
            pass
