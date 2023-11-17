# 93MiataCluster
This project is a gauge cluster for a 1993 Mazda Miata. 
![Miata Cluster V2](https://github.com/gamatatsu0/93MiataCluster/assets/142171373/3b6e49d5-634a-4b45-a927-aeb0644a1947)

This is an ongoing project to freshen up the gauge cluster on my old Miata, it was only made to work with a miata pre OBD2. Hardware used on the project consists of a RaspberryPi, Arduino Mega,a donor gauge cluster and a jumper harness to wich I will share the drawing at a later time. 


The jumper harness connects the donor gauge cluster to the arduino mega and the ground bus. The Arduino Mega connects to the raspberry pi over a serial connection using the a USB cable. 
The arduino read the different analog and digital signals coming from the gauge cluster, performs multiple conversion on the values read to provide values related to our needs. 
