const questionSubmitButton = document.querySelector("a#question_submit_button");
const questionSucessMessage = document.querySelector("div#question_success_message");
const questionFailureMessage = document.querySelector("div#question_failure_message");
const askQuestion = document.querySelector('textarea#ask_question');

questionSucessMessage.style.display = 'none';

questionSubmitButton.addEventListener('click', function() {
	var ul = document.querySelector('ul#question_collections');
	var li = document.querySelector("li#question_detail_cover,p#question_details");
	if (askQuestion.value === "") {
		questionSucessMessage.style.display = 'none';
		questionSubmitButton.textContent = "Please Ask question";
	} else {
		questionSubmitButton.textContent = "SUBMITED";
		questionSubmitButton.textContent = "SUBMIT";
		questionSucessMessage.style.display = 'block';
		// li = document.createElement('li');
		// li.textContent = askQuestion.value;
		// ul.appendChild(li);
	}
	askQuestion.value = "";
});