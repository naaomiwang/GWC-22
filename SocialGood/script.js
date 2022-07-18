/* .js files add interaction to your website */
var displayScript = document.getElementById("scriptReturned"); 
var scriptBtn = document.getElementById("scriptBtn"); 

if (scriptBtn){
  scriptBtn.addEventListener("click",generateScript);
}

function generateScript(){
  var name = document.getElementById("name").value; 
  var issue = document.getElementById("issue").value; 
  var experience = document.getElementById("experience").value; 

displayScript.innerHTML = "Hello, my name is " + name + " and i have/had " + issue + "." + " This is my experience: " + experience; 
}

var factList = [
  "One in five American adults experienced a mental health issue.", 
  "One in 6 young people experienced a major depressive episode", 
  "One in 20 Americans lived with a serious mental illness, such as schizophrenia, bipolar disorder, or major depression.", 
  "Half of all mental health disorders show first signs before a person turns 14 years old, and three-quarters of mental health disorders begin before age 24.", 
  "Mental health problems have nothing to do with being lazy or weak and many people need help to get better.", 
  " In 2020, only 20% of adults received any mental health treatment in the past year, which included 10% who received counseling or therapy from a professional."
];

var fact = document.getElementById("fact");
var factBtn = document.getElementById("factBtn");
var count = 0;

if (factBtn) {
  factBtn.addEventListener("click", displayFact);
}

function displayFact() {
  fact.innerHTML = factList[count];
  count++;
  if (count == factList.length) {
    count = 0;
  }
}
