import QtQuick 2.12
import QtQuick.Controls 2.12
import QtCharts

//Car info Widget
Rectangle {
    id: graphsWidget

    // Temperature properties
    // Temperature properties
    property string engineTemperature : "0"
    property string ambientTemperature : "0"
    property string interiorTemperature : "0"


    // Fuel properties
    property int fuelLevel : 0
    property string fuelLevelStr: "0"
    property string averageMPG : "0"
    property string fuelRange : "0"

    // Battery properties
    property int voltage: 0

    // Speed properties
    property string averageSpeed: "0"


    property color myTransparent: Qt.rgba(0, 0, 0, 0.01)
    property color mainColorBlack: Qt.rgba(0, 0, 0, 0.35)


    anchors{
        right:parent.right
        bottom:parent.bottom
    }
    width:parent.width
    height:parent.height * 1/3
    color:mainColorBlack

    ChartView {
        title: "Line Chart"
        anchors.fill: parent
        antialiasing: true

        LineSeries {
            name: "Line"
            XYPoint { x: 0; y: 0 }
            XYPoint { x: 1.1; y: 2.1 }
            XYPoint { x: 1.9; y: 3.3 }
            XYPoint { x: 2.1; y: 2.1 }
            XYPoint { x: 2.9; y: 4.9 }
            XYPoint { x: 3.4; y: 3.0 }
            XYPoint { x: 4.1; y: 3.3 }
        }
    }

    //        Average Mpg

}


