// Define streetmap and darkmap layers
var streetmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.streets",
    accessToken: API_KEY
});

var darkmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.dark",
    accessToken: API_KEY
});

var graymap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href='https://www.openstreetmap.org/'>OpenStreetMap</a> contributors, <a href='https://creativecommons.org/licenses/by-sa/2.0/'>CC-BY-SA</a>, Imagery © <a href='https://www.mapbox.com/'>Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.light",
    accessToken: API_KEY
});

var satellitemap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href='https://www.openstreetmap.org/'>OpenStreetMap</a> contributors, <a href='https://creativecommons.org/licenses/by-sa/2.0/'>CC-BY-SA</a>, Imagery © <a href='https://www.mapbox.com/'>Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.streets-satellite",
    accessToken: API_KEY
});

var outdoors = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href='https://www.openstreetmap.org/'>OpenStreetMap</a> contributors, <a href='https://creativecommons.org/licenses/by-sa/2.0/'>CC-BY-SA</a>, Imagery © <a href='https://www.mapbox.com/'>Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.outdoors",
    accessToken: API_KEY
});

// Define a baseMaps object to hold our base layers
var baseMaps = {
    "Satellite": satellitemap,
    "Dark Map": darkmap,
    "Gray Map": graymap,
    "Street Map": streetmap,
    "Outdoors": outdoors
};

// Initialize all of the LayerGroups we'll be using
var layers = {
    LAYER_PONGO_PYGMAEUS: new L.LayerGroup(),
    LAYER_PONGO_ABELII: new L.LayerGroup(),
    LAYER_PONGO_TAPANULIENSIS: new L.LayerGroup(),
    LAYER_MARKER: new L.LayerGroup(),
};

// Creating map object
var myMap = L.map("map", {
    center: [0, 110],
    zoom: 5,
    layers: [
        layers.LAYER_PONGO_PYGMAEUS,
        layers.LAYER_PONGO_ABELII,
        layers.LAYER_PONGO_TAPANULIENSIS,
        layers.LAYER_MARKER
    ]
});

// Add our 'streetmap' tile layer to the map
satellitemap.addTo(myMap);

// Create an overlays object to add to the layer control
var overlays = {
    "Boronean Orangutan": layers.LAYER_PONGO_PYGMAEUS,
    "Sumatrun Orangutan": layers.LAYER_PONGO_ABELII,
    "Tanapulien Orangutan": layers.LAYER_PONGO_TAPANULIENSIS,
    "Palm Oil Mills": layers.LAYER_MARKER,
};

// Create a control for our layers, add our overlay layers to it
L.control.layers(baseMaps, overlays, {
    collapsed: false
}).addTo(myMap);

// Load in geojson data
var geoData_Pongo_pygmaeus = "static/data2/Pongo_pygmaeus.json";

var Pongo_pygmaeus_Habitat;

// Grab data with d3
d3.json(geoData_Pongo_pygmaeus, function(data) {

    // Create a new choropleth layer
    Pongo_pygmaeus_Habitat = L.choropleth(data, {
        style: {
            // Border color
            color: "orange",
            weight: 1,
            fillOpacity: 0.6
        },

        // // Binding a pop-up to each layer
        // onEachFeature: function(feature, layer) {
        //     layer.bindPopup("Zip Code: " + feature.properties.ZIP + "<br>Median Household Income:<br>" +
        //         "$" + feature.properties.MHI2016);
        // }
    }).addTo(myMap);

});

// Add the second Orangutan

var geoData_Pongo_abelii = "static/data2/Pongo_abelii.json";

var Pongo_abelii_Habitat;

d3.json(geoData_Pongo_abelii, function(data3) {

    // Create a new choropleth layer
    Pongo_abelii_Habitat = L.choropleth(data3, {

        style: {
            // Border color
            color: "purple",
            weight: 1,
            fillOpacity: 0.6
        },

        // // Binding a pop-up to each layer
        // onEachFeature: function(feature, layer) {
        //     layer.bindPopup("Zip Code: " + feature.properties.ZIP + "<br>Median Household Income:<br>" +
        //         "$" + feature.properties.MHI2016);
        // }
    }).addTo(myMap);

});

//Add the third Orangutan

var geoData_Pongo_tapanuliensis = "static/data2/Pongo_tapanuliensis.json";

var Pongo_tapanuliensis_Habitat;

d3.json(geoData_Pongo_tapanuliensis, function(data2) {

    // Create a new choropleth layer
    Pongo_tapanuliensis_Habitat = L.choropleth(data2, {

        style: {
            // Border color
            color: "red",
            weight: 1,
            fillOpacity: 0.6
        },

        // // Binding a pop-up to each layer
        // onEachFeature: function(feature, layer) {
        //     layer.bindPopup("Zip Code: " + feature.properties.ZIP + "<br>Median Household Income:<br>" +
        //         "$" + feature.properties.MHI2016);
        // }
    }).addTo(myMap);

});

// Here we create a legend control object.
var legend = L.control({
    position: "topleft"
});

// Then add all the details for the legend
legend.onAdd = function() {
    var div = L.DomUtil.create("div", "info legend");

    var Orangutans = ["Bornean Orangutan ", "Sumatrun Orangutan ", " Tapanuli Orangutan "];
    var species = [" Pongo pygmaeus", " Pongo abelli", " Pongo tapanuliensis"]
    var colors = [
        "orange",
        "purple",
        "red"
    ];

    // Looping through our intervals to generate a label with a colored square for each interval.
    div.innerHTML = "<span>Legend:<br></span>";
    for (var i = 0; i < Orangutans.length; i++) {
        div.innerHTML +=
            "<i class='circle' style='background: " + colors[i] + "'></i> " +
            Orangutans[i] + (species[i] ? "&ndash;" + species[i] + "<br>" : "+");
    }
    return div;
};

// Finally, we our legend to the map.
legend.addTo(myMap);

// Create a red circle over Dallas
L.circle([5, 110], {
    color: "red",
    fillColor: "red",
    fillOpacity: 0.75,
    radius: 100000
}).addTo(myMap);
/////////////////////////////////////////////////////////////////////////////////////

//This code works yeah

var newtry2 = "https://opendata.arcgis.com/datasets/5c026d553ff049a585b90c3b1d53d4f5_34.geojson";

d3.json(newtry2, function(response) {
    console.log(response);
    for (var i = 0; i < response.features.length; i++) {
        var location = response.features[i].properties;
        if (location) {
            L.marker([location.latitude, location.longitude]).addTo(myMap);
        }
    }
});

//end alexander--------------------------------------------------------------------

// Perform a GET request to the query URL

// d3.json(newtry2, function(data9) {
//     // Once we get a response, send the data.features object to the createFeatures function
//     createFeatures(data9.features);
// });

// function createFeatures(earthquakeData) {

// Define a function we want to run once for each feature in the features array
// Give each feature a popup describing the place and time of the earthquake
// function onEachFeature(feature, layer) {
//     layer.bindPopup("<h3>" + feature.properties.mill_name +
//         "</h3><hr><p>" + feature.properties.cert + "</p>"
//         // + "<hr><p>Magnitude: " + feature.properties.mag + "</p>"
//     );
// }

//marker options
// var geojsonMarkerOptions = {
//     radius: 10000,
//     fillColor: "#ff7800",
//     color: "#000",
//     weight: 1,
//     opacity: 1,
//     fillOpacity: 0.8
// };

// Create a GeoJSON layer containing the features array on the earthquakeData object
// Run the onEachFeature function once for each piece of data in the array

// var earthquakes = L.geoJSON(earthquakeData, {
//     onEachFeature: onEachFeature,
//     pointToLayer: function(feature, latlng) {
//         return L.circleMarker(latlng, geojsonMarkerOptions);
//         console.log(earthquakes)
//     },
//     style: function(feature) {
//         var mag = { color: "blue", fillColor: "blue", radius: 2 };
//         if (mag >= 5.0) {
//             return { color: "firebrick", fillColor: "firebrick", radius: 18 };
//         } else if (mag >= 4.0) {
//             return { color: "red", fillColor: "red", radius: 14 };
//         } else if (mag >= 3.0) {
//             return { color: "orange", fillColor: "orange", radius: 11 };
//         } else if (mag >= 2.0) {
//             return { color: "yellow", fillColor: "yellow", radius: 8 };
//         } else if (mag >= 1.0) {
//             return { color: "green", fillColor: "green", radius: 5 };
//         } else {
//             return { color: "blue", fillColor: "blue", radius: 2 };
//         }
//     },
// });

// Sending our earthquakes layer to the createMap function
// createMap(earthquakes);
// };