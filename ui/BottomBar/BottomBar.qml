import QtQuick 2.12
import QtQml 2.2

Rectangle{
    id: bottomBar


    anchors{
        bottom:parent.bottom
    }
    height: parent.height /12
    x: (parent.width /2) - (topBar.width /2)
    radius: 15
    color: "black"
    width: parent.width /2

    // Lights
    property bool seatBeltLights:  false
    property bool gasLights: true
    property bool breaksLights: true

    property bool airBagLights: true
    property bool oilLights: true
    property bool washerLightss: true
    property bool checkEngineLights:true
    property bool batteryLight: false

    property int  ambientTemperature : 0



    Row {
        id: leftRow
        x: 0
        y: 0

        height: 100

        anchors{
            left: parent.left
        }

        //        seatBeltLight
        Image {
            id: seatBeltLight
            source:seatBeltLights? "../../ui/assets/cluster images/seatBeltWarning-on.png" : "../../ui/assets/cluster images/seatBeltWarning-off.png"
            height: parent.height /2.5
            width: parent.height /2.5
            //            anchors.centerIn: parent.verticalCenter
        }

        //        gasLight
        Image {
            id: gasLight
            source:gasLights? "../../ui/assets/cluster images/gas-low.png" : "../../ui/assets/cluster images/gas-good.png"
            height: parent.height /2.5
            width: parent.height /2.5
            //            anchors.centerIn: parent.verticalCenter
        }

        //        breaksLight
        Image {
            id: breaksLight
            source:breaksLights? "../../ui/assets/cluster images/brakeWarning_on.png" : "../../ui/assets/cluster images/brakeWarning_Off.png"
            height: parent.height /2.5
            width: parent.height /2.5
            //            anchors.centerIn: parent.verticalCenter
        }
    }

    // Ambient Temperature
    Text{
        text:bottomBar.ambientTemperature + " F"
        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter
        color: "white"
        font.pointSize: 20
        font.family: "Segoe UI"
    }


    Row {
        id: righRow
        x: 0
        y: 0

        height: 100
        anchors{
            right: parent.right}

        //          airBagLight
        Image {
            id: airBagLight
            source:airBagLights ? "../../ui/assets/cluster images/airBagWarning-on.png" : "../../ui/assets/cluster images/airBagWarning-off.png"
            height: parent.height /2.5
            width: parent.height /2.5
            //             anchors.centerIn: parent.verticalCenter
        }
        //        oilLight
        Image {
            id: oilLight
            source:oilLights? "../../ui/assets/cluster images/engine-oil-on.png" : "../../ui/assets/cluster images/engine-oil-off.png"
            height: parent.height /2.5
            width: parent.height /2.5
            //             anchors.centerIn: parent.verticalCenter
        }
        //        washerLights
        Image {
            id: washerLights
            source:washerLights? "../../ui/assets/cluster images/washerFluid-off.png" : "../../ui/assets/cluster images/washerFluid-on.png"
            height: parent.height /2.5
            width: parent.height /2.5
            //            anchors.centerIn: parent.verticalCenter
        }

        //        checkEngineLight
        Image {
            id: checkEngineLight
            source:checkEngineLights? "../../ui/assets/cluster images/checkEngine-on.png" : "../../ui/assets/cluster images/checkEngine-off.png"
            height: parent.height /2.5
            width: parent.height /2.5
        }

    }
}
