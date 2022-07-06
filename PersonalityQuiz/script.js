var oldieScore = 0; 
var newbieScore = 0; 
var questionCount = 0; 

var result = document.getElementById("result");
var q1a1 = document.getElementById("q1a1");
var q1a2 = document.getElementById("q1a2");
var q2a1 = document.getElementById("q2a1"); 
var q2a2 = document.getElementById("q2a2"); 
var q3a1 = document.getElementById("q3a1"); 
var q3a2 = document.getElementById("q3a2"); 
var restartButton = document.getElementById("restartButton"); 
var display = document.getElementById("display")

q1a1.addEventListener('click',oldie); 
q1a2.addEventListener('click',newbie); 
q2a1.addEventListener('click',newbie); 
q2a2.addEventListener('click',oldie); 
q3a1.addEventListener('click',newbie); 
q3a2.addEventListener('click',oldie); 
restartButton.addEventListener('click',restart); 
display.addEventListener('click',displayResult)


function oldie(){
  oldieScore += 1; 
  questionCount += 1; 

  console.log("questionCount = " + questionCount + "oldieScore = " + oldieScore); 

  if (questionCount == 3) {
    console.log("The quiz is done.")
    updateResult()
}
}

function newbie() {
  newbieScore += 1;  
  questionCount += 1; 

  console.log("questionCount = " + questionCount + "newbieScore = " + newbieScore); 
  
  if (questionCount == 3) {
    console.log("The quiz is done.")
    updateResult()
  }
}
// Update quiz result 
/* function updateResult() {
  if (oldieScore >= 2){
    result.innerHTML = "You are an oldie!"
    console.log("You are an oldie!")
  } else if (newbieScore >= 2) {
    result.innerHTML = "You are a newbie!"
    console.log("You are a newbie!")
  }
}
*/

function restart(){
  document.getElementById('result').innerHTML = "Your result is ..."
  var oldieScore = 0; 
  var newbieScore = 0; 
  var questionCount = 0;
  enableQuestions();
}

// Manually display result 
function displayResult(){
  if (oldieScore >= 2){
    result.innerHTML = "You are an oldie!"
    console.log("You are an oldie!")
  } else if (newbieScore >= 2) {
    result.innerHTML = "You are a newbie!"
    console.log("You are a newbie!")
  } 
}

// Figure out how to disable the buttons once the question is answered. 

q1a1.addEventListener("click", disableQ1);
q1a2.addEventListener("click", disableQ1);

q2a1.addEventListener("click", disableQ2);
q2a2.addEventListener("click", disableQ2);

q3a1.addEventListener("click", disableQ3);
q3a2.addEventListener("click", disableQ3);

function disableQ1() {
  q1a1.disabled = true; 
  q1a2.disabled = true; 
}

function disableQ2() {
  q2a1.disabled = true; 
  q2a2.disabled = true; 
}

function disableQ3() {
  q3a1.disabled = true; 
  q3a2.disabled = true; 
}


function enableQuestions(){
  q1a1.disabled = false; 
  q1a2.disabled = false; 
  q2a1.disabled = false; 
  q2a2.disabled = false;
  q3a1.disabled = false; 
  q3a2.disabled = false;
}

