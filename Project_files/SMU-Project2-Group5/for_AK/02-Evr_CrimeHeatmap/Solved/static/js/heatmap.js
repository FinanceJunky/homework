var myMap = L.map("map", {
    center: [0, 110],
    zoom: 5
});

L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href='https://www.openstreetmap.org/'>OpenStreetMap</a> contributors, <a href='https://creativecommons.org/licenses/by-sa/2.0/'>CC-BY-SA</a>, Imagery © <a href='https://www.mapbox.com/'>Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.streets",
    accessToken: API_KEY
}).addTo(myMap);

var url = "https://opendata.arcgis.com/datasets/5c026d553ff049a585b90c3b1d53d4f5_34.geojson";

d3.json(url, function(response) {

    console.log(response);

    var heatArray = [];

    for (var i = 0; i < response.length; i++) {
        var location = response.features[i].geometry;;

        if (location) {
            heatArray.push([location.coordinates[1], location.coordinates[0]]);
        }
    }

    var heat = L.heatLayer(heatArray, {
        radius: 20,
        blur: 35
    }).addTo(myMap);

});