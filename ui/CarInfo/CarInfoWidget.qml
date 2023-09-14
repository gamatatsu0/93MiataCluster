import QtQuick 2.12
import QtQuick.Controls 2.12


//Car info Widget
    Rectangle {
        id: carInfo

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

//        Average Speed
        Rectangle{
            id: avgSpeed
            anchors{
                left:parent.left
                bottom:parent.bottom
            }
            width: parent.width *1/4
            height:parent.height * 1/2
            color:"transparent"
            Column{
                Text{
                    text: "Average Speed"
                    color:"white"}

                Text{
                    text:carInfo.averageSpeed + " M/H"
                    color:"white"}

                    }
            }
//        Average Mpg
        Rectangle{
            id: avgMPG
            anchors{
                left:parent.left
                bottom:avgSpeed.top
            }
            width: parent.width *1/4
            height:parent.height * 1/4
            color:"transparent"
            Column{
                Text{
                    text:"AVG MPG"
                    color:"white"}

                Text{
                    text: carInfo.averageMPG + " M/G"
                    color:"white"}

                    }
            }

//        My Range
        Rectangle{
            id: range
            anchors{
                left:parent.left
                bottom:avgMPG.top
            }
            width: parent.width *1/4
            height:parent.height * 1/4
            color:"transparent"
            Column{
                Text{
                    text:"Range"
                    color:"white"}

                Text{
                    function get_avg_range(gas){
                        var gallons_left = gas*13
                        return gallons_left
                    }
                    text: get_avg_range(carInfo.fuelRange) + " Miles"
                    color:"white"}
                    }
        }

//        Margin at Top
        Rectangle{
        id: borders
        anchors{
            top:parent.top
            left:parent.left
            right:parent.right
            }
        height: 2
        color:"white"
        }

        Rectangle{
            id: righBarsrHolder
            anchors{
                right:parent.right
                top:border.bottom
            }
            width: parent.width - range.width
            height:parent.height * .1
            color:myTransparent


            //        Holds the gas tank bar
                    Rectangle{
                        id: rangeBarRight
                        anchors{
                            right:parent.right
                            bottom: parent.bottom
                        }
                        width: parent.width *1/3
                        height:parent.height *1/8
                        color:"transparent"

                        Text{
                            id:fuelText
                        text: "     Fuel"
                        color:"white"}


                        Text{
                            id:fuelTextValue
                        text: carInfo.fuelLevelStr
                        color:"white"}

                        ProgressBar {
                                anchors{
                                    right: parent.right
                                    left:parent.left
                                    bottom: parent.bottom

                                }
                                // Actual gastank value
                                value: carInfo.fuelLevel /10
                            }

                    }

//                    Holds the battery Voltage bar
                    Rectangle{
                        id: batteryBarRight
                        anchors{
                            left:parent.left
                            bottom:parent.bottom
                        }
                        width: parent.width *1/3
                        height:parent.height * 1/8
                        color:"transparent"
                        Text{
                            id:batteryText
                        text: "Battery"
                        color:"white"}
                        ProgressBar {
                                anchors{
                                    right: parent.right
                                    left:parent.left
                                    bottom: parent.bottom
                                }
                                // Actual voltage value
                                value: carInfo.voltage
                            }
                    }
}

//        Rectangle to hold car Image
        Rectangle{
            id: imageHolder
            anchors{
                right:parent.right
                bottom:parent.bottom
            }
            width: parent.width - range.width
            height:parent.height * .85
            color:"transparent"

//            Car Image
            Image {
                id: carRender
                anchors.centerIn:  parent
                width: parent.width+10
                fillMode: Image.PreserveAspectFit
                source:"../../ui/assets/redMiata.png"
                anchors.verticalCenterOffset: -1
                anchors.horizontalCenterOffset: -5
            }
        }
    }


