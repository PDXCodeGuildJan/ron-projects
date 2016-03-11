//Establish the event listener for when they clck an item
//Add the click event handler to "add-item"
var addItemButton = document.getElementById("add-item");

addItemButton.onclick = addItem;

var addStockButton = document.getElementById("add-stock");

addStockButton.onclick = addStock;

var removeStockButton = document.getElementById("remove-stock");

removeStockButton.onclick = removeStock;

//initialize global variable that stores the inventory
var products =[];


/*toggle the inStock status on the selected rows inside of inventory*/

function addStock(){
	//NOT ALLOWED TO USE querySelectorAll()

	//create an empty list
	var checkboxes = [];


	//find all the selected items in the HTML list
	//grab all the items with checkboxes and put them into a list
	var input = document.getElementsByClassName("checkbox"); 
	//console.log(input);


	//loop through the list of all checkboxes and select only the checked=true items

	for (var i = 0; i < input.length; i++){

		if(input[i].checked){
			checkboxes.push(input[i]);


			var status = input[i].parentNode.parentNode.lastChild;

			console.log("Last item:", status);

			status.textContent = "Yes";
			status.className = "true";
		}
	}
	//console.log(checkboxes);

	//change their in-stock value

	//checkboxes[i].onchange = addStock;


	//update the display? depends on previous step. not adding quantity

}


function removeStock(){
	//use querySelectorAll()

	//create an empty list
	//var checkboxes = [];


	//find all the selected items in the HTML list
	//grab all the items with checkboxes and put them into a list

	var input = document.querySelectorAll('input:checked:not([id="in-stock"])');
	console.log(input)
	//var input = document.querySelectorAll('.checkbox');

/*	for (var i = 0; i < input.length; i++){

		if(input[i].checked){
			checkboxes.push(input[i]);
		
		}
	}*/

//console.log(input)

	for (var i=0; i < input.length; i++){
		var status = input[i].parentNode.nextSibling.nextSibling.nextSibling;
		console.log("Last item:", status);

		status.textContent = "No";
		status.className = "false";

		//alternative options
		//var status = selected[i].parentNode.parentNode.lastChild;
		//var status = selected[i].parentNode.parentNode.children[3];
	}

}






/*	Add the item in the text fields to the inventory
	list, which is in the table body (id="inventory")
 */
 function addItem(){
 	//console.log("Inside addItem function.");

 	var materialName = document.getElementById("name").value;
 	//console.log(materialName);
 	var priceName = document.getElementById("price").value;
 	//console.log(priceName);
 	var inStock = document.getElementById("in-stock").checked;
 	//console.log(inStock);

 	var inventory = document.getElementById("inventory");
 	var newRow = "<tr>" + "<td>" + "<input type='checkbox' class='checkbox'>" + "</td>" + "<td>" + materialName + "</td>" + "<td>" + priceName + "</td>" + "<td class=' " + inStock + "'>"; 
 	
 	if (inStock){
 		newRow += "Yes";
 	} else{
 		newRow += "No";
 	}
 	newRow += "</td></tr>";

 	

 	inventory.innerHTML += newRow; 

 	//create a new instance of the Product object with the new item's info
 	var newProd = new Product(materialName, priceName, inStock);
 	console.log(newProd);
 	products.push(newProd);
 }


/* Constructor for the Product object */
function Product(name, price, inStock){

	this.prodName = name;
	this.price = price;
	this.inStock = inStock;

	this.setStock = function (stock){
	this.inStock = stock;
	};
}


