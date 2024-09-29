

var cur = 3;

function displaypage(i) {
  cur = i;
  var div = $("#pagediv");
  if (cur === 3) {
    div.html('<b>Boca Style</b>');
  }
  if (cur === 2) {
    div.html('<b>Bella Style</b>');
  }
  if (cur === 1) {
    div.html('<b>Terra Style</b>');
  }
}