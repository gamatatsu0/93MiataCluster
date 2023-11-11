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



            OilPressure{
                id: oilPressureGauge
                value: 5000
                oilPresureValue: 10
                oilPresureValueText: bridge.setOilPressure(1)

                coolentTempValue: bridge.setTemperature(1)
                coolentTempValueText: bridge.setTemperature(1)
            }
        }

        TopBar{
            id:topBar
            leftTurnSignal: bridge.setTurnLeft(1)
            rightTurnSignal:bridge.setTurnRight(1)
            popUp: bridge.setRetract(1)
            brights:bridge.setBeam(1)
            runningLights:bridge.setHold(1)
            hazardLights:bridge.setHazard(1)
        }

        BottomBar{
            id:bottombar

            ambientTemperature : bridge.setAmbientTemperature(1)
            seatBeltLights: bridge.setBelts(1)
            gasLights: bridge.setFuelLight(1)
            breaksLights: bridge.setBreak(1)
            airBagLights: bridge.setAirBag(1)
            oilLights: bridge.setOil(1)
            washerLightss: bridge.setWasher(1)
            checkEngineLights: bridge.setCheckHeat(1)


        }

        RightDisplay{
            id:rightDisplay

            engineTemperature : bridge.setTemperature(1)
            ambientTemperature : bridge.setAmbientTemperature(1)
            interiorTemperature : bridge.setInteriorTemperature(1)

            fuelLevel : bridge.setFuelLevel(1)
            fuelLevelStr: bridge.setFuelLevel(1)
            averageMPG : bridge.setAverageMPG(1)
            fuelRange : bridge.setFuelRange(1)

            voltage : bridge.setBatteryVoltage(1)

            averageSpeed : bridge.setAverageSpeed(1)

        }



    }

