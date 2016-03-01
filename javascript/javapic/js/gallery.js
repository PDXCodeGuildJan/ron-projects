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






function showLightbox(event) {

    if (event.target.nodeName === "IMG") {

        var element = document.getElementById("image_show")
        element.firstChild.src = event.target.src
        element.className = "display_img"

    }
    console.log(element.src)
    console.log(event.target.src)
    
}



function hideLightBox(){

    document.getElementById("image_show").className = "display_none"
}





document.getElementById('gallery').addEventListener('click', showLightbox);

//document.getElementById('image_show').removeEventListener('click', lightbox, false);





window.onload = gallery;













//document.getElementById("gallery").style = " + mySlides + ;  

