$(function() {
  $('.button1').hover(function() {
    $('.img-new').css('width', '100%');
    $('h1').css('color', 'black');
  }, function() {
    // on mouseout, reset the background colour
    $('.img-new').css('width', '0%');
    $('h1').css('color', '#00adb5');
  });
});
$(document).ready(function () {
  var a = $( '#original-img-id' ).css('width');
  $('#new-img-id').css('width', a);
})
