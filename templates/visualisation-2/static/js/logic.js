function createMap(CountryMetrics) {

  // Create the tile layer that will be the background of our map.
  var streetmap = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  });


  // Create a baseMaps object to hold the streetmap layer.
  var baseMaps = {
    "Street Map": streetmap
  };

  // Create an overlayMaps object to hold the bikeStations layer.
  var overlayMaps = {
    "Country Metrics": CountryMetrics
  };

  // Create the map object with options.
  var map = L.map("map-id", {
    center: [54, -2],
    zoom: 4,
    layers: [streetmap, CountryMetrics]
  });

  // Create a layer control, and pass it baseMaps and overlayMaps. Add the layer control to the map.
  L.control.layers(baseMaps, overlayMaps, {
    collapsed: false
  }).addTo(map);
}

function createMarkers(response) {

  // Pull the "stations" property from response.data.
  var countries = response;

  // Initialize an array to hold bike markers.
  var countryMarkers = [];

  // Loop through the stations array.
  for (var index = 0; index < countries.length; index++) {
    var country = countries[index];

    // For each station, create a marker, and bind a popup with the station's name.
    var countryMarker = L.marker([country.Latitude, country.Longitude])
      .bindPopup("<p><b>" + country.Country + "</b></p><p>Total Vaccinations: " + country.TOTAL_VACCINATIONS + "</p><p>Total Cases: " + country.Cumulative_cases + "</p><p>Total Deaths: " + country.Cumulative_deaths + "</p>");

    // Add the marker to the bikeMarkers array.
    countryMarkers.push(countryMarker);
  }

  // Create a layer group that's made from the bike markers array, and pass it to the createMap function.
  createMap(L.layerGroup(countryMarkers));
}


// Perform an API call to the Citi Bike API to get the station information. Call createMarkers when it completes.
d3.json("http://127.0.0.1:5000/country_metadata").then(createMarkers);
