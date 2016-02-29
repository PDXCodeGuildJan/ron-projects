function lightbox(i){


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