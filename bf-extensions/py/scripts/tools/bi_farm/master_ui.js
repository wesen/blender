// Maintanance message
// alert("FARM IS UNDER MAINTANANCE - DO NOT SUBMIT ANY JOB PLEASE");

function request(url, data)
{
	xmlhttp = new XMLHttpRequest();
	xmlhttp.open("POST", url, false);
	xmlhttp.send(data);
	window.location.reload()
}

