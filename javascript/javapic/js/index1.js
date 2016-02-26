 var myImage = document.getElementById("jumbotron").style.backgroundImage;

 var imageArray = ["images/pdxcg_01.jpg","images/pdxcg_02.jpg","images/pdxcg_03.jpg",
  "images/pdxcg_04.jpg","images/pdxcg_05.jpg","images/pdxcg_06.jpg"];

 var imageIndex = 0; 

 function changeImage() 
{
  myImage.setAttribute("src",imageArray[imageIndex]);
  imageIndex++;
  if (imageIndex >= imageArray.length) {
    imageIndex = 0;
 }

}

setInterval(changeImage,5000);

window.onload = changeImage();