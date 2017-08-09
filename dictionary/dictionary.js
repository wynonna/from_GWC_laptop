var wordsList = [];

function init() {
  // Load the words from the dictionary text file to wordsList
  var wordsFile = "https://raw.githubusercontent.com/GirlsFirst/SIP-2017/master/Unit2_Applications/dictionary-attack/dictionary.txt?token=ADcVhZjRMd86ZdhPE2jVvIaJdQdzLA6Yks5YvvVSwA%3D%3D";
  $.get(wordsFile, function(data) {
    document.getElementById("btnSubmit").disabled = true;
    wordsList = data.split('\n');
    document.getElementById("btnSubmit").disabled = false;
  });
}

window.onload = init;

/* ADD YOUR CODE BELOW */

function checkPassword() {
  //take user input from box

var found = false;
for (var i=0; i<wordsList.length; i++) {
  var pass = document.getElementById("pw").value;
  if (wordsList[i]===pass); {
    found==true;
    break;
  }
  else {
    found==false;
  }
}
if (found==true) {
    alert("good password");
  }

else{
  alert("bad password");
  }
}
checkPassword()
