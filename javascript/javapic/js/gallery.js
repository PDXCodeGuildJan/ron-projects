//create a gallery of thumbnails from the images directory and enlarge one individual image at a time in a lightbox




function gallery(){

    for (i = 1; i <= 60; i++){

        //create a string adding the images directory and looping through the filename numbers

        //loop through images 1-9 due to the extra character space added after the number 9
        if (i < 10){
            var mySlides = "images/pdxcg_0" + i + ".jpg";

        }

        //loop through all image after the number 9
        if(i > 9){
            var mySlides = "images/pdxcg_" + i + ".jpg";


            //ignore missing file 42 and keep going
            if( i===42){
                continue;
            }
        }
        console.log(mySlides)
        //create an <li> in javascript
        var li = document.createElement("LI");

        //create an image in javascript
        var img = document.createElement("IMG");
        img.setAttribute("src", mySlides);

        //place the image in the <li> 
        li.appendChild(img);

        //place the <li> in the gallery
        document.getElementById("gallery").appendChild(li);

        
    }
}

window.onload = gallery;



    //document.getElementById("gallery").style = " + mySlides + ;  

    //document.getElementById("gallery").getElementsByTagName("li").innerHTML = + mySlides(0) +;
    //document.getElementById("gallery").appendChild(mySlides(0)) //= + mySlides(0) +;

    /*
    when the loop gets to the end of the images return to image 1 to keep looping
    if (i > 60) {

        i = 1;
        
    }
    */

