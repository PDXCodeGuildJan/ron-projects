//disable built in browser form validation. shotgun approach if all else fails
/*
for(var f=document.forms,i=f.length;i--;)
	f[i].setAttribute("novalidate",i)
*/

var submitBtn = document.getElementById("submit");

submitBtn.onclick = submit;

function submit(e) {
    //kill built-in browser validation
    var form = document.getElementById("signup");
    form.noValidate=true;


    var name = document.forms["signup"]["name"].value;
    var username = document.forms["signup"]["username"].value;
    var email = document.forms["signup"]["email"].value;
    //var formFailure 
    console.log(name, username, email);


    if (name === "") {
        alert("Name must be filled out");
    }
    //regex not working yet
    var regexName = "/^(?:[-A-Z]+\.? )+[-A-Z]+$/i";
        if (regexName.test(name)){
            alert("Incomplete name entered. Please type a name a-z in lower or uppercase");
        }


    if (username ===""){
        alert("Username must be filled out");
    }


    if (email ===""){
        alert("Username must be filled out");
    }


}



/*
function validateName(){

    document.getElementById("signup").noValidate = true;
    //returns true if matched, validates for a-z, A-Z, white space and periods
    /^(?:[-A-Z]+\.? )+[-A-Z]+$/i.test(x)

}
*/




/*

//validate an empty form field

function IsEmpty(objectfield,stringfield)
{
    objectvalue = objectfield.value.length;
    if(objectvalue=="")
    {
        alert("Oops.. Please fill out the value of " + stringfield);
        objectfield.style.background = 'Red';
        return false;
    }
    else
        return true;
}



//validate an email address

function validate_email(field,alerttxt)
{
    with (field)
    {
        apos = value.indexOf("@");
        dotpos = value.lastIndexOf(".");
        if (apos < 1 || dotpos - apos < 2){
            alert(alerttxt);
            return false;
        }
        else {
            return true;
        }
    }
}

*/


