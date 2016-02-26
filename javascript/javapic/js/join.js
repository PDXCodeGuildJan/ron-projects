//disable built in browser form validation
for(var f=document.forms,i=f.length;i--;)
	f[i].setAttribute("novalidate",i)

/*
returns true if matched, validates for a-z and A-Z and white space
/^[A-Za-z ]+$/.test(x)

*/

//vaidate an empty form field

function IsEmpty(objectfield,stringfield)
{
    objectvalue = objectfield.value.length;
    if(objectvalue=="")
    {
        alert("Oops.. Please fill out the value of "+stringfield);
        objectfield.style.background = 'Yellow';
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
        apos=value.indexOf("@");
        dotpos=value.lastIndexOf(".");
        if (apos<1||dotpos-apos<2){
            alert(alerttxt);return false;
        }
        else {
            return true;
        }
    }
}


//validate a password

function validatePassword(fld) {
    var error = "";
    var illegalChars = /[\W_]/; // allow only letters and numbers
 
    if (fld.value == "") {
        fld.style.background = 'Yellow';
        error = "You didn't enter a password.\n";
        alert(error);
        return false;
 
    } else if ((fld.value.length < 7) || (fld.value.length > 15)) {
        error = "The password is the wrong length. \n";
        fld.style.background = 'Yellow';
        alert(error);
        return false;
 
    } else if (illegalChars.test(fld.value)) {
        error = "The password contains illegal characters.\n";
        fld.style.background = 'Yellow';
        alert(error);
        return false;
 
    } else if ( (fld.value.search(/[a-zA-Z]+/)==-1) || (fld.value.search(/[0-9]+/)==-1) ) {
        error = "The password must contain at least one numeral.\n";
        fld.style.background = 'Yellow';
        alert(error);
        return false;
 
    } else {
        fld.style.background = 'White';
    }
   return true;
}



