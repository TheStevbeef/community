# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class User(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, name: str=None, image_url: str=None):  # noqa: E501
        """User - a model defined in Swagger

        :param id: The id of this User.  # noqa: E501
        :type id: str
        :param name: The name of this User.  # noqa: E501
        :type name: str
        :param image_url: The image_url of this User.  # noqa: E501
        :type image_url: str
        """
        self.swagger_types = {
            'id': str,
            'name': str,
            'image_url': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'image_url': 'image_url'
        }
        self._id = id
        self._name = name
        self._image_url = image_url

    @classmethod
    def from_dict(cls, dikt) -> 'User':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The User of this User.  # noqa: E501
        :rtype: User
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this User.


        :return: The id of this User.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this User.


        :param id: The id of this User.
        :type id: str
        """

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this User.


        :return: The name of this User.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this User.


        :param name: The name of this User.
        :type name: str
        """

        self._name = name

    @property
    def image_url(self) -> str:
        """Gets the image_url of this User.


        :return: The image_url of this User.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url: str):
        """Sets the image_url of this User.


        :param image_url: The image_url of this User.
        :type image_url: str
        """

        self._image_url = image_url
