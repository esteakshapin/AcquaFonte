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
				const newprofilepic = $('#profilepic').val()

    var form = $('.accountForm')[0];
    var fd = new FormData(form);

    if (!newUsername == curUsername || newUsername == "" || newUsername == Undefined){
      fd.append('newUsername', newUsername);
						sendRequest = true;
					}
				if (!newFirst == curFirst || newFirst == "" || newFirst == Undefined){
		    fd.append('newFirst', newFirst);
						sendRequest = true;
					}
				if (!newLast == curLast || newLast == "" || newLast == Undefined){
		    fd.append('newLast', newLast);
						sendRequest = true;
					}
				if (!newprofilepic == Undefined){
					fd.append('newprofilepic', newprofilepic);
					sendRequest = true;
				}
				if (sendRequest){
					$.ajax({
							type : 'POST',
							url : '/',
							data: fd,
							processData: false,  // tell jQuery not to process the data
							contentType: false,   // tell jQuery not to set contentType
							success: function(data) {
									console.log(data)
									if (data == "success"){
											document.location.reload();
											console.log("push to backend");
											alert("");
									}else {
										console.log('test');
											alert(data);
									}

							},
					});
				}
				else {
					console.log("No edits were made, canceling changes");
				}



				var form = $('#toGCS')[0]
				var GCS = new FormData(form)


  });
});
