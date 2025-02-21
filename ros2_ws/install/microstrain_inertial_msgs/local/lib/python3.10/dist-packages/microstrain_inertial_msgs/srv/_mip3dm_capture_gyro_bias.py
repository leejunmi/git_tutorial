# generated from rosidl_generator_py/resource/_idl.py.em
# with input from microstrain_inertial_msgs:srv/Mip3dmCaptureGyroBias.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Mip3dmCaptureGyroBias_Request(type):
    """Metaclass of message 'Mip3dmCaptureGyroBias_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('microstrain_inertial_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'microstrain_inertial_msgs.srv.Mip3dmCaptureGyroBias_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__mip3dm_capture_gyro_bias__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__mip3dm_capture_gyro_bias__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__mip3dm_capture_gyro_bias__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__mip3dm_capture_gyro_bias__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__mip3dm_capture_gyro_bias__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Mip3dmCaptureGyroBias_Request(metaclass=Metaclass_Mip3dmCaptureGyroBias_Request):
    """Message class 'Mip3dmCaptureGyroBias_Request'."""

    __slots__ = [
    ]

    _fields_and_field_types = {
    }

    SLOT_TYPES = (
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

# Member 'bias'
import numpy  # noqa: E402, I100

# already imported above
# import rosidl_parser.definition


class Metaclass_Mip3dmCaptureGyroBias_Response(type):
    """Metaclass of message 'Mip3dmCaptureGyroBias_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('microstrain_inertial_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'microstrain_inertial_msgs.srv.Mip3dmCaptureGyroBias_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__mip3dm_capture_gyro_bias__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__mip3dm_capture_gyro_bias__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__mip3dm_capture_gyro_bias__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__mip3dm_capture_gyro_bias__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__mip3dm_capture_gyro_bias__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Mip3dmCaptureGyroBias_Response(metaclass=Metaclass_Mip3dmCaptureGyroBias_Response):
    """Message class 'Mip3dmCaptureGyroBias_Response'."""

    __slots__ = [
        '_bias',
    ]

    _fields_and_field_types = {
        'bias': 'float[3]',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('float'), 3),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        if 'bias' not in kwargs:
            self.bias = numpy.zeros(3, dtype=numpy.float32)
        else:
            self.bias = numpy.array(kwargs.get('bias'), dtype=numpy.float32)
            assert self.bias.shape == (3, )

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if all(self.bias != other.bias):
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def bias(self):
        """Message field 'bias'."""
        return self._bias

    @bias.setter
    def bias(self, value):
        if isinstance(value, numpy.ndarray):
            assert value.dtype == numpy.float32, \
                "The 'bias' numpy.ndarray() must have the dtype of 'numpy.float32'"
            assert value.size == 3, \
                "The 'bias' numpy.ndarray() must have a size of 3"
            self._bias = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) == 3 and
                 all(isinstance(v, float) for v in value) and
                 all(not (val < -3.402823466e+38 or val > 3.402823466e+38) or math.isinf(val) for val in value)), \
                "The 'bias' field must be a set or sequence with length 3 and each value of type 'float' and each float in [-340282346600000016151267322115014000640.000000, 340282346600000016151267322115014000640.000000]"
        self._bias = numpy.array(value, dtype=numpy.float32)


class Metaclass_Mip3dmCaptureGyroBias(type):
    """Metaclass of service 'Mip3dmCaptureGyroBias'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('microstrain_inertial_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'microstrain_inertial_msgs.srv.Mip3dmCaptureGyroBias')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__mip3dm_capture_gyro_bias

            from microstrain_inertial_msgs.srv import _mip3dm_capture_gyro_bias
            if _mip3dm_capture_gyro_bias.Metaclass_Mip3dmCaptureGyroBias_Request._TYPE_SUPPORT is None:
                _mip3dm_capture_gyro_bias.Metaclass_Mip3dmCaptureGyroBias_Request.__import_type_support__()
            if _mip3dm_capture_gyro_bias.Metaclass_Mip3dmCaptureGyroBias_Response._TYPE_SUPPORT is None:
                _mip3dm_capture_gyro_bias.Metaclass_Mip3dmCaptureGyroBias_Response.__import_type_support__()


class Mip3dmCaptureGyroBias(metaclass=Metaclass_Mip3dmCaptureGyroBias):
    from microstrain_inertial_msgs.srv._mip3dm_capture_gyro_bias import Mip3dmCaptureGyroBias_Request as Request
    from microstrain_inertial_msgs.srv._mip3dm_capture_gyro_bias import Mip3dmCaptureGyroBias_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
