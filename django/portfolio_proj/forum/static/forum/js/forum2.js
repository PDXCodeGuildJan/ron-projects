//GET XML data from JSON request


function get() {
	$('.items').remove();
	
	$.getJSON( "http://spreadsheets.google.com/feeds/list/1NlIJLGd32t38kt6mJgc64SFpDM_ltq7nfzaRjV1wpLI/default/public/values?alt=json-in-script&callback=?",
		function (data) {
			//inside the results class create a new div with a class called items
			$('.results').append('<div class="items"></div>');
			
			// parse the google feed string and grab each spreadsheet column heading 
			$.each(data.feed.entry, function(i,entry) {
				//define the variable "item"
				var item = '<span style="display:none">' + entry.id.$t + '</span>';
				item += '<br/>Date: ' + entry.gsx$timestamp.$t;
				item += '<br/>title: ' + entry.gsx$title.$t;
				item += '<br/>bodytext: ' + entry.gsx$post.$t;
				//take the results of all the items and put them in the div class called items
				$('.items').append('<div>' + item + '</div>');

			});
	});
}



//POST XML data
// define how to submit content to the spreadsheet
function postToGoogle(title, bodytext) {

	$.ajax({
	url: "https://docs.google.com/forms/d/1W1jO8DwInFuzlabeYqEp6hUUUqDbR8gESs1Pk6qozOc/formResponse",
	data: {"entry.1639809944" : title, "entry.1402022725" : bodytext},
	type: "POST",
	dataType: "xml",
	statusCode: {
		0: function() {
		//get();
		location.reload();

		//Error message
		},

		200: function() {
		//Success Message
		}
	}
	});
}

// define what is being submitted to the function postToGoogle()
function submit(event){
	event.preventDefault();
	var title = document.forms["form"]["title"].value;
	var bodytext = document.forms["form"]["bodytext"].value;

	postToGoogle(title, bodytext);


	//console.log(title, bodytext)

}

$(document).ready(function(){
	get();

	form = document.getElementById("form")

	form.addEventListener("submit", submit)

});



/*
function get() {	

	$.getJSON('http://spreadsheets.google.com/feeds/list/1NlIJLGd32t38kt6mJgc64SFpDM_ltq7nfzaRjV1wpLI/default/public/values?alt=json-in-script&callback=?', 
	function(data) {
    var string = "<div>";       
    for (var i = 0; i < data.feed.entry.length; i++) {

      var timestamp = data.feed.entry[i].gsx$timestamp.$t;
      var title = data.feed.entry[i].gsx$title.$t;
      var bodytext = data.feed.entry[i].gsx$bodytext.$t;
      string += '</br>' + timestamp + '</br>' + title + '</br>' + bodytext + '</br>';

    }

    string += "</div>";

    $('string').appendTo('.results');

});

}*/