ARTICLE_SCHEMA = {
    '$schema': 'http://json-schema.org/schema#',
    'type': 'object',
    'properties': {
        'title': {
            # 'type': 'string',
            'minLength': 1,
            'maxLength': 250,
        },
        'body': {
            # 'type': 'string',
            'minLength': 1,
        },
    },
    'required': ['title', 'body'],
}
