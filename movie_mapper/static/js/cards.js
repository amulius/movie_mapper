
function toggleRotate() {
    $("#joker1").toggleClass("rotate");
    $("#joker2").toggleClass("rotate");
}

setInterval(toggleRotate, 2000);