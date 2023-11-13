import QtQuick 2.12
import QtQuick.Shapes 1.12
//import QtGraphicalEffects 1.5

Item {

    id: progress
    width: 400;
    height: 400;

//    Values being passed
    property real value: 5000
    property int oilPresureValue: 0
    property int coolentTempValue: 0
    property string oilPresureValueText: "0"
    property string coolentTempValueText: "0"

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
                sweepAngle: (180 / 100 * progress.oilPresureValueText)
            }
        }
// Middle Text
        Text {
            id: textProgress

            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            color: progress.textColor
            text: "5000"
            font.pointSize: progress.textSize
            font.family: progress.textFontFamily

        }
// Oil pressure text (PSI)
        Text {
            id: oilPreaaure
            text: progress.oilPresureValueText  + "PSI"

            anchors.verticalCenter: parent.verticalCenter
            x: 40
            width: 53
            height: 32
            color: progress.textColor
            font.pointSize: progress.textSize
            font.family: progress.textFontFamily

        }
// Collent Temp
        Text {
            id: coolantTemp

            text: progress.coolentTempValueText + " F"

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
        // Coolent
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
                sweepAngle: 180- (180 / 250 * progress.coolentTempValueText)

            }
        }


    }

}


