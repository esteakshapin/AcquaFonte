var water_marker_icon = "/static/find_water/water_marker_icon.svg";
var fountain_marker;
var rating_num = 0;
//Default location if location of user is not found --Defualt location set to stuyvesant
var fountian_lat;
var fountian_lng;

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


  zoomL = 18;

  navigator.geolocation.getCurrentPosition(function(position) {
    // Center on user's current location if geolocation prompt allowed
      fountian_lat = position.coords.latitude;
      fountian_lng = position.coords.longitude;

    var initialLocation = new google.maps.LatLng(fountian_lat, fountian_lng);
    gMap.setCenter(initialLocation);
    gMap.setZoom(zoomL);
    gMap.setOptions({styles: map_styles_array, disableDefaultUI: true});

      addMarker(initialLocation, gMap, water_marker_icon);
      addListener(gMap);

  }, function(positionError) {
    // User denied geolocation prompt - default to Stuyvesant
    fountian_lat = 40.717892;
    fountian_lng = -74.013908;

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
    fountain_lng = marker.getPosition().lng();
    fountian_lat = marker.getPosition().lat();
  });
}

function stars(num){
  rating_num = num;

  var star_class = document.getElementsByClassName('stars');

  for(i = 0; i < star_class.length; i++){
    star_class[i].innerHTML = "☆";
    star_class[i].style.color = "black"
  }

  for (i = 1; i < num+1; i++){
    var starElement = document.getElementById(i);
    $(starElement).css('color',"#FFCC00");
    starElement.innerHTML = "&#9733;";

  }
}

$(document).ready(function () {
  $('#fountain_submit').click(function (){
    var radioButton = document.getElementsByName('status');
    var feildsEmpty = true;
    const fountain_name = $('#fountain_name').val();
    const comment = $('#fountain_comment').val();
    const type = $('#fountain_type').val();
    const rating = rating_num;
    const lat = fountian_lat;
    const lng = fountian_lng;
    const status = (function(){
      for(i = 0; i < radioButton.length; i++) {
        if (radioButton[i].checked){
          return radioButton[i].value;
        }
      };
    })();

    var form = $("#fountain-form")[0];
    var fd = new FormData(form);

    if (fountain_name == ""){
      alert('please enter a name for the fountain');
      feildsEmpty = true;
    }else if (status == undefined) {
      alert('please select the status of this fountian');
      feildsEmpty = true;
    }else if (type == null) {
      alert('please select a type for this fountian');
      feildsEmpty = true;
    }else if (comment == "") {
      alert('please provide some comments for the fountain');
      feildsEmpty = true;
    }else if (rating == 0) {
      alert('please give this fountian a rating');
      feildsEmpty = true;
    }else {
      feildsEmpty = false;
    }

    if (!feildsEmpty){
      fd.append('type', type);
      fd.append('rating',rating);
      fd.append('status',status);
      fd.append('lat',lat);
      fd.append('lng',lng);
      console.log('hello',fountian_lat,fountian_lng);

      $.ajax({
        type : 'POST',
        url : '/add_location',
        data: fd,
        processData: false,  // tell jQuery not to process the data
        contentType: false,   // tell jQuery not to set contentType
        success: function(data) {
          if (data == "success"){
            alert("Fountain successfully added!!");
            window.location.reload(true);
          }else {
            alert(data);
          }
        },
        error: function(e) {
         alert(e);
        }
      });
    }


    // $.post('/add_location', {
    //   username:username,
    //   password:password
    //   }).done(function(){
    //     document.location.reload();
    //   });
  });
});
