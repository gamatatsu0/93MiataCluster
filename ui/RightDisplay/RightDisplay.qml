import QtQuick 2.15
import "../CarInfo"


Rectangle {
    id: rightDisplayMain

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

    anchors{


    top:parent.top
    right:parent.right
    bottom:parent.bottom
    }
    width:parent.width *1/4.5
    color: "transparent"


    CarInfoWidget{
        id:carInfoWidget

        engineTemperature : rightDisplayMain.engineTemperature
        ambientTemperature : rightDisplayMain.ambientTemperature
        interiorTemperature : rightDisplayMain.interiorTemperature

        fuelLevel : rightDisplayMain.fuelLevel
        averageMPG : rightDisplayMain.averageMPG
        fuelRange : rightDisplayMain.fuelRange

        voltage : rightDisplayMain.voltage

        averageSpeed : rightDisplayMain.averageSpeed
    }

}

