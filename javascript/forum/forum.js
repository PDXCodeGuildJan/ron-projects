


//GET XML data from JSON request

var insertAfter = '.results'; // reference of object in your DOM to insert the object into
var objectType  = '<div>'; // object that we'll be inserting as a container for the feed information
var objectID  = 'spreadsheedFeed'; // id of the object that is being inserted
var url   = 'http://spreadsheets.google.com/feeds/list/1NlIJLGd32t38kt6mJgc64SFpDM_ltq7nfzaRjV1wpLI/default/public/values?alt=json-in-script';

$(document).ready(function(){
	google.load('feeds', '1', { 'callback' : function(){ 
		($.getJSON(url, 'callback=?')).success(function(data){
			$(insertAfter).after(
				$(objectType).attr('id',objectID)
				);
	var wrapper = $('#'+objectID);
	//from the feed array create a clean row
	$(data.feed.entry).each(function(i,entry){
		//create variables for the column names
		var timestamp    = entry.gsx$timestamp.$t;
		var title    = entry.gsx$title.$t;
		var post   = entry.gsx$post.$t;

   
		wrapper.append(
			$('<ul>').append(
				$('<li>').text(timestamp)
				).append(
					$('<li>').text(title)
					).append(
						$('<li>').text(post)
						)
				)
			});
			});
		}});
});


//POST XML data

//var submitBtn = document.getElementById("submit");

//submitBtn.onclick = postToGoogle;





function postToGoogle(){
	var title = $('#title').val();
	var bodytext = $('#bodytext').val();


	if ((title !== "") && (bodytext !== "")) {
		$('#error-message').hide();
		$.ajax({
			url: "https://docs.google.com/forms/d/1W1jO8DwInFuzlabeYqEp6hUUUqDbR8gESs1Pk6qozOc/formResponse",
			data: {"entry.1639809944" : title, "entry.1402022725" : bodytext},
			type: "POST",
			dataType: "xml",
			statusCode:{
				0: function (){
                	/*$("#title").val("");
                	$("#bodytext").val("");
*/
                    //Success message
                },
                200: function (){
                	$("#title").val("");
                	$("#bodytext").val("");

                    //Success Message
                }
            }
        });
    }
    else {
        $('#error-message').slideUp(800, function() { $(this).slideDown(800)});
    }
}

$(document).ready(function(){
    $('#error-message').hide();
	$('#request').submit(function() {
		postToGoogle();
		return false;
	});
});