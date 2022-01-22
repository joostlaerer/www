var sliderUte = document.getElementById("sliderUteTemp");
var sliderInne = document.getElementById("sliderInneTemp");
var knappUregning = document.getElementById("utregningButton")
var textUtregning =document.getElementById("utregnetWattUT")

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

knappUregning.addEventListener("click", regnut);

function regnut() {
  textUtregning.innerHTML= `Slider 1 står på ${sliderInne.value} slider 2 står på ${sliderUte.value}`

}

//Legger til dropdown
/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

function filterFunction() {
  var input, filter, ul, li, a, i;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  div = document.getElementById("myDropdown");
  a = div.getElementsByTagName("a");
  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
    } else {
      a[i].style.display = "none";
    }
  }
}

//Legger til dropdown med klick
/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}