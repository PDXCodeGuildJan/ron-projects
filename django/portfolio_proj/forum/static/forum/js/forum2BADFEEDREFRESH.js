//GET XML data from JSON request


function get() {	
	$.getJSON( "http://spreadsheets.google.com/feeds/list/1NlIJLGd32t38kt6mJgc64SFpDM_ltq7nfzaRjV1wpLI/default/public/values?alt=json-in-script&callback=?",
		function (data) {	

			$('.results').append('<div class="items"></div>');

			$.each(data.feed.entry, function(i,entry) {	
				var item = '<span style="display:none">' + entry.id.$t + '</span>';
				item += '<br/>Date: ' + entry.gsx$timestamp.$t;
				item += '<br/>title: ' + entry.gsx$title.$t;
				item += '<br/>bodytext: ' + entry.gsx$post.$t;	
				$('.items').append('<div>' + item + '</div>');


			});
	});
}




//POST XML data

function postToGoogle(title, bodytext) {

	$.ajax({
	url: "https://docs.google.com/forms/d/1W1jO8DwInFuzlabeYqEp6hUUUqDbR8gESs1Pk6qozOc/formResponse",
	data: {"entry.1639809944" : title, "entry.1402022725" : bodytext},
	type: "POST",
	dataType: "xml",
	statusCode: {
		0: function() {
		get();
		//Error message
		},

		200: function() {
		//Success Message
		}
	}
	});
}


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

