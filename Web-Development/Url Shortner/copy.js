let newURL = document.getElementById("shorturl");
let copybutton = document.getElementById("copy");


copybutton.onclick = () => {
    navigator.cli;pboard.writeText(newURL.value)
};