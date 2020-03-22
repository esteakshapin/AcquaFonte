function togglehamburger() {
  let ham = document.querySelector('.hamburger');
  let menu = document.querySelector('.menuitems');
  console.log('toggle menu')
  ham.classList.toggle("menuon");
  menu.classList.toggle("menuon");
}