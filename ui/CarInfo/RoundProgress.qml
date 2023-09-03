// Make sure to use the QtQuick 2.12
// Otherwise there will be issues with with imports and QtQuick.Shapes
// For shapes we need to make sure we use the version 1.12

import QtQuick.Shapes 1.12
import QtQuick 2.12
//import QtGraphicalEffects 1.12


import 'Speedometer'

//import QtGraphicalEffects 1.5

Item {
    
    id: progress
    width: 550;
    height: 550;

//   General Gauge Properties
    property bool roundCap: true
    property int startAngle: -210
    property real maxRPMValue: 7000
    property string speedValue: "0"
    property string rpmValue: "5" // Value for the number in the center
    property int samples: 12
    property string kmhOrMPH : "MPH" // Default is MPH
    property string celOrFarheit: "C" // Default is Celcius

//    Big Circle
    property color bgColor: "transparent"
    property color bgStrokeColor: "#7e7e7e"
    property int strokeBgWidth: 40

//    Progress Circle
    property color progressColor: (progress.rpmValue < 6000)? "blue" : "red"
    property color lessColor: "blue"

    property int progressWidth: 40

//    Text Properties
    property string text: "%"
    property string textFontFamily: "Segoe UI"
    property int textSize: 35
    property int rpmLabelSize: 30
    property color textColor: "#7c7c7c"



    Shape{
        id:shape
        anchors.fill: parent
        layer.enabled: true
        layer.samples: progress.samples


        ShapePath{
            id: pathBG
            strokeColor: progress.bgStrokeColor
            fillColor: progress.bgColor
            strokeWidth: progress.strokeBgWidth
            capStyle: progress.roundCap ? ShapePath.RoundCap : ShapePath.FlatCap

            PathAngleArc{
                radiusX: (progress.width /2) - (progress.progressWidth  / 2)
                radiusY: (progress.height /2) - (progress.progressWidth  / 2)
                centerX: progress.width / 2
                centerY: progress.height / 2
                startAngle: progress.startAngle
                sweepAngle: 360

            }
        }


        ShapePath{
            id: path
            strokeColor: progress.progressColor
            fillColor: "transparent"
            strokeWidth: progress.progressWidth
            capStyle: progress.roundCap ? ShapePath.RoundCap : ShapePath.FlatCap

            PathAngleArc{
                radiusX: (progress.width /2) - (progress.progressWidth / 2)
                radiusY: (progress.height /2) - (progress.progressWidth / 2)
                centerX: progress.width / 2
                centerY: progress.height / 2
                startAngle: progress.startAngle
                sweepAngle: (240 / progress.maxRPMValue * progress.rpmValue)

            }

//            Glow {
//                anchors.fill: path
//                radius: 20
//                samples: 17
//                color: "red"
//                source: path
//            }
        }

        // Displays the RPM
        Text {
            id: textProgress
            text: progress.rpmValue

            anchors.top: milesPerHourWidget.bottom
//            anchors.verticalCenter: parent.bottom
            anchors.horizontalCenter: parent.horizontalCenter

            color: progress.textColor
            font.pointSize: progress.textSize
            font.family: progress.textFontFamily

        }

        Text{
            id: rpmLabel
            text: "RPM"

            anchors.left: textProgress.right
            anchors.bottom: textProgress.bottom


        }

        // Displays the speed
        MilesPerHour{
            id: milesPerHourWidget
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            currentMphValue:progress.speedValue
            mphOrKm:progress.kmhOrMPH

        }




    }

}

/*##^##
Designer {
    D{i:0;autoSize:true;height:250;width:250}
}
##^##*/
