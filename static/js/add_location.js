var water_marker_icon = "/static/find_water/water_marker_icon.svg";
var fountain_marker;
var rating_num = 0;
//Default location if location of user is not found --Defualt location set to stuyvesant
var fountian_lat;
var fountian_lng;
var submitApproved = false
var diffrentOrigin = false
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

    if (!diffrentOrigin){
      fountian_lat = position.coords.latitude;
      fountian_lng = position.coords.longitude;
    }
    // else{
    //   changeForm()
    // }
    var initialLocation = new google.maps.LatLng(fountian_lat, fountian_lng);
    gMap.setCenter(initialLocation);
    gMap.setZoom(zoomL);
    gMap.setOptions({styles: map_styles_array, disableDefaultUI: true});

      addMarker(initialLocation, gMap, water_marker_icon);
      if (!diffrentOrigin){
        addListener(gMap);
      }
  }, function(positionError) {
    // User denied geolocation prompt - default to Stuyvesant

    if (!diffrentOrigin){
      fountian_lat = 40.717892;
      fountian_lng = -74.013908;
    }
    var initialLocation = new google.maps.LatLng(fountian_lat, fountian_lng);
    gMap.setCenter(initialLocation);
    //   changeForm()
    // }
    gMap.setZoom(zoomL);
    gMap.setOptions({styles: map_styles_array, disableDefaultUI: true});

      addMarker(initialLocation, gMap, water_marker_icon);
    if (!diffrentOrigin){
      alert("Couldn't find your location. Please make sure your location services are enabled and try again.");
      addListener(gMap);
    }
  }
);

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
  console.log('add listener');
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

function checkValue(value){
    $('input[name="status"]').each(function(){
      console.log(this.value);
      if (this.value == value){
        this.checked = true;
      }
      return 'checked box'
    })
}
function changeForm(){
  console.log('looking at meta data');
  // var prelat
  // var prelon
  if (! $("#fountaindata").length){
    initMap()
    console.log('no data');
    return('finished')
  }
  $("#fountaindata").each(function(){
    $.each(this.attributes, function(){
      if (this.specified) {
        // console.log(value);
        console.log(this.name, this.value);
        if (this.name == '_id'){
          submitApproved = this.value
        }
        // if (this.name == 'comments'){
        //   $('#fountain_comment').val(this.value).prop('disabled', true);
        //
        // }

        if (this.name == 'status'){
          if (this.value == 'Active'){
            console.log('working');
             checkValue('working');
            }else{
            console.log('not working');
            checkValue('not Working');
        }
      }
// ratings WIP
        if (this.name == 'ratings'){
          console.log(this.value);
          // if (this.value == 0){
          //   stars(1)
          // }//testing it works!!
          // else {
            stars(this.value)
          // }
        }
        if (this.name == "type"){
          console.log(this.value);

        }
        if (this.name == 'lat'){
          console.log('latfound');
          fountian_lat = this.value
        }
        if (this.name == 'lon'){
          console.log('lonfound');
          fountian_lng = this.value
        }
        if (fountian_lat && fountian_lng && ! diffrentOrigin){
          console.log('initing map');
          diffrentOrigin = true
          initMap()
        }
        // else{
        //   console.log('data has no lat/lon, fake request/exiting');
        //   initMap()
        // }
        if (this.name == 'type'){ // type not done, waiting for name changes

          // if this.value == XXX => A, b,c,d,e
          $('#inputDefault').prop('selected', false)

          // temp for testing
          $('#A').prop('selected', true)
          $( '#B, #C, #D').prop('disabled', true)

        }
        if (this.name == 'name'){
          $('#fountain_name').val(this.value)
          $('#fountain_name').prop('disabled', true)
        }
        // if (this.name == 'type'){
        //   if (this.value==Pedestal){
        //     $('select[value="A"]')
        //   }
        // work in progress
        // }



      }


    })
  })
}

$(document).ready(function () {
  changeForm();
  $('#fountain_submit').click(function (){
//need status, rating//, img
    const rating = rating_num;
    var radioButton = document.getElementsByName('status');
    comment = $('#fountain_comment').val();
    const status = (function(){
      for(i = 0; i < radioButton.length; i++) {
        if (radioButton[i].checked){
          return radioButton[i].value;
        }
      };
    })();

    var feildsEmpty = true;

    if (rating == 0) { //a
      alert('please give this fountian a rating');
      feildsEmpty = true;
    }
    if (status == undefined) {
      alert('please select the status of this fountian');
      feildsEmpty = true;
    }
     if (comment == "") {//b
        alert('please provide some comments for the fountain');
        feildsEmpty = true;
    }
    else{
      feildsEmpty = false;
    }

    if (!submitApproved){ //need status, img, radio
      fountain_name = $('#fountain_name').val();
      type = $('#fountain_type').val();
      formlat = fountian_lat;
      formlng = fountian_lng;

      if (fountain_name == ""){
        alert('please enter a name for the fountain');
        feildsEmpty = true;
      }else if (type == null) {//b
        alert('please select a type for this fountian');
        feildsEmpty = true;
      }else {
        feildsEmpty = false;
      }
    }

    var form = $("#fountain-form")[0];
    var fd = new FormData(form);

    if (!feildsEmpty){
      fd.append('rating',rating);
      fd.append('status',status);
      if (!submitApproved) {
        fd.append('type', type);
        fd.append('lat', formlat);
        fd.append('lng', formlng);

      }
      else {
        fd.append('_id', submitApproved)
      }

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
         console.log();(e);
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
