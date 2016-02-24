

var inputField = document.getElementById("num-loops")
var counter = document.getElementById("counter");

//make a random dice function that will roll a 6-sided die and return the result


function rollDie() {
    for (var i = 1; i <= inputField.value; i++) {
       var randomDie = Math.floor(6 * Math.random()) +1;

       //counter.innerHTML += randomDie + "<br/>";
       counter.innerHTML += "<img src='"+ randomDie + ".png' alt='A die. '/> <br/>"
       //counter.innerHTML += "img src='casino/" + randomDie + ".png' alt='A die. '/> <br/>"
       //counter.innerHTML += <img src="casino/" + randomDie + ".png">;
    }
}

// add click listener
document.getElementById("loop-btn").onclick = rollDie;



/*
//number of times we're going to loop
var number = 5;
	//print out the inputField
	//console.log(inputField);


	function loopClick(){
	number = inputField.value;
	//set it to an empty string
	counter.innerHTML = "";


	for (var i = 0; i < number; i++) {
		//print to the console log
		counter.innerHTML += i + "<br/>";
	};		
};
// add click listener
document.getElementById("loop-btn").onclick = onClick;

window['dice'+i].src = "dice/" + randomDice + ".jpg";
*/