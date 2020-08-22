function collaps_navbar() {
    var navbar = document.getElementById("my_navbar");

    if (navbar.className === "my_navbar") {
        navbar.className += " responsive";
    } else {
        navbar.className = "my_navbar";
    }
}

function bootstrap_unstyle_body() {
    if (window.location.href.indexOf('/topics/') !== -1)
        document.body.className = 'topic_page'
}

window.onload = bootstrap_unstyle_body;
