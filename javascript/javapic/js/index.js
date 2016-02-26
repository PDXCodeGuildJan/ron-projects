//create a new array were the images will be stored for display on index.html


//var mySlides = ['images/pdxcg_01.jpg','images/pdxcg_02.jpg','images/pdxcg_03.jpg','images/pdxcg_04.jpg','images/pdxcg_05.jpg','images/pdxcg_06.jpg']
slide = 0


//auto rotate the images sequencially
function rotateSlide(i){



    if (i < 10){
        var mySlides = "images/pdxcg_0" + i + ".jpg";
        i++;
    }
    if(i > 9){
        var mySlides = "images/pdxcg_" + i + ".jpg";
        i++;
        if( i===42){
            i++;
        }
    }

    document.getElementById("jumbotron").style.backgroundImage = "url(" + mySlides + ")";  


    if (i > 60) {

        i = 1;
        
    }
    console.log(mySlides);
    console.log(i);
    setTimeout(rotateSlide, 1000, i);
    //console.log("first value is slide 2nd value is length of mySlides", slide, mySlides.length);

}

//window.onload = setInterval(rotateSlide(1), 3000);

//document.getElementById("jumbotron").style.backgroundImage = "url('" + mySlides "[" + slide + "]" + "')";


