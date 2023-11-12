import QtQuick 2.12
import "../CarInfo"


Rectangle {
    id: rightDisplayMain

    // Temperature properties
    property string engineTemperature : "0"
    property string ambientTemperature : "0"
    property string interiorTemperature : "0"


    // Fuel properties
    property int fuelLevel : 0
    property int averageMPG : 0
    property int fuelRange : 0

    // Battery properties
    property int voltage: 0

    // Speed properties
    property int averageSpeed: 0

    anchors{


    top:parent.top
    right:parent.right
    bottom:parent.bottom
    }
    width:parent.width *1/4.5
    color: "transparent"


    CarInfoWidget{
        id:carInfoWidget
        // Temperature
        engineTemperature : rightDisplayMain.engineTemperature
        ambientTemperature : rightDisplayMain.ambientTemperature
        interiorTemperature : rightDisplayMain.interiorTemperature

        // Fuel
        fuelLevel : rightDisplayMain.fuelLevel
        fuelLevelStr: rightDisplayMain.fuelLevelStr
        averageMPG : rightDisplayMain.averageMPG
        fuelRange : rightDisplayMain.fuelRange

        // voltage:
        voltage : rightDisplayMain.voltage
        // Speed
        averageSpeed : rightDisplayMain.averageSpeed
    }

}

