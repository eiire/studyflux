export const is_auth = JSON.parse($('meta[name=is_auth]').attr('is_auth').toLowerCase())
export const csrf_token = $('input[name=csrfmiddlewaretoken]').attr('value')
