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
        // layers.LAYER_MARKER
    ]
});

// Add our 'streetmap' tile layer to the map
satellitemap.addTo(myMap);

// Create an overlays object to add to the layer control
var overlays = {
    "Boronean Orangutan": layers.LAYER_PONGO_PYGMAEUS,
    "Sumatrun Orangutan": layers.LAYER_PONGO_ABELII,
    "Tanapuli Orangutan": layers.LAYER_PONGO_TAPANULIENSIS,
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
    }).addTo(layers.LAYER_PONGO_PYGMAEUS);

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
    }).addTo(layers.LAYER_PONGO_ABELII);

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
    }).addTo(layers.LAYER_PONGO_TAPANULIENSIS);

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

/////////////////////////////////////////////////////////////////////////////////////

//This code works yeah

var newtry2 = "https://opendata.arcgis.com/datasets/5c026d553ff049a585b90c3b1d53d4f5_34.geojson";

d3.json(newtry2, function(response) {
    console.log(response);
    for (var i = 0; i < response.features.length; i++) {
        var location = response.features[i].properties;
        if (location) {
            var newMarker = L.marker([location.latitude, location.longitude]);
        };
        // Add the new marker to the appropriate layer
        newMarker.addTo(layers.LAYER_MARKER);
        // Bind a popup to the marker that will  display on click. This will be rendered as HTML
        newMarker.bindPopup("Mill Name: " + location.mill_name + "<br> Location Certified Using Sustainable <br> Practices: " + location.cert + "<br>");
    }
});

//end --------------------------------------------------------------------