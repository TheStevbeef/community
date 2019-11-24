# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.post import Post  # noqa: E501
from swagger_server.models.post_without_time_and_id import PostWithoutTimeAndId  # noqa: E501
from swagger_server.models.posts import Posts  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_posts_get(self):
        """Test case for posts_get

        
        """
        query_string = [('limit', 56),
                        ('offset', 56)]
        response = self.client.open(
            '//posts',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_posts_id_delete(self):
        """Test case for posts_id_delete

        
        """
        response = self.client.open(
            '//posts/{id}'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_posts_id_get(self):
        """Test case for posts_id_get

        
        """
        response = self.client.open(
            '//posts/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_posts_post(self):
        """Test case for posts_post

        
        """
        body = PostWithoutTimeAndId()
        response = self.client.open(
            '//posts',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
