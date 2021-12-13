var sliderUte = document.getElementById("sliderUteTemp");
var sliderInne = document.getElementById("sliderInneTemp");

var outputUteTemp = document.getElementById("uteTempFelt");
var outputInneTemp = document.getElementById("inneTempFelt");

outputUteTemp.innerHTML = sliderUte.value;
outputInneTemp.innerHTML = sliderInne.value;

sliderUte.oninput = function() {
  outputUteTemp.innerHTML = this.value;
}
sliderInne.oninput = function() {
    outputInneTemp.innerHTML = this.value;
  }