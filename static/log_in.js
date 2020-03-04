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
  $('#log_out').click(function (){
    $.post('/log_out',{}).done(function(){
      document.location.reload();
    });
  });
  $('#register_submit').click(function (){
    const first_name = $('#register_first_name').val();
    const last_name = $('#register_last_name').val();
    const username = $('#register_username').val();
    const password = $('#register_password').val();
    const confirm_pass = $('#confirm_pass').val();
    $.post('/register', {
      first_name:first_name,
      last_name:last_name,
      username:username,
      password:password,
      confirm_pass:confirm_pass
      }).done(function(){
        document.location.reload();
      });
  });
});
