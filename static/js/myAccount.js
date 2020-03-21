document.getElementById("editAccount").onclick = openForm;
var open = false;

function openForm(){
	if (open == false){
		open = true;
		document.getElementById("showEdit").style.display = "block";
		document.getElementById("closeForm").onclick = closeForm;
	}
	else{
		closeForm()
	}
}

function closeForm(){
	open = false;
	document.getElementById('showEdit').style.display = 'none';
}

$(document).ready(function () {
	 $('#log_out').click(function (){
			$.post('/log_out',{})
			.done(function(x){
					window.location.href = '/';
			});
	 });
  $('#submit').click(function (){
				var sendRequest = false;
			 	const curUsername = $('#cusername').val();
    		const newUsername = $('#username').val();
				console.log(newUsername);
				const curFirst = $('#cfirstname').val();
				const newFirst = $('#firstname').val();
				console.log(newFirst);
				const curLast = $('#clastname').val()
				const newLast = $('#lastname').val();
				console.log(newLast);
				const newprofilepic = $('#profilepic').prop('files')[0];
				console.log(newprofilepic);

    var form = $('.accountForm')[0];
    var fd = new FormData(form);

    if (newUsername != curUsername && newUsername != "" && newUsername != undefined){
						console.log('form includes user');
						fd.append('newUsername', "true");
						sendRequest = true;
		}else {
			fd.append('newUsername', "false");
		}
		if (newFirst != curFirst && newFirst != "" && newFirst != undefined){
				console.log('form includes first');
				sendRequest = true;
				fd.append('newFirst', "true");
			}else {
				fd.append('newFirst', "false");
			}
		if (newLast != curLast && newLast != "" && newLast != undefined){
				console.log('form includes last');
				sendRequest = true;
				fd.append('newLast', "true");
			}else {
				fd.append('newLast', "false");
			}
		if (newprofilepic != undefined){
			console.log('form includes pic 2,0');
			sendRequest = true;
			fd.append('newPFP', "true");
		}else {
			fd.append('newPFP', "false");
		}


		if (sendRequest){
			$.ajax({
        type : 'POST',
        url : '/myAccount',
        data: fd,
        processData: false,  // tell jQuery not to process the data
        contentType: false,   // tell jQuery not to set contentType
        success: function(data) {
          if (data == "success"){
            alert("edits successful");
						window.location.reload(true);
          }else {
            alert(data);
						window.location.reload(true);
          }
        },
        error: function(e) {
         console.log(e);
        }
      });
		}
		else {
			alert("No edits were made, canceling changes");
		}

				//
				//
				// var form = $('#toGCS')[0]
				// var GCS = new FormData(form)


  });
});
