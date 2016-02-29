

//the following hard coded approach was in elegant
//create a new array were the images will be stored for display on index.html
//var mySlides = ['images/pdxcg_01.jpg','images/pdxcg_02.jpg','images/pdxcg_03.jpg','images/pdxcg_04.jpg','images/pdxcg_05.jpg','images/pdxcg_06.jpg']




//create a function that assembles a string based on the filename of the images then loop through them
//auto rotate the images sequencially through their filenames
function rotateSlide(i){


    //create a string adding the images directory and looping through the filename numbers

    //loop through images 1-9 due to the extra character space added after the number 9
    if (i < 10){
        var mySlides = "images/pdxcg_0" + i + ".jpg";
        i++;
    }

    //loop through all image after the number 9
    if(i > 9){
        var mySlides = "images/pdxcg_" + i + ".jpg";
        i++;

        //ignore missing file 42 and keep going
        if( i===42){
            i++;
        }
    }

    //replace the hard coded background-image in the CSS with the variable mySlides
    document.getElementById("jumbotron").style.backgroundImage = "url(" + mySlides + ")";  

    //when the loop gets to the end of the images return to image 1 to keep looping
    if (i > 60) {

        i = 1;
        
    }
    //console.log(mySlides);
    //console.log(i);

    //recursive call. setInterval wasn't working correctly
    setTimeout(rotateSlide, 5000, i);



}


//window.onload = setInterval(rotateSlide(1), 3000);

//document.getElementById("jumbotron").style.backgroundImage = "url('" + mySlides "[" + slide + "]" + "')";


