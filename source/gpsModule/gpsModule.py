# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
import serial
import csv


class gpsModule(QtCore.QObject):
    def __init__(self,serialPort):
        self.serialPort = serialPort
        self.serialConnection =None
        self.gpsData = ""

#        print("gps class init")

    def __str__(self):
        return f"The port '{self.serialPort}' was provided for serial communication with GPS module. Select actions you need to take"

    # ...................... Starting the GPS connection ......................
    def start_GPS_connection(self):

        try:
            print("Connecting to GPS antenna....")
            serialConnection = serial.Serial('/dev/ttyACM0', baudrate=9600)
#            serialConnection = serialConnection.readline()
            return serialConnection
#            self.get_gps_data(gps_connection)
        except:
            print("GPS Serial connection error")
    # ...................... Conversions ......................

    def meter_to_feet(self, meters):
        # One meter is 3.28084 feet
        return int(meters) * 3.28084

    def knots_to_miles(self,knots):
        # One knot is 1.68781 Miles
#        print (knots * 2)

        return float(knots * 1.68781)

    def clean_and_prep_data(self,gps):
        # Convert data to UTF-8 and separate by comas
        ser_bytes = gps.readline()
        decoded_bytes = ser_bytes.decode("UTF-8")
        return decoded_bytes.split(",")

# when at a complete stop the gps reads between 0.0. and 0.04 MPH
# adjust to hink it is qithin 0.000

    # ...................... Getting Data ......................
    def get_speed(self,gps_data):
        # Requires GPRMC sentence
        # We ge the data from the GPS sentence and convert the data field from knots to miles
        try:
            if gps_data[0] == "$GPRMC" or gps_data[0] == "$GPVTG":
                if gps_data[0] == "$GPRMC":
                    speed_data_kilometers = float(gps_data[7])
                    return '{0:.2f}'.format(speed_data_kilometers *1.151 )

                if gps_data[0] == "$GPVTG":
                    speed_data_kilometers = float(gps_data[5])
                    return '{0:.2f}'.format(speed_data_kilometers * 1.151)
        except:
            pass

    def get_altitude(self,gps_GPGGA_data):
        print("get altitude")
        # Requires GPGGA Sentence
        #  We get the data from the GPS sentence and convert the data field from meters to feet
#        print(gps_GPGGA_data)
        try:
            alt_data_meters = float(gps_GPGGA_data[9])
#            print("Altitude: {}".format(self.meter_to_feet(alt_data_meters)))
            return alt_data_meters
        # print(meter_to_feet(int(alt_data_meters)))
        except:
            alt_data_meters ="0"
            return alt_data_meters

    def get_latitude(self,gps_GPRMC_data):

        latitude_nmea = gps_GPRMC_data[3]
        latitude_degrees = latitude_nmea[:2]
        try:
            if gps_GPRMC_data[4] == "S":
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
        except:
            pass


    def get_longitude(self,gps_GPRMC_data):
        try:
#            print(gps_GPRMC_data)
            longitude_nmea = gps_GPRMC_data[5]
            longitude_degrees = longitude_nmea[1:3]
            try:
                if gps_GPRMC_data[6] == "N":
                    longitude_degrees = float(longitude_degrees) * -1
                else:
                    longitude_degrees = float(longitude_degrees)

                longitude_degrees = str(longitude_degrees).strip(".0")
                longitude_ddd = longitude_nmea[3:10]
                longitude_mmm = float(longitude_ddd) / 60
                longitude_mmm = str(longitude_mmm).strip("0.")[:8]
                longitude = "{}.{}".format(longitude_degrees, longitude_mmm)
                return longitude
            except:
                pass
        except:
            pass

    def store_gps_data(self,latitude,longitude,fileName):
        try:
            delimiter='\t'

            with open(fileName, 'w', newline='\n') as csvfile:
                fieldnames = ['longitude', 'latitude']
                writer = csv.writer(csvfile, delimiter=delimiter, quoting=csv.QUOTE_NONE, quotechar='',  lineterminator='\n')
#                writer.writeheader()

                writer.writerow({'longitude': longitude, 'latitude': latitude})



        except:
            "error "



    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
