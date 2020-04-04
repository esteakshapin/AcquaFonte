function togglehamburger() {
  // let ham = document.querySelector('.hamburger');
  // let menu = document.querySelector('.menuitems');
  // console.log('toggle menu')
  // ham.classList.toggle("menuon");
  // menu.classList.toggle("menuon");

  //new nav bar system
  openNav();
}
/* Set the width of the side navigation to 250px */
function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
  document.getElementById('blackout').style.display = 'block';
  document.getElementById('blackout').style.backgroundColor= 'rgb(0,0,0,.6)';
}

/* Set the width of the side navigation to 0 */
function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  document.getElementById('blackout').style.display = 'none';
}
jQuery('html').bind('click', function(e) {
    sidenavL = $('.sidenav').width();
    if(jQuery(e.target).closest('.sidenav').length == 0 && sidenavL > 0) {
        // click happened outside of .navbar, so hide

        closeNav();
    }
});
