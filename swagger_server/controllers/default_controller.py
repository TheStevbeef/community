import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.post import Post  # noqa: E501
from swagger_server.models.post_without_time_and_id import PostWithoutTimeAndId  # noqa: E501
from swagger_server.models.posts import Posts  # noqa: E501
from swagger_server import util


def posts_get(limit=None, offset=None):  # noqa: E501
    """posts_get

    Get posts # noqa: E501

    :param limit: The amount of posts returned
    :type limit: int
    :param offset: The Offset of the returning list
    :type offset: int

    :rtype: Posts
    """


    return 'do some magic!'


def posts_id_delete(id):  # noqa: E501
    """posts_id_delete

    Obtain information about specific post # noqa: E501

    :param id: The ID of the post
    :type id: str

    :rtype: InlineResponse200
    """
    return 'do some magic!'


def posts_id_get(id):  # noqa: E501
    """posts_id_get

    Obtain information about specific post # noqa: E501

    :param id: The ID of the post
    :type id: str

    :rtype: Post
    """
    return 'do some magic!'


def posts_post(body):  # noqa: E501
    """posts_post

    post post # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Post
    """
    if connexion.request.is_json:
        body = PostWithoutTimeAndId.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
