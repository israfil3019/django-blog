let like = document.getElementById("heart")
like.onmouseover = function() {mouseOver()};
like.onmouseout = function() {mouseOut()};

function mouseOver() {
  like.className = "text-danger";
}

function mouseOut() {
  like.className = "text-info";
}