var water_marker_icon = "/static/find_water/water_marker_icon.svg";
var fountain_marker;
var rating_num = 0;

var map_styles_array = (function () {
    var map_styles_array = null;
    $.ajax({
        'async': false,
        'global': false,
        'url': "/static/js/map_style.json",
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
      addListener(gMap);

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
      addListener(gMap);
  });

}

//add Marker function
function addMarker(location, map, icon) {
    marker = new google.maps.Marker({
        position: location,
        map: map,
        icon: icon
    });
    fountain_marker = marker;
}

function addListener(map) {
  map.addListener('center_changed', function(){
    fountain_marker.setPosition(map.getCenter());
  });
}

function stars(num){
  rating_num = num;
  for (i = 1; i < num+1; i++){
    var starElement = document.getElementById(i);
    $(starElement).css('color',"#113788");
    $(starElement).css('content',"'test'");

  }
}

$(document).ready(function () {
  $('#fountain_submit').click(function (){
    var radioButton = document.getElementsByName('status');
    const fountain_name = $('#fountain_name').val();
    const comment = $('#fountain_comment').val();
    const type = $('#fountain_type').val();
    const pic = $('#fountain_img_input').val();
    const status = (function(){
      for(i = 0; i < radioButton.length; i++) {
        if (radioButton[i].checked){
          return radioButton[i].value;
        }
      };
    })();



    console.log(fountain_name + comment + type + pic + status);
    // $.post('/add_location', {
    //   username:username,
    //   password:password
    //   }).done(function(){
    //     document.location.reload();
    //   });
  });
});
