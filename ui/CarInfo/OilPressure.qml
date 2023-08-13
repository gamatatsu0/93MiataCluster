import QtQuick 2.15
import QtQuick.Shapes 1.15
//import QtGraphicalEffects 1.5

Item {

    id: progress
    width: 400;
    height: 400;


    property real value: 5000
    property string oilPresureValue: "0"
    property string coolentTempValue: "0"

//    Properties General
    property bool roundCap: false
    property int startAngleLeft: -90
    property int startAngle: 90
    property real maxValue: 7000
    property int samples: 12

//    Big Circle
    property color bgColor: "transparent"
    property color bgStrokeColor: "#7e7e7e"
    property int strokeBgWidth: 20

//    Progress Circle
    property color progressColor: "blue"
    property color lessColor: "blue"
    property int progressWidth: 20

//    Text
    property string textFontFamily: "Segoe UI"
    property int textSize: 20
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
                radiusX: (progress.width /2.2) - (progress.progressWidth  /2.2)
                radiusY: (progress.height /2.2) - (progress.progressWidth  /2.2)
                centerX: (progress.width /2) -10
                centerY: progress.height /2.2
                startAngle: progress.startAngle
                sweepAngle: 180

            }
        }


        ShapePath{
            id: path
            strokeColor: progress.progressColor
            fillColor: "transparent"
            strokeWidth: progress.progressWidth
            capStyle: progress.roundCap ? ShapePath.RoundCap : ShapePath.FlatCap

            PathAngleArc{
                radiusX: (progress.width /2.2) - (progress.progressWidth /2.2)
                radiusY: (progress.height /2.2) - (progress.progressWidth /2.2)
                centerX: (progress.width /2) - 10
                centerY: progress.height /2.2
                startAngle: progress.startAngle
                sweepAngle: (180 / progress.maxValue * progress.value)

            }
        }

        Text {
            id: textProgress

            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            color: progress.textColor
            text: "5000"
            font.pointSize: progress.textSize
            font.family: progress.textFontFamily

        }

        Text {
            id: oilPreaaure
            text: progress.oilPresureValue + "PSI"

            anchors.verticalCenter: parent.verticalCenter
            x: 40
            width: 53
            height: 32
            color: progress.textColor
            font.pointSize: progress.textSize
            font.family: progress.textFontFamily

        }

        Text {
            id: coolantTemp

            text: progress.coolentTempValue + " F"

            anchors.verticalCenter: parent.verticalCenter
            x:  300
            color: progress.textColor
            font.pointSize: progress.textSize
            font.family: progress.textFontFamily

        }




        ShapePath{
            id: leftBG
            strokeColor: "red"
            fillColor: progress.bgColor
            strokeWidth: progress.strokeBgWidth
            capStyle: progress.roundCap ? ShapePath.RoundCap : ShapePath.FlatCap

            PathAngleArc{
                radiusX: (progress.width /2.2) - (progress.progressWidth  /2.2)
                radiusY: (progress.height /2.2) - (progress.progressWidth  /2.2)
                centerX: (progress.width /2) + 10
                centerY: progress.height /2.2
                startAngle: progress.startAngleLeft
                sweepAngle: 180

            }
        }


        ShapePath{
            id: lefts
            strokeColor: progress.bgStrokeColor
            fillColor: "transparent"
            strokeWidth: progress.progressWidth
            capStyle: progress.roundCap ? ShapePath.RoundCap : ShapePath.FlatCap

            PathAngleArc{
                radiusX: (progress.width /2.2) - (progress.progressWidth / 2.2)
                radiusY: (progress.height /2.2) - (progress.progressWidth / 2.2)
                centerX: (progress.width / 2) + 10
                centerY: (progress.height / 2.2)
                startAngle: progress.startAngleLeft
                sweepAngle: (180 / progress.maxValue * progress.value)

            }
        }


    }

}


