var btnMsg = document.getElementById("buttonShowMsg");
var msgText = document.getElementById("msgText");

console.log("script started")

btnMsg.addEventListener("click", function() {
  console.log("button clicked")
  var req = new XMLHttpRequest();

  req.open('POST', '/show_message', true);
  req.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
  req.send("text=" + msgText.value);
});