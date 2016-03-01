//disable all built-in browser validation. shotgun approach if all else fails
/*
for(var f=document.forms,i=f.length;i--;)
	f[i].setAttribute("novalidate",i)
*/

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

	
	if (reName.test(name)){
		//successful validation
		return true;
	}	else{

		alert("Incomplete name entered. Please type a name a-z in lower or uppercase");
		//document.forms["signup"]["name"].focus();
		return false;
        }



	//validate username text field
    if (username === ""){
		alert("Error: Username must contain only letters, numbers and underscores!");
		//document.forms["signup"]["username"].focus();
		return false;
    }

    //regular expression to match only alphanumeric characters and underscores
    var reUsername = /^\w+$/;
	
	if (reUsername.test(username)){
		//successful validation
		return true;
	}	else{
		
		alert("Error: Username must contain only letters, numbers and underscores!");
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
		return true;
	}	else{
		
		alert("Invalid email address entered.");
		//document.forms["signup"]["email"].focus();
		return false;
		}
		
}

//document.forms["signup"]["name"].value
