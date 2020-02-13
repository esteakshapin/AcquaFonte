// $(document).ready(function () {
//   $('#submit').click(function (){
//     const username = $('#username').val();
//     const password = $('#password').val();
//     $.post('/log_in', {
//       username:username,
//       password:password
//       }).done(function(){
//         document.location.reload();
//       });
//   });
// });

function submit(){
  print('hello');
  const username = $('#username').val();
  const password = $('#password').val();
  $.post('/log_in', {
      username:username,
      password:password
      }).done(function(){
        document.location.reload();
      });
};