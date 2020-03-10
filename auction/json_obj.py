"""This module is used to decode/encode json"""
import json


class JsonObj(json.JSONEncoder):
    """
    Class to abstract custom json object decoding/encoding. Inherits from
    json.JSONEncoder

    Attributes
    ----------
    data : dict
        A dictionary of Python decoded objects
    properties : dict
        A dictionary of Python class properties used to identify this class
        object

    Methods
    -------
    loads(class_name, json_str)
        Static method to deserialize json_str (a str, bytes or bytearray
        instance containing a JSON document) to a
        Python object of type class_name
    dumps(class_name, json_dict)
        Static method to serialize json_dict with objects of type class_name to
        a JSON formatted str

    """

    _properties = dict()

    def __init__(self, data, **kwargs):
        """__init__ method.

        Parameters
        ----------
        data : dict
            A dictionary of Python decoded objects
        **kwargs
            Keyword arguments passed to JSONEncoder parent class

        """
        super().__init__(**kwargs)
        self._data = data

    @property
    def data(self):
        """dict:  A dictionary of Python decoded objects"""
        return self._data

    @property
    def properties(self):
        """dict:  A dictionary of Python class properties used to identify
        this class object """
        return self._properties

    @staticmethod
    def _object_hook(json_dict):
        """Default object hook for decoding json elements with default types

        Parameters
        ----------
        json_dict : dict
            Python dictionary with standard type elements

        Returns
        -------
        bool
            Python dictionary with decoded elements

        """
        return json_dict

    @staticmethod
    def _get_properties(class_name):
        """Private method to return class properties (attributes with
        @property decorator)

        Parameters
        ----------
        class_name : str
            Class name

        Returns
        -------
        dict
            Dictionary containing property name,object key,values

        """
        properties = {key: val
                      for key, val in class_name.__dict__.items()
                      if isinstance(val, property)}
        return properties

    @staticmethod
    def _is_object(class_name, json_dict):
        """Private method to determine if class with class_name matches
        element in json_dict. The method compares class_name properties with
        json_dict keys to determine a match.

        Parameters
        ----------
        class_name : str
            Class name to determine match
        json_dict : dict
            Python dictionary element

        Returns
        -------
        bool
            True if class_name properties matches json_dict keys

        """
        if not class_name._properties:
            class_name._properties = JsonObj._get_properties(class_name)
        return class_name._properties.keys() == json_dict.keys()

    @staticmethod
    def loads(class_name, json_str):
        """Static method to to deserialize json_str (a str, bytes or
        bytearray instance containing a JSON document) to a Python object of
        type class_name. This method uses object_hook parameter in
        json.loads to do the parsing of custom JsonObj type classes

        Parameters
        ----------
        class_name : JsonObj
            Class used to decode additional Python objects (e.g. bid objects)
        json_str : str
            A str, bytes or bytearray instance containing a JSON document

        Returns
        -------
        dict
            Python dictionary containing python object elements

        """
        return json.loads(json_str, object_hook=class_name._object_hook)

    @staticmethod
    def dumps(class_name, json_dict):
        """Static method to serialize json_dict with objects of type
        class_name to a JSON formatted str

        Parameters
        ----------
        class_name : str
            Class to serialise additional types
        json_dict : dict
            A str, bytes or bytearray instance containing a JSON document

        Returns
        -------
        str
            JSON formatted str

        """
        return json.dumps(json_dict, cls=class_name, indent=4)
