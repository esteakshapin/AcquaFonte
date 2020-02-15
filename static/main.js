$(document).ready(function () {
  $('#submit').click(function (){
    const username = $('#username').val();
    const password = $('#password').val();
    $.post('/log_in', {
      username:username,
      password:password
      }).done(function(){
        document.location.reload();
      });
  });
  $('#register_submit').click(function (){
    const username = $('#register_username').val();
    const password = $('#register_password').val();
    const confirm_pass = $('#confirm_pass').val();
    $.post('/register', {
      username:username,
      password:password,
      confirm_pass:confirm_pass
      }).done(function(){
        document.location.reload();
      });
  });
});
