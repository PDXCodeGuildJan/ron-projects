//Establish the event listener for when they clck an item
//Add the click event handler to "add-item"
var addItemButton = document.getElementById("add-item");

addItemButton.onclick = addItem;

var delItemButton = document.getElementById("del-item");

delItemButton.onclick = delItem;

var addStockButton = document.getElementById("add-stock");

addStockButton.onclick = addStock;

var removeStockButton = document.getElementById("remove-stock");

removeStockButton.onclick = removeStock;


window.onload = loadData;

//initialize global variable that stores the inventory
var products =[];


/*toggle the inStock status on the selected rows inside of inventory*/

function addStock(){
	//NOT ALLOWED TO USE querySelectorAll()



	//find all the selected items in the HTML list
	//grab all the items with checkboxes and put them into a list
	//var input = document.getElementsByClassName("checkbox"); 
	var input = getSelectedRowBoxes();
	//console.log(input);


	//loop through the list of all checkboxes and select only the checked=true items

	for (var i = 0; i < input.length; i++){

		var status = input[i].parentNode.parentNode.lastChild;

		console.log("Last item:", status);

		status.textContent = "Yes";
		status.className = "true";

		//update the Product in the products array that corresponds to the checked checkbox we're updating
		var prodId = input[i].parentNode.parentNode.id;
		products[prodId].inStock = true;

		
	}
	saveData();
}









function removeStock(){
	//use querySelectorAll()

	//create an empty list
	//var checkboxes = [];


	//find all the selected items in the HTML list
	//grab all the items with checkboxes and put them into a list

	var input = getSelectedRowBoxes();

	//console.log(input)


	for (var i=0; i < input.length; i++){
		var status = input[i].parentNode.nextSibling.nextSibling.nextSibling;
		console.log("Last item:", status);

		status.textContent = "No";
		status.className = "false";


		//update the Product in the products array that correspends to the checked checkbox we're updating
		var prodId = input[i].parentNode.parentNode.id;
		products[prodId].inStock = false;
	}
	saveData();
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

 	//create a new instance of the Product object with the new item's info
 	var newProd = new Product(materialName, priceName, inStock);
 	//console.log(newProd);
 	products.push(newProd);

 	displayInventory();
 	saveData();
 }




/* Delete selected rows from the inventory */
function delItem(){
	//determine all the selected rows
	var input = getSelectedRowBoxes();

	//delete the Product objects that correspond to those rows from the products array
	//loop through the list backwards
	for (var i = input.length-1; i>=0; i--){
		//get the id on the row that the checkbox is in
		var prodId = input[i].parentNode.parentNode.id;

		//delete the Product at that index (prodId = index)
		delete products[prodId]

		//delete products leaves an undefined item , so we need to fill the hole
		products.splice(prodId, 1);

	}

	//re-render the hTML list using displayInventory
	displayInventory();

	saveData();
}

//helper function to get all the checked boxes in the HTML's inventory
//returns array of selected checkboxes
function getSelectedRowBoxes(){
	var input = document.querySelectorAll('input:checked:not([id="in-stock"])');
	return input;

}


/* adds all the items in the products array to the HTML*/
function displayInventory(){

	var inventory = document.getElementById("inventory")
	inventory.innerHTML = "";

	//loop through the products array adding each Product to the inventory table in the HTML
	for (var i=0; i < products.length; i++){

		//make a new row for the product i
		var newRow = document.createElement("TR");
		newRow.id = i;

		//better alternative
		//newRow.id = "prod_" + i;

		//make a <td> for the checkbox
		var checkbox = document.createElement("TD");
		//make the checkbox
		var innerCheckbox = document.createElement("INPUT");
		//set the input type to checkbox
		innerCheckbox.type = "checkbox";

		//don't forget we getelementByClassName in addStock and need to update it here too
		innerCheckbox.className = "checkbox";

		//add the checkbox into the <td>
		checkbox.appendChild(innerCheckbox);

		//make a <td> for the material name
		var materialName = document.createElement("TD");
		materialName.textContent = products[i].prodName;

		//make a <td> for the price
		var price = document.createElement("TD");
		price.textContent = products[i].price;

		//make a <td> for the stock toggle
		var inStock = document.createElement("TD");
		//set the <td>'s text content to either yes or no based on the product at index i's inStock property
		inStock.textContent = (function(inStock){
			if (inStock){
				return "Yes";
			}
			return "No";
		}(products[i].inStock));

		//manually set the attribute 
		inStock.className = products[i].inStock;

		//same as above, but let javascript set it for you
		//set the class on the <td> to the correct class
		//inStock.setAttribute("class", products[i].inStock);


		/*if (products[i].inStock){
			inStock.textcontent = "Yes";
		} else {
			inStock.textcontent = "No";
		}*/

		//add all the <td>'s to the <tr>'
		newRow.appendChild(checkbox);
		newRow.appendChild(materialName);
		newRow.appendChild(price);
		newRow.appendChild(inStock);

		//add the new row to the actual TBODY in the HTML
		inventory.appendChild(newRow);
	};

	saveData();
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


//saves the current state of the products array

function saveData(){
	//transform the products array into a JSON string
	var productJSON = JSON.stringify(products);
	console.log(productJSON);

	//save that JSON string to local storage
	localStorage.setItem("price_list", productJSON);
}



//loads the current state of the product data
function loadData(){
	//load datat from local storage
	var productJSON = localStorage.getItem("price_list");
	console.log("loaded data ", productJSON);

	//parse it into a javscript data type and save to the global array
	products = JSON.parse(productJSON);
	console.log(products);

	//double check products is set ot a list of null
	if (!products){
		products = [];
	}

	//updatethe rendered display
	displayInventory();

}