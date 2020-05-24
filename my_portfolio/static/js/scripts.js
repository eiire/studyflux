function collaps_navbar() {
    var navbar = document.getElementById("my_navbar");

    if (navbar.className === "my_navbar") {
        navbar.className += " responsive";
    } else {
        navbar.className = "my_navbar";
    }
}