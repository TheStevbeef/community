# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Media(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, content_type: str=None, url: str=None):  # noqa: E501
        """Media - a model defined in Swagger

        :param content_type: The content_type of this Media.  # noqa: E501
        :type content_type: str
        :param url: The url of this Media.  # noqa: E501
        :type url: str
        """
        self.swagger_types = {
            'content_type': str,
            'url': str
        }

        self.attribute_map = {
            'content_type': 'content_type',
            'url': 'url'
        }
        self._content_type = content_type
        self._url = url

    @classmethod
    def from_dict(cls, dikt) -> 'Media':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Media of this Media.  # noqa: E501
        :rtype: Media
        """
        return util.deserialize_model(dikt, cls)

    @property
    def content_type(self) -> str:
        """Gets the content_type of this Media.


        :return: The content_type of this Media.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type: str):
        """Sets the content_type of this Media.


        :param content_type: The content_type of this Media.
        :type content_type: str
        """

        self._content_type = content_type

    @property
    def url(self) -> str:
        """Gets the url of this Media.


        :return: The url of this Media.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """Sets the url of this Media.


        :param url: The url of this Media.
        :type url: str
        """

        self._url = url