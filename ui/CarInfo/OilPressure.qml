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
    property int strokeBgWidth: 10

//    Progress Circle
    property color progressColor: "blue"
    property color lessColor: "blue"
    property int progressWidth: 10

//    Text
    property string textFontFamily: "Segoe UI"
    property int textSize: 50
    property color textColor: "#7c7c7c"
    FontLoader { id: digitalFont; source: "../../ui/assets/fonts/DS-DIGII.TTF" }

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

            text: "5000"
            font.family: digitalFont.name
            font.pixelSize: progress.textSize
            color: progress.textColor

            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter


        }
// Oil pressure text (PSI)
        Text {
            id: oilPreaaure
            text: progress.oilPresureValueText  + " PSI"
            font.family: digitalFont.name
            font.pixelSize:  progress.textSize-10
            color: progress.textColor

            x: 40
            width: 53
            height: 32

            anchors.verticalCenter: parent.verticalCenter



        }
// Collent Temp
        Text {
            id: coolantTemp

            text: progress.coolentTempValueText + " F"
            font.family: digitalFont.name
            font.pixelSize:  progress.textSize-10
            color: progress.textColor

            x:  300
            width: 53
            height: 32


            anchors.verticalCenter: parent.verticalCenter


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


