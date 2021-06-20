// var format = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]+/;
var format = /[!@#$%^&*()+\=\[\]{};':"\\|,<>\/?]+/;
str = "hi$m";
function checkStr() {
  if (format.test(str) || str.indexOf(" ") > -1) {
    return true;
  } else {
    return false;
  }
}
console.log(checkStr());
