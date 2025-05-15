console.log('test');
var linkRefs = document.getElementsByClassName("nav-item");
// linkRefs[2].className += ' active';
for (var i = 0; i < linkRefs.length; i++) {
    console.log(i)
    linkRefs[i].addEventListener("click", function() {
        var current = document.getElementsByClassName("active");
        current[0].className = current[0].className.replace(" active", "");
        this.className += " active";
});
}
console.log('test');
var subLinkRefs = document.getElementsByClassName("nav-item-sub");
// linkRefs[2].className += ' active';
for (var i = 0; i < subLinkRefs.length; i++) {

    subLinkRefs[i].addEventListener("click", function() {
        var current = document.getElementsByClassName("nav-item-sub active");
        current[0].className = current[0].className.replace(" active", "");
        this.className += " active";
});
}