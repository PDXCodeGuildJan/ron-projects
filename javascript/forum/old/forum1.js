

//var url = "https://spreadsheets.google.com/feeds/list/1NlIJLGd32t38kt6mJgc64SFpDM_ltq7nfzaRjV1wpLI/default/public/values?alt=json-in-script&callback=?";


/*

gdocs.constructSpreadAtomXml_ = function(title, post) {    
    var atom = ["<?xml version='1.0' encoding='UTF-8'?>",
              '<entry xmlns="http://www.w3.org/2005/Atom" xmlns:gsx="http://schemas.google.com/spreadsheets/2006/extended">',
              '<gsx:title>',title,'</gsx:title>',
              '<gsx:post>',post,'</gsx:post>',
              '</entry>'].join('');
    return atom;
};

 var params = {
    'method': 'POST',
    'headers': {
      'GData-Version': '3.0',
      'Content-Type': 'application/atom+xml'
    },

    'body': gdocs.constructSpreadAtomXml_(title, post)
};

  var worksheetId = 'od6'; //The first worksheet.
  var docID = '1NlIJLGd32t38kt6mJgc64SFpDM_ltq7nfzaRjV1wpLI';

  var url = 'https://spreadsheets.google.com/feeds'+'/list/'+docId+'/'+worksheetId+'/private/full';

  //sends the params to the background page to get delivered to gDocs
  oauth.sendSignedRequest(url, handleSuccess, params);

*/

/*
function writeJSONtoSheet(json) {
 
  var sheet = SpreadsheetApp.getActiveSheet();
 
  var keys = Object.keys(json).sort();
  var last = sheet.getLastColumn();
  var header = sheet.getRange(1, 1, 1, last).getValues()[0];
  var newCols = [];
 
  for (var k = 0; k < keys.length; k++) {
    if (header.indexOf(keys[k]) === -1) {
      newCols.push(keys[k]);
    }
  }
 
  if (newCols.length > 0) {
    sheet.insertColumnsAfter(last, newCols.length);
    sheet.getRange(1, last + 1, 1, newCols.length).setValues([newCols]);
    header = header.concat(newCols);
  }
 
  var row = [];
 
  for (var h = 0; h < header.length; h++) {
    row.push(header[h] in json ? json[header[h]] : "");
  }
 
  sheet.appendRow(row);
 
}
*/	
/*

window.onload = loadDataWithAJAX;


//Load data from the JSON file on the server with AJAX
function loadDataWithAJAX(){

	//create a new XMLHttpRequest object
	var request = new XMLHttpRequest();
	//add the call info
	request.open('GET', 'data.json', true);

	//setup th eonload function
	request.onload = function() {
		// make sure that everthing is good with the callback
		if (request.status === 200){
			console.log(request.responseText);
			var prodJSON = request.responseText;
			products = JSON.parse(prodJSON);
			displayInventory();
		}

	}

	//actually send out the request
	request.send();
}
*/


