// Copyright (C) 2021 The Qt Company Ltd.
// SPDX-License-Identifier: LicenseRef-Qt-Commercial


import QtQuick 2.0
import QtQuick.Layouts 1.11
import QtQuick.Controls 2.1
import QtQuick.Window 2.1
import QtQuick.Controls.Material 2.1

import io.qt.textproperties 1.0
import 'ui/BottomBar'
import 'ui/TopBar'
import 'ui/RightDisplay'
import 'ui/CarInfo'

ApplicationWindow {
    id: page
    width: 1920;
    height: 720;
    visible: true
    Material.theme: Material.Dark
    Material.accent: Material.Red

   Bridge {
        id: bridge
    }

   Timer{
       interval: 500; running:true; repeat:true
       onTriggered: bridge.setGauges("s");
   }
        Image {
            id: image2
            anchors.fill: parent
            opacity: .6
            z: -1
        }

        Rectangle{
            id:roundHolder
            x: (parent.width /2) - (roundHolder.width /2)
            y: (parent.height / 2) - (roundHolder.height / 2)

            color:"transparent"

            width: 500
            height:500

            RoundProgress{
                id:centerGauge
                rpmValue:"0"// Pass value for RPM Here
                speedValue:"0" // Pass value for the crrent speed
                kmhOrMPH:"MPH" // TODO
                celOrFarheit:"C" // TODO
            }
        }

        Rectangle{
            id:oilPressureHolder
            x: (parent.width /2.5) - (roundHolder.width )
            y: (parent.height /1.8) - (roundHolder.height / 2)
            color:"transparent"
            width: 500
            height:500

            // Timer for oil pressure
            Timer{
                interval: 100; running:true; repeat:true; triggeredOnStart:true;
                onTriggered: oilPressureGauge.oilPresureValueText = bridge.setOilPressure("11");
            } // Timer for coolent
            Timer{
                interval: 100; running:true; repeat:true; triggeredOnStart:true;
                onTriggered: oilPressureGauge.coolentTempValueText = bridge.setTemperature("11");
            }

            OilPressure{
                id: oilPressureGauge
                value: 5000
                oilPresureValueText: "0"
                coolentTempValueText: "0"
            }
        }

        TopBar{
            id:topBar
            dateTimeString: bridge.setTime("11")
            leftTurnSignal: bridge.setTurnLeft("11")
            rightTurnSignal:bridge.setTurnRight("11")
            popUp: bridge.setRetract("11")
            brights:bridge.setBeam("11")
            runningLights:bridge.setHold("11")
            hazardLights:bridge.setHazard("11")
        }

        BottomBar{
            id:bottombar

            ambientTemperature : bridge.setAmbientTemperature("11")
            seatBeltLights: bridge.setBelts("11")
            gasLights: bridge.setFuelLight("11")
            breaksLights: bridge.setBreak("11")
            airBagLights: bridge.setAirBag("11")
            oilLights: bridge.setOilLight("11")
            washerLightss: bridge.setWasher("11")
            checkEngineLights: bridge.setCheckHeat("11")
        }

        Timer{
            interval: 500; running:true; repeat:true
            onTriggered: rightDisplay.fuelLevel = bridge.setFuelLevel("11")
        }
        RightDisplay{
            id:rightDisplay

            engineTemperature : bridge.setTemperature("11")
            ambientTemperature : bridge.setAmbientTemperature("11")
            interiorTemperature : bridge.setInteriorTemperature("11")

            fuelLevel : 0
            averageMPG : bridge.setAverageMPG("11")
            fuelRange : bridge.setFuelRange("11")
            voltage : bridge.setBatteryVoltage("11")
            averageSpeed : bridge.setAverageSpeed()
        }
    }
