window.onLoad = function(){
	document.getElementById('question_vote').addEventListener('submit', votingSubmission);
}

function votingSubmission(event){
	event.preventDefault();

	var form = document.getElementById('question_vote');

	var data = form.querySeelctor("[type='radio']:checked")

	var question_id = form.getElementById('question_id').value;

	console.log(data.value)
}