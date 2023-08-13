import QtQuick 2.15
import QtQuick.Window 2.15

import QtQuick 2.0
import QtQuick.Layouts 1.11
import QtQuick.Controls 2.1
import QtQuick.Window 2.1
import QtQuick.Controls.Material 2.1


// Importing other eleents
import 'ui/BottomBar'
import 'ui/TopBar'
import 'ui/RightDisplay'
import 'ui/CarInfo'



// NOTES
// Try to pass data from python through the bridge
// From the bridge we can pass the data to each one of the elements
// From the elements we need to make that the value that is being changes has been declared @ in the Item



ApplicationWindow {
    id:page
    visible: true
    width: 1920;
    height: 720

    // The bridge is used to connect to the Python Backend
    // The functions in here calls the variable in the different elements that need to be changed
    Connections {
        target: backend

        function onPrintTime(time){
            centerGauge.kmhOrMPH = time
        }

        function onPrintMPH(time){
            centerGauge.speedValue = time
        }

        function onPrintRPM(rpm){
            centerGauge.rpmValue = rpm
        }

        function onPrintEngineTemperature(coolant){
            oilPressureGauge.coolentTempValue = coolant
        }
        function onPrintOilPressure(oil){
            oilPressureGauge.oilPresureValue = oil
        }
        function onPrintFuelLevel(fuel){
            rightDisplay.fuelLevel = fuel
        }
        function onprintBatteryVoltage(voltage){
            rightDisplay.voltage = voltage
        }
        // For the simple lights
        function onPrintTurnLeft(light){
            topBar.leftTurnSignal = light
        }
        function onPrintTurnRight(light){
            topBar.rightTurnSignal = light
        }
        function onPrintHold(light){}

        function onPrintAirBag(light){
            bottombar.airBagLights = light
        }
        function onPrintRetract(light){
            topBar.popUp = light
        }
        function onPrintABS(light){

        }
        function onPrintWasher(light){
            bottombar.washerLightss = light
        }

        function onPrintBeam(light){
            topBar.brights = light
        }
        function onPrintBelts(light){
            bottombar.seatBeltLights = light
        }
        function onPrintBreak(light){
            bottombar.breaksLights = light
        }
        function onPrintBattery(light){
            bottombar.batteryLight = light
        }
        function onPrintCheckHeat(light){
            bottombar.checkEngineLights = light
        }
        //        function onPrintCheckEngine(light){}
        //        function onPrintCheckEngine(light){}
        //        function onPrintCheckEngine(light){}
        //        function onPrintCheckEngine(light){}
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
                oilPresureValue: "80"
                coolentTempValue: "30"
            }
        }

        TopBar{
            id:topBar
            leftTurnSignal: false
            rightTurnSignal:false
            popUp: false
            brights:false
            runningLights:false
            hazardLights:false
        }

        BottomBar{
            id:bottombar

            ambientTemperature : "0"
            seatBeltLights: false
            gasLights: false
            breaksLights: false
            airBagLights: false
            oilLights: false
            washerLightss: false
            checkEngineLights: false


        }

        RightDisplay{
            id:rightDisplay

            engineTemperature : "0"
            ambientTemperature : "0"
            interiorTemperature : "0"

            fuelLevel : 0
            averageMPG : "0"
            fuelRange : "0"

            voltage : 0

            averageSpeed : "0"

        }
    }

    /*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
##^##*/

