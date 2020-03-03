$(function() {
  $('.button2').hover(function() {
    $('.image-new').css('width', '100%');
    $('h1').css('color', 'black');

  }, function() {
    // on mouseout, reset the background colour
    $('.image-new').css('width', '0%');
    $('h1').css('color', '#00adb5');
  });
});
