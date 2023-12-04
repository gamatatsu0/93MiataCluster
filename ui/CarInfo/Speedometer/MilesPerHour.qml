import QtQuick 2.12

Item {
    id:milesperhour
    width: 100
    height:200


//    Values
    property string currentMphValue:"60"
    property string mphOrKm: "MPH"
//    Text
    property string text: "%"
    property string textFontFamily: "Orbitron"
    property int textSize: 50
    property color textColor: "#7c7c7c"
    FontLoader { id: digitalFont; source: "../../../ui/assets/fonts/DS-DIGII.TTF" }


//    Column{
//        id:mainColumn
//        height: 50


        // Text that just says MPH
        Text {
            id: mphText
            text: milesperhour.mphOrKm // Miles of kilometers per hour

            anchors.verticalCenter: parent.top
            anchors.horizontalCenter: parent.horizontalCenter
            color: milesperhour.textColor
            font.family: digitalFont.name
            font.pixelSize: milesperhour.textSize

        }

        // Text that displays the actual value of the car speed
        Text {
            id: mphValue
            text: milesperhour.currentMphValue // Actual value of MPH

            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            color: milesperhour.textColor
            font.family: digitalFont.name
            font.pixelSize: 150

//        }

    }



}
