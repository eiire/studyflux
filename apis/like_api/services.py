from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from user_blog.models import PostLike
User = get_user_model()


def to_like(_object, user):
    """Likes `obj`."""
    obj_type = ContentType.objects.get_for_model(_object)
    like, is_created = PostLike.objects.get_or_create(
        content_type=obj_type, object_id=_object.id, user=user
    )

    return like


def to_unlike(_object, user):
    """Removes like from `obj`."""
    obj_type = ContentType.objects.get_for_model(_object)
    PostLike.objects.filter(
        content_type=obj_type, object_id=_object.id, user=user
    ).delete()


def is_fan(_object, user) -> bool:
    """Checks if ʻuser` ʻobj` has liked."""
    if not user.is_authenticated:
        return False

    obj_type = ContentType.objects.get_for_model(_object)
    likes = PostLike.objects.filter(
        content_type=obj_type, object_id=_object.id, user=user
    )

    return likes.exists()


def get_fans(_object):
    """Gets all users who like ʻobj`."""
    obj_type = ContentType.objects.get_for_model(_object)

    return User.objects.filter(
        likes__content_type=obj_type, likes__object_id=_object.id
    )
