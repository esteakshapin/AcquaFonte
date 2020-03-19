$(document).ready(function () {
  $('#submit').click(function (){
    const username = $('#username').val();
    const password = $('#password').val();
    $.post('/log_in', {
      username:username,
      password:password
     }).done(function(x){
        window.location.href = '/';
      });
  });
  $('#log_out').click(function (){
    $.post('/log_out',{}).done(function(x){
      window.location.href = '/';
    });
  });
  $('#register_submit').click(function (x){
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
      })
      //.done(function(){
        //document.location.reload();
      //});
  });
  $('#register_form').click(function(){
    $(".register-form").css('display', 'inherit');
    $(".login-form").css('display', 'none');
  });
  $('#login_form').click(function(){
    $(".register-form").css('display', 'none');
    $(".login-form").css('display', 'inherit');
  });
});
