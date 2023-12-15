import QtQuick 2.12
import QtQuick.Controls 2.12

Rectangle {
    id: topBar
    anchors {
        top: parent.top
    }

    x: (parent.width / 2) - (topBar.width / 2)
    radius: 15
    color: "black"
    height: parent.height / 12
    width: parent.width / 2

    property bool leftTurnSignal: false
    property bool rightTurnSignal: false
    property bool popUp: false
    property bool brightBeam: false
    property bool runningLights: false
    property bool hazardLights: false

    property var locale: Qt.locale()
    property string dateTimeString: "Tue 2013-09-17 10:56:06"

    Row {
        id: leftRow
        x: 0
        y: 0
        height: 100
        anchors {
            left: parent.left
        }

        //        turnLeft
        Image {
            id: leftArrow
            source: leftTurnSignal ? "../../ui/assets/cluster images/blueArrowLeft.png" : "../../ui/assets/cluster images/grayArrowLeft.png"
        }

        //        popUp
        Image {
            id: pupUp
            source: popUp ? "../../ui/assets/cluster images/popUpOn.png" : "../../ui/assets/cluster images/popUpOff.png"
        }

        //        lights
        Image {
            id: lights
            source: runningLights ? "../../ui/assets/cluster images/lightsOn.png" : "../../ui/assets/cluster images/lightsOff.png"
        }
    }

    // Clock
    Item {
        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter
        Timer {
            interval: 500
            running: true
            repeat: true
            onTriggered: time.text = new Date().toLocaleTimeString(
                             Qt.locale("de_DE"))
        }
        Text {
            id: time
            color: "white"
            font.pointSize: 20
            font.family: "Segoe UI"
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
        }
    }
    Row {
        id: righRow
        x: 0
        y: 0

        height: 100
        anchors {
            right: parent.right
        }
        //          brights
        Image {
            id: brights
            source: brightBeam ? "../../ui/assets/cluster images/lightsOn.png" : "../../ui/assets/cluster images/lightsOff.png"
        }
        //        hazardLights
        Image {
            id: hazards
            source: hazardLights ? "../../ui/assets/cluster images/hazardOn.png" : "../../ui/assets/cluster images/hazardOff.png"
        }
        //        turnRight
        Image {
            id: rightArrow
            source: rightTurnSignal ? "../../ui/assets/cluster images/blueArrowRight.png" : "../../ui/assets/cluster images/grayArrowRight.png"
        }
    }
}
