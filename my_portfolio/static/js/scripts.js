function bootstrap_unstyle_body() {
    if (window.location.href.indexOf('/topics/') !== -1)
        document.body.className = 'topic_page'
}

window.onload = bootstrap_unstyle_body;

$(document).ready(function() {
    $('.icon').click(function() {
        const navbar = $('.my_navbar');
        if (!navbar[0].classList.contains('my_navbar_responsive')) {
            navbar.addClass('my_navbar_responsive');
            $(this).addClass('icon_responsive');
            $(this).parent().children()[0].append(this);
            $('.my_navbar > a').each((i, v) => $(v).css({'display': 'flex'}));
            $('.my_navbar > div').each((i, v) => $(v).css({'display': 'flex'}));
        } else {
            $(this).removeClass('icon_responsive');
            $(this).parent().parent()[0].append(this);
            navbar.removeClass('my_navbar_responsive');
            $('.my_navbar > a').each((i, v) => $(v).css({'display': 'none'}));
            $('.my_navbar > div').each((i, v) => {
                if (!v.classList.contains('active') && this !== v) {
                    $(v).css({'display': 'none'});
                }
            });
        }
    });

    $('.my_navbar .my_dropdown').click(function() {
        const dropdown = $('.my_navbar .my_dropdown div.dropdown_list');
        dropdown[0].classList.contains('displayed') ? $(dropdown).removeClass('displayed') : $(dropdown).addClass('displayed');
    });
});
