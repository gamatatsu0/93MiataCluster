import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick 2.0

// import QtCharts 2.13

//Car info Widget
Rectangle {
    id: graphsWidget

    // Temperature properties
    // Temperature properties
    property string engineTemperature: "0"
    property string ambientTemperature: "0"
    property string interiorTemperature: "0"

    // Fuel properties
    property int fuelLevel: 0
    property string fuelLevelStr: "0"
    property string averageMPG: "0"
    property string fuelRange: "0"

    // Battery properties
    property int voltage: 0

    // Speed properties
    property string averageSpeed: "0"

    property color myTransparent: Qt.rgba(0, 0, 0, 0.01)
    property color mainColorBlack: Qt.rgba(0, 0, 0, 0.35)

    anchors {
        right: parent.right
        bottom: parent.bottom
    }
    width: parent.width
    height: parent.height * 1 / 3
    color: mainColorBlack

    // ChartView {
    //     width: 400
    //     height: 300
    //     theme: ChartView.ChartThemeBrownSand
    //     antialiasing: true

    //     PieSeries {
    //         id: pieSeries
    //         PieSlice {
    //             label: "eaten"
    //             value: 94.9
    //         }
    //         PieSlice {
    //             label: "not yet eaten"
    //             value: 5.1
    //         }
    //     }
    // }
}
