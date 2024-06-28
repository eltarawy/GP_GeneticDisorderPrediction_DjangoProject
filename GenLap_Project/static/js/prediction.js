let currentQuestion = 1;
const totalQuestions =20; // Update this value with the total number of questions

function showQuestion(questionNumber) {
  document
    .getElementById(`question${questionNumber}`)
    .classList.remove("hidden");
}

function hideQuestion(questionNumber) {
  document
    .getElementById(`question${questionNumber}`)
    .classList.add("hidden");
}

function nextQuestion() {
  hideQuestion(currentQuestion);
  currentQuestion++;
  showQuestion(currentQuestion);
  updateButtons();
}

function prevQuestion() {
  hideQuestion(currentQuestion);
  currentQuestion--;
  showQuestion(currentQuestion);
  updateButtons();
}

function updateButtons() {
  document.getElementById("prevButton").disabled = currentQuestion === 1;
  document
    .getElementById("nextButton")
    .classList.toggle("hidden", currentQuestion === totalQuestions);
  document
    .getElementById("submitButton")
    .classList.toggle("hidden", currentQuestion !== totalQuestions);
}

// Show the first question initially
showQuestion(currentQuestion);
updateButtons();