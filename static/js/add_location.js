var water_marker_icon = "/static/find_water/water_marker_icon.svg";
var map_styles_array = (function () {
    var map_styles_array = null;
    $.ajax({
        'async': false,
        'global': false,
        'url': "/static/find_water/map_setting.json",
        'dataType': "json",
        'success': function (data) {
            map_styles_array = data;
        }
    });
    return map_styles_array;
})();

function initMap(){
  gMap = new google.maps.Map(document.getElementById('map'));
  //Default location if location of user is not found --Defualt location set to stuyvesant
  var fountian_lat;
  var fountain_lng;

  zoomL = 18;

  navigator.geolocation.getCurrentPosition(function(position) {
    // Center on user's current location if geolocation prompt allowed
      var fountian_lat = position.coords.latitude;
      var fountian_lng = position.coords.longitude;

    var initialLocation = new google.maps.LatLng(fountian_lat, fountian_lng);
    gMap.setCenter(initialLocation);
    gMap.setZoom(zoomL);
    gMap.setOptions({styles: map_styles_array, disableDefaultUI: true});

      addMarker(initialLocation, gMap, water_marker_icon);

  }, function(positionError) {
    // User denied geolocation prompt - default to Stuyvesant
    var fountian_lat = 40.717892;
    var fountian_lng = -74.013908;
    var initialLocation = new google.maps.LatLng(fountian_lat, fountian_lng);
    gMap.setCenter(initialLocation);
    gMap.setZoom(zoomL);
    gMap.setOptions({styles: map_styles_array, disableDefaultUI: true});

    alert("Couldn't find your location. Please make sure your location services are enabled and try again.");

      addMarker(initialLocation, gMap, water_marker_icon);
  });
}

//add Marker function
function addMarker(location, map, icon) {
    marker = new google.maps.Marker({
        position: location,
        map: map,
        icon: icon
    });
}
