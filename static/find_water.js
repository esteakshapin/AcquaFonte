//symbol for marker user

var water_marker_icon = "/static/find_water/water_marker_icon.svg";

var user_marker_icon = '/static/find_water/user_marker_icon.svg';

var markersArray = [];

var circle;


//MAP STYLE DATA
var map_styles_array = [
  {
    "elementType": "geometry",
    "stylers": [
      {
        "color": "#ebe3cd"
      }
    ]
  },
  {
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "color": "#523735"
      }
    ]
  },
  {
    "elementType": "labels.text.stroke",
    "stylers": [
      {
        "color": "#f5f1e6"
      }
    ]
  },
  {
    "featureType": "administrative",
    "stylers": [
      {
        "visibility": "simplified"
      }
    ]
  },
  {
    "featureType": "administrative",
    "elementType": "geometry.stroke",
    "stylers": [
      {
        "color": "#c9b2a6"
      }
    ]
  },
  {
    "featureType": "administrative",
    "elementType": "labels",
    "stylers": [
      {
        "visibility": "off"
      }
    ]
  },
  {
    "featureType": "administrative.land_parcel",
    "elementType": "geometry.stroke",
    "stylers": [
      {
        "color": "#dcd2be"
      }
    ]
  },
  {
    "featureType": "administrative.land_parcel",
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "color": "#ae9e90"
      }
    ]
  },
  {
    "featureType": "landscape",
    "elementType": "labels",
    "stylers": [
      {
        "visibility": "off"
      }
    ]
  },
  {
    "featureType": "landscape.natural",
    "elementType": "geometry",
    "stylers": [
      {
        "color": "#dfd2ae"
      }
    ]
  },
  {
    "featureType": "poi",
    "elementType": "geometry",
    "stylers": [
      {
        "color": "#dfd2ae"
      }
    ]
  },
  {
    "featureType": "poi",
    "elementType": "labels",
    "stylers": [
      {
        "visibility": "off"
      }
    ]
  },
  {
    "featureType": "poi",
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "color": "#93817c"
      }
    ]
  },
  {
    "featureType": "poi.park",
    "elementType": "geometry.fill",
    "stylers": [
      {
        "color": "#a5b076"
      }
    ]
  },
  {
    "featureType": "poi.park",
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "color": "#447530"
      }
    ]
  },
  {
    "featureType": "road",
    "elementType": "geometry",
    "stylers": [
      {
        "color": "#f5f1e6"
      },
      {
        "visibility": "simplified"
      }
    ]
  },
  {
    "featureType": "road",
    "elementType": "labels",
    "stylers": [
      {
        "visibility": "simplified"
      }
    ]
  },
  {
    "featureType": "road.arterial",
    "elementType": "geometry",
    "stylers": [
      {
        "color": "#fdfcf8"
      }
    ]
  },
    {
        "featureType": "road.highway",
        "elementType": "labels",
        "stylers": [
          {
            "visibility": "off"
          }
        ]
    },
  {
    "featureType": "road.highway",
    "elementType": "geometry",
    "stylers": [
      {
        "color": "#f8c967"
      }
    ]
  },
  {
    "featureType": "road.highway",
    "elementType": "geometry.stroke",
    "stylers": [
      {
        "color": "#e9bc62"
      }
    ]
  },
  {
    "featureType": "road.highway.controlled_access",
    "elementType": "geometry",
    "stylers": [
      {
        "color": "#e98d58"
      }
    ]
  },
  {
    "featureType": "road.highway.controlled_access",
    "elementType": "geometry.stroke",
    "stylers": [
      {
        "color": "#db8555"
      }
    ]
  },
  {
    "featureType": "road.local",
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "color": "#806b63"
      }
    ]
  },
  {
    "featureType": "transit",
    "elementType": "labels",
    "stylers": [
      {
        "visibility": "off"
      }
    ]
  },
  {
    "featureType": "transit.line",
    "elementType": "geometry",
    "stylers": [
      {
        "color": "#dfd2ae"
      }
    ]
  },
  {
    "featureType": "transit.line",
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "color": "#8f7d77"
      }
    ]
  },
  {
    "featureType": "transit.line",
    "elementType": "labels.text.stroke",
    "stylers": [
      {
        "color": "#ebe3cd"
      }
    ]
  },
  {
    "featureType": "transit.station",
    "elementType": "geometry",
    "stylers": [
      {
        "color": "#dfd2ae"
      }
    ]
  },
  {
    "featureType": "water",
    "elementType": "geometry.fill",
    "stylers": [
      {
        "color": "#b9d3c2"
      }
    ]
  },
  {
    "featureType": "water",
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "color": "#92998d"
      }
    ]
  }
];


function initMap() {

  gMap = new google.maps.Map(document.getElementById('map'));

  //Default location if location of user is not found --Defualt location set to stuyvesant
  var user_lat;
  var user_lng;

  zoomL = 15;

  var radius = zoom_to_miles(zoomL);
  var cirRadius = zoom_to_radius(zoomL);

  navigator.geolocation.getCurrentPosition(function(position) {
    // Center on user's current location if geolocation prompt allowed
      var user_lat = position.coords.latitude;
      var user_lng = position.coords.longitude;

    var initialLocation = new google.maps.LatLng(user_lat, user_lng);
    gMap.setCenter(initialLocation);
    gMap.setZoom(zoomL);
    gMap.setOptions({styles: map_styles_array, disableDefaultUI: true});

      addMarker(initialLocation, gMap, user_marker_icon);

      //Getting markers drawing circle
      get_Markers(user_lat, user_lng, radius, gMap);

      //adding search circle
      // addCircle(user_lat,user_lng,gMap,cirRadius);

  }, function(positionError) {
    // User denied geolocation prompt - default to Stuyvesant
    var user_lat = 40.717892;
    var user_lng = -74.013908;
    var initialLocation = new google.maps.LatLng(user_lat, user_lng);
    gMap.setCenter(initialLocation);
    gMap.setZoom(zoomL);
    gMap.setOptions({styles: map_styles_array, disableDefaultUI: true});

      addMarker(initialLocation, gMap, user_marker_icon);

      //Getting markers drawing circle
      get_Markers(user_lat, user_lng, radius, gMap);

      //adding search circle
      // addCircle(user_lat,user_lng,gMap,cirRadius);
  });

  addListener(gMap);

}

//add Marker function
function addMarker(location, map, icon) {
    marker = new google.maps.Marker({
        position: location,
        map: map,
        icon: icon
    });
}

function addWaterMarker(location, map, icon, name, status, type, dist, comments, ratings){
  marker = new google.maps.Marker({
        position: location,
        map: map,
        icon: icon,
        name:name,
        status:status,
        type:type,
        dist:dist,
        comments:comments,
        ratings:ratings
    });

  markersArray.push(marker);

}

//delete marker function
function clearMarkers(){
    for (var i = 0; i < markersArray.length; i++){
      markersArray[i].setMap(null);
    }
    markersArray.length = 0;
}

//allowing all the markers to be clicked and subsequently display something
function addClickEvent(){
  if (markersArray.length > 0){
    markersArray.forEach(function(item, index){
      item.addListener('click', function(){
        var infoBox = document.getElementById('fountain_detail');
        var childs = infoBox.children;
        childs[0].innerHTML = item['name'];
        childs[1].innerHTML = item['status'];
        childs[2].innerHTML = item['type'];
        childs[3].innerHTML = item['comments'];
        infoBox.style.visibility = 'visible';

        console.log(childs);
      });

    });
  }
}

//Drawing circle with the search radius
function addCircle(lat, lon, map, r){
    circle = new google.maps.Circle({
    center:new google.maps.LatLng(lat, lon),
    radius: r,
    strokeColor:'#113788',
    strokOpacity:0.6,
    strokeWeight:2,
    fillColor:'#FFCC00',
    fillOpacity:0.4
  });

  circle.setMap(map);
}

//delete search circle from the map
function deleteCircle(){
  circle.setMap(null);
}

// CONVERSION FROM ZOOM LEVEL TO MILES FOR SEARCH RADIUS
function zoom_to_miles(zoom_level){
  return Math.pow(2, (-(zoomL) + 14.679));
}

function zoom_to_radius(zoom_level){
  return (zoom_to_miles(zoom_level) / 0.00062137);
}


// GETIING THE FUCNTION WITHIN THE GIVEN RANGE
function get_Markers(lat, lon, dist_range, map){
  $.get('/get_markers', {'lat':lat, 'lon':lon, 'dist_range': dist_range}, function(data){
    if (data.length > 0){
      console.log(data[0]);
      data.forEach(function (item, index) {
        marker_LatLng = new google.maps.LatLng(item['lat'],item['lon']);
        var name = item['name'];
        var status = item['status'];
        var type = item['type'];
        var dist  = item['dist'];
        var comments = item['comments'];
        var ratings = item['ratings']


        addWaterMarker(marker_LatLng, map, water_marker_icon, name, status, type, dist, comments, ratings);

      });

      //adding click function to all the water markers
      addClickEvent();

    }else{
      alert('No fountains found. Please increase your search area or search a different region.');
    }

  });
}



function addListener(map) {
  var idle;
  var drag = false;
  var zoom = false;
  initCall = true;

  map.addListener('dragend', function(){
    drag = true;
  });

  map.addListener('zoom_changed', function(){
    if (initCall){
      initCall = false;
    }else{
      console.log('zoomChanged');
      zoom = true;
    }
  });


  map.addListener('bounds_changed', function() {
    if (drag || zoom){
      idle = false;
      drag = false;
      zoom = false;
    }
  });

  map.addListener('idle', function(){
    if (idle == false) {
      console.log('alert');
      document.getElementById('redo-search').style.visibility = 'visible';
      idle = true;
    }
  });

  document.getElementById('redo-search').addEventListener('click', function(){
    console.log('button-clicked');
    console.log(map.getCenter().lat());
    map_center = map.getCenter();
    zoomL = map.getZoom();
    radius = zoom_to_miles(zoomL);
    this.style.visibility = 'hidden';

    clearMarkers();
    deleteCircle();

    get_Markers(map_center.lat(), map_center.lng(), radius, map);
    addCircle(map_center.lat(), map_center.lng(), map, zoom_to_radius(zoomL));


  });

}
