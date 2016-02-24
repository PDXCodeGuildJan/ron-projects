//Establish the event listener for when they clck an item
//Add the click event handler to "add-item"
var addItemButton = document.getElementById("add-item");

addItemButton.onclick = addItem;

var addStockButton = document.getElementById("add-stock");

addStockButton.onclick = addStock;


/*toggle the inStock status on the selected rows inside of inventory*/

function addStock(){
	//NOOT ALLOWED TO USE querySelectorAll()
	console.log()
	//find all the selected items in the HTML list

	//change their in-stock value

	//update the display? depends on previous step. not adding quantity

}


function removeStock(){
	//use querySElectorAll()

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
 	var newRow = "<tr>" + "<td>" + "<input type='checkbox'>" + "</td>" + "<td>" + materialName + "</td>" + "<td>" + priceName + "</td>" + "<td class=' " + inStock + "'>"; 
 	
 	if (inStock){
 		newRow += "Yes";
 	} else{
 		newRow += "No";
 	}
 	newRow += "</td> </tr>";

 	

 	inventory.innerHTML += newRow; 
 	}



