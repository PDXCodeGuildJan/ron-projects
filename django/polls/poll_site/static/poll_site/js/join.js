//validate name, username and email address of the signup form and upon successful signup 
//redirect the user to the gallery page with their name appended to the gallery tagline 


var submitBtn = document.getElementById("submit");

submitBtn.onclick = submit;


function submit() {
    //kill built-in browser validation
    var form = document.getElementById("signup");
    form.noValidate=true;


    var name = document.forms["signup"]["name"].value;
    var username = document.forms["signup"]["username"].value;
    var email = document.forms["signup"]["email"].value;
    //var formFailure 
    console.log(name, username, email);

	//validate name text field
    if (name === "") {
        alert("Name must be filled out");
		//document.forms["signup"]["name"].focus();
		return false;
    }
    //regular expression to match only alpha characters and spaces
    var reName = /^[a-zA-Z ]+$/;

	//console.log("value of reName is ", reName.test(name));
	
	if (!(reName.test(name))){
		//successful validation
		//return true;

		alert("Incomplete name entered. Please type a name a-z in lower or uppercase");
		//document.forms["signup"]["name"].focus();
		return false;
    }



	//validate username text field
    if (username === ""){
		alert("Error: Username must contain only alphanumeric characters!");
		//document.forms["signup"]["username"].focus();
		return false;
    }

    //regular expression to match only alphanumeric characters and underscores
    var reUsername = /^[0-9a-zA-Z]+$/;


	if (!(reUsername.test(username))){
		//successful validation

		alert("Error: Username must contain only alphanumeric characters");
		//document.forms["signup"]["username"].focus();
		return false;
		}



	//validate email text field
    if (email === ""){
        alert("Email must be filled out");
		//document.forms["signup"]["email"].focus();
		return false;
    }
	//regular expression to validate an email
	var reEmail = /^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/;
	
	if (reEmail.test(email)){
		//successful validation
		alert("Login Successful");
        setTimeout(function() {window.location.href = "gallery.html?" + name;});

	}	else{
		
		alert("Invalid email address entered. Example; yourname@yourdomain.com ");
		//document.forms["signup"]["email"].focus();
		event.preventDefault()
		return false;
		}




}





        

