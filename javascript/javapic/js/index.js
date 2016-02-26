



//create a new array were the images will be stored for display on index.html
mySlides = new Array('images/pdxcg_01.jpg','images/pdxcg_02.jpg','images/pdxcg_03.jpg', 'images/pdxcg_04.jpg', 'images/pdxcg_05.jpg' , 'images/pdxcg_06.jpg')
slide = 0


//auto rotate the images sequencially
function rotateSlide(slide){


    var pic = document.getElementById("jumbotron").style.backgroundImage = "url('" + mySlides "[" + slide + "]" + "')";
    console.log(pic);
    console.log(slide);
    
    if (slide < 5){ 
        slide++
    }
    if (slide == mySlides.length) {
        slide = 0
    }

/*
    if (slide == slide + mySlides){ 
        slide++
    }
    if (slide == mySlides.length) {
        slide = 0
    }
*/

    //var displaySlide = "images/"+ mySlides[slide]
    //var jumbotron = document.getElementsByClassName("jumbotron");
    //jumbotron.innerHTML =+ displaySlide


    //document.getElementById("jumbotron").style.backgroundImage = "url('images/' + mySlides[slide])";

    //"url('images/' + mySlides[slide] )";
    setInterval(rotateSlide, 5000);

}



document.onclick = rotateSlide(slide);

























//ALTERNATIVE METHOD of hardcoding - old school?


/*var howOften = 5; //number often in seconds to rotate
var current = 0; //start the counter at 0
//var ns6 = document.getElementById&&!document.all; //detect netscape 6

// place your images, text, etc in the array elements here
var items = new Array();
    items[0]="<a href='index.htm' ><img alt='image0 (9K)' src=' /images/pdxcg_01.jpg' /></a>"; 
    items[1]="<a href='index.htm'><img alt='image1 (9K)' src='/images/pdxcg_02.jpg'  /></a>"; 
    items[2]="<a href='index.htm'><img alt='image2 (9K)' src='/images/pdxcg_03.jpg' /></a>"; 
    items[3]="<a href='index.htm'><img alt='image3 (9K)' src='/images/pdxcg_04.jpg' /></a>"; 
    items[4]="<a href='index.htm'><img alt='image4 (9K)' src='/images/pdxcg_05.jpg' /></a>"; 
    items[5]="<a href='index.htm'><img alt='image5 (18K)' src='/images/pdxcg_06.jpg' /></a>"; 
function rotater() {
    document.getElementById("placeholder").innerHTML = items[current];
    current = (current==items.length-1) ? 0 : current + 1;
    setTimeout("rotater()",howOften*1000);
}

function rotater() {
    if(document.layers) {
        document.placeholderlayer.document.write(items[current]);
        document.placeholderlayer.document.close();
    }
    if(ns6)document.getElementById("placeholderdiv").innerHTML=items[current]
        if(document.all)
            placeholderdiv.innerHTML=items[current];

    current = (current==items.length-1) ? 0 : current + 1; //increment or reset
    setTimeout("rotater()",howOften*1000);
}

window.onload=rotater;
*/
