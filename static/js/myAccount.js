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
      fd.append('newUsername', newUsername);
						console.log('form includes user');
						sendRequest = true;
					}
				if (newFirst != curFirst && newFirst != "" && newFirst != undefined){
		    fd.append('newFirst', newFirst);
						console.log('form includes first');
						sendRequest = true;
					}
				if (newLast != curLast && newLast != "" && newLast != undefined){
		    fd.append('newLast', newLast);
						console.log('form includes last');
						sendRequest = true;
					}
				if (newprofilepic != undefined){
					fd.append('newprofilepic', newprofilepic);
					console.log('form includes pic');
					sendRequest = true;
				}
				console.log(fd);
				if (sendRequest){
					$.ajax({
							type : 'POST',
							url : '/myAccount',
							data: fd,
							processData: false,  // tell jQuery not to process the data
							contentType: 'multipart/form-data',   // tell jQuery not to set contentType
							success: function(data) {
									console.log(data)
											alert(data);

							},
					});
				}
				else {
					console.log("No edits were made, canceling changes");
				}

				//
				//
				// var form = $('#toGCS')[0]
				// var GCS = new FormData(form)


  });
});
