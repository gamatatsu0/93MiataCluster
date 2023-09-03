# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
import serial
import csv


class gpsModule(QtCore.QObject):
    """Connect and get information from the GPS module.

    Class is meant to connect and manage GPS data.
    We get multiple fields of data from the GPS module
    in the form of GPS sentences.
    """
    def __init__(self,serialPort):
        """ Create variable for use of GPS data and serial conn.

        We need to use this properties as global varibles to update
        the serial connection and the data that comes GPS module.
        """
        self.serialPort = serialPort
        self.serialConnection =None
        self.gpsData = ""
    def __str__(self):
        """ Print out message about the serial port used.

        Displays message when the class initiates.
        """
        return f"The port '{self.serialPort}' was provided for serial communication with GPS module. Select actions you need to take"
    # ...................... Starting the GPS connection ......................
    def start_GPS_connection(self):
        """Start the connection to the gps module.

        This function takes in no parameters and
        start the connection to the GPS module.
        """
        try:
            print("Connecting to GPS antenna ....")

            serial_connection = serial.Serial('/dev/ttyACM1', baudrate=9600)
            return serial_connection
        except RuntimeError:
            print("GPS Serial connection error")
    # ...................... Conversions ......................

    def meter_to_feet(self, meters):
        """Coverting meters to feet.

        Takes in the a numerical value for meters,
        and it will return the equivalent of meters to feet.
        """
        # One meter is 3.28084 feet
        return int(meters) * 3.28084

    def knots_to_miles(self, knots):
        """Converts Knotts to miles.

        Takes in the current speed in knotts as a parameter
        return the speed in miles.
        One knot is 1.68781 Miles.
        print (knots * 2).
        """
        return float(knots * 1.68781)

    def clean_and_prep_data(self, gps):
        """Convert data to UTF-8 and separate by comas.

        # when at a complete stop the gps reads between 0.0. and 0.04 MPH
        # adjust to hink it is qithin 0.000
        """
        try:
            ser_bytes = gps.readline()
            decoded_bytes = ser_bytes.decode("UTF-8")
            return decoded_bytes.split(",")
        except RuntimeError:
            pass



    # ...................... Getting Data ......................
    def get_speed(self, gps_data):
        """ Requires GPRMC sentence.

        We ge the data from the GPS sentence and convert it.
        The data GPS sentance is passed to the fuction as gps_data.
        The speed value is than convert it from KM to ML and returned.
        """
        try:
            if gps_data[0] == "$GPRMC" or gps_data[0] == "$GPVTG":
                if gps_data[0] == "$GPRMC":
                    speed_data_kilometers = float(gps_data[7])
                    return '{0:.2f}'.format(speed_data_kilometers *1.151)

                if gps_data[0] == "$GPVTG":
                    speed_data_kilometers = float(gps_data[5])
                    return '{0:.2f}'.format(speed_data_kilometers * 1.151)
        except RuntimeError:
            pass

    def get_altitude(self, gps_gpgga_data):
        """Returns altitude from gps module.

            Requires GPGGA Sentence
            We get the data from the GPS sentence
            and convert the data field from meters to feet
        """
        print("get altitude")

        try:
            alt_data_meters = float(gps_gpgga_data[9])
            return alt_data_meters
        except RuntimeError:
            alt_data_meters = 0
            return alt_data_meters

    def get_latitude(self, gps_gprmc_data):
        """ Get lattitude information from GPS module.

        From the gps module get lattitude information.
        Its must be a float since thats how global coordinated work.
        """
        latitude_nmea = gps_gprmc_data[3]
        latitude_degrees = latitude_nmea[:2]
        try:
            if gps_gprmc_data[4] == "S":
                # If we are going south we use the negative
                latitude_degrees = float(latitude_degrees) * -1
            else:
                latitude_degrees = float(latitude_degrees) * 1

            latitude_degrees = str(latitude_degrees).strip(".0")
            latitude_ddd = latitude_nmea[2:10]
            latitude_nnm = float(latitude_ddd) / 60
            latitude_nnm = str(latitude_nnm).strip("0.")[:8]
            latitude = "{}.{}".format(latitude_degrees, latitude_nnm)
            return float(latitude)
        except RuntimeError:
            pass


    def get_longitude(self, gps_gprmc_data):
        """ Gets longitude information from GPS module.

        From the gps module get longitude information.
        Its must be a float since thats how global coordinated work.
        """
        try:
            longitude_nmea = gps_gprmc_data[5]
            longitude_degrees = longitude_nmea[1:3]
            try:
                if gps_gprmc_data[6] == "N":
                    longitude_degrees = float(longitude_degrees) * -1
                else:
                    longitude_degrees = float(longitude_degrees)

                longitude_degrees = str(longitude_degrees).strip(".0")
                longitude_ddd = longitude_nmea[3:10]
                longitude_mmm = float(longitude_ddd) / 60
                longitude_mmm = str(longitude_mmm).strip("0.")[:8]
                longitude = "{}.{}".format(longitude_degrees, longitude_mmm)
                return longitude
            except RuntimeError:
                pass
        except RuntimeError:
            pass

    def store_gps_data(self, latitude, longitude, fileName):
        """ Store historical GPS data.

        A file will be created everytime the car starts,
        a file will be populated with GPS information
        for later use.
        """
        try:
            delimiter = '\t'

            with open(fileName, 'w', newline='\n') as csvfile:
                fieldnames = ['longitude', 'latitude']
                writer = csv.writer(csvfile,
                delimiter=delimiter,
                quoting=csv.QUOTE_NONE,
                quotechar='',
                lineterminator='\n')
#                writer.writeheader()

                writer.writerow({'longitude': longitude, 'latitude': latitude})
        except RuntimeWarning:
            print("error")
