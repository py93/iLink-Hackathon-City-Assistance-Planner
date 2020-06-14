

function sendSearch()
{
    searchText = $("#searchText").val().split(" ")[0];
    if (searchText.lastIndexOf('s') > 2)
    searchText = searchText.substring(0, searchText.lastIndexOf('s'));
    // alert(searchText);
    console.log("Send " + searchText);

    $.post("setDestination", {destination: searchText}).done(function(data) {
        console.log("SetDestination ");
        console.log(data);

        $("#searchResult").html("");

        for (el of data)
        {
            // data = '<div class="resultUnit">\
            // <div>Start Time: ' + el["start"] + '</div>\
            // <div><span><button onclick="sendFinalTravel(\'' + el["name"] + '\')"><i class="material-icons" style="padding: 5px;">directions_bike</i></button></span> <b>' + el["name"] + '</b></div>\
            // </div>';
            data = '<li class="w3-bar">\
            <img  onclick="sendFinalTravel(\'' + el["name"] + '\')" src="./images/cycle.png" class="w3-bar-item w3 w3-hide-small" style="width:85px">\
            <div class="w3-bar-item">\
              <span class="">Start Time: ' + el["start"] + '</span><br>\
              <span class="w3-large">' + el["name"] + '</span>\
            </div>\
          </li>\
            ';
            $("#searchResult").append(data);
        }
    });

    $("#guide001").html("Double click to select a location");
    mapAdd = "map.html?keyword=" + searchText;
    console.log("Set map " + mapAdd);
    loadIframe("mapframe", mapAdd);
}

function sendFinalTravel(destinationName)
{
    console.log("SendFinal " + destinationName);

    $.post("finalizeTravel", {destination: destinationName}).done(function(data) {
        console.log("Final ");
        console.log(data);

        // loadIframe("direction", "navigate.html?travel=" + data["travel"])
        $("#guide001").html("&nbsp;");
        loadIframe("mapframe", "navigate.html?travel=" + data["travel"])
        // showNav();
    });
}

$(document).ready(function() {
    $("#curtain").click(function() {
        hideNav();
        loadIframe("direction", "about:blank")
    })

    $("#searchButton").click(function() {
        sendSearch();
    });

    $("#searchText").keypress(function(e) {
        if (e.which == 13)
            sendSearch();
    });

});
