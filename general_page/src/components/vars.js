import Cookies from 'js-cookie'

export let csrf_token = Cookies.get('csrftoken');
