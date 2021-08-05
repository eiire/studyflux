const csrf_token = function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
} ('csrftoken')

const likes = $('.like > input')

likes.each(function (i, e) {
    let like_obj = this
    let post_id = $(this).attr("id").split('_')[1];

    $.ajax({
        type: 'GET',
        url: window.location.origin + '/like_api/v1/posts/' + post_id + '/',
        context: function () {return like_obj} (),
        headers: {'X-CSRFToken': csrf_token},
        success: function (data) {
            if (data.is_fan)
                e.setAttribute('checked', 'checked')
        }
    });
})

likes.on("click", function() {
    let like_obj = this
    let post_id = $(this).attr("id").split('_')[1];
    let method;
    this.getAttribute('checked') === 'checked' ? method = '/unlike/' : method = '/like/'

    $.ajax({
        type: 'POST',
        url: window.location.origin + '/like_api/v1/posts/' + post_id + method,
        context: function () {
            return like_obj
        } (),
        headers: {'X-CSRFToken': csrf_token},
        success: function () {
            method === '/unlike/' ? this.removeAttribute('checked') : this.setAttribute('checked', 'checked')
        }
    });
})

function get_comment_form(parent_id) {
    let parent = $("#id_parent")
    parent_id === 'write_comment' ? parent.val('') : parent.val(parent_id);

    $("#comment_form").insertAfter("#" + parent_id);
}
