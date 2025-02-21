# generated from rosidl_generator_py/resource/_idl.py.em
# with input from microstrain_inertial_msgs:msg/MipFilterGnssDualAntennaStatus.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_MipFilterGnssDualAntennaStatus(type):
    """Metaclass of message 'MipFilterGnssDualAntennaStatus'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'FIX_TYPE_FIX_NONE': 0,
        'FIX_TYPE_FIX_DA_FLOAT': 1,
        'FIX_TYPE_FIX_DA_FIXED': 2,
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
                'microstrain_inertial_msgs.msg.MipFilterGnssDualAntennaStatus')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__mip_filter_gnss_dual_antenna_status
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__mip_filter_gnss_dual_antenna_status
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__mip_filter_gnss_dual_antenna_status
            cls._TYPE_SUPPORT = module.type_support_msg__msg__mip_filter_gnss_dual_antenna_status
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__mip_filter_gnss_dual_antenna_status

            from microstrain_inertial_msgs.msg import MipFilterGnssDualAntennaStatusStatusFlags
            if MipFilterGnssDualAntennaStatusStatusFlags.__class__._TYPE_SUPPORT is None:
                MipFilterGnssDualAntennaStatusStatusFlags.__class__.__import_type_support__()

            from microstrain_inertial_msgs.msg import MipHeader
            if MipHeader.__class__._TYPE_SUPPORT is None:
                MipHeader.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'FIX_TYPE_FIX_NONE': cls.__constants['FIX_TYPE_FIX_NONE'],
            'FIX_TYPE_FIX_DA_FLOAT': cls.__constants['FIX_TYPE_FIX_DA_FLOAT'],
            'FIX_TYPE_FIX_DA_FIXED': cls.__constants['FIX_TYPE_FIX_DA_FIXED'],
        }

    @property
    def FIX_TYPE_FIX_NONE(self):
        """Message constant 'FIX_TYPE_FIX_NONE'."""
        return Metaclass_MipFilterGnssDualAntennaStatus.__constants['FIX_TYPE_FIX_NONE']

    @property
    def FIX_TYPE_FIX_DA_FLOAT(self):
        """Message constant 'FIX_TYPE_FIX_DA_FLOAT'."""
        return Metaclass_MipFilterGnssDualAntennaStatus.__constants['FIX_TYPE_FIX_DA_FLOAT']

    @property
    def FIX_TYPE_FIX_DA_FIXED(self):
        """Message constant 'FIX_TYPE_FIX_DA_FIXED'."""
        return Metaclass_MipFilterGnssDualAntennaStatus.__constants['FIX_TYPE_FIX_DA_FIXED']


class MipFilterGnssDualAntennaStatus(metaclass=Metaclass_MipFilterGnssDualAntennaStatus):
    """
    Message class 'MipFilterGnssDualAntennaStatus'.

    Constants:
      FIX_TYPE_FIX_NONE
      FIX_TYPE_FIX_DA_FLOAT
      FIX_TYPE_FIX_DA_FIXED
    """

    __slots__ = [
        '_header',
        '_time_of_week',
        '_heading',
        '_heading_unc',
        '_fix_type',
        '_status_flags',
        '_valid_flags',
    ]

    _fields_and_field_types = {
        'header': 'microstrain_inertial_msgs/MipHeader',
        'time_of_week': 'float',
        'heading': 'float',
        'heading_unc': 'float',
        'fix_type': 'uint8',
        'status_flags': 'microstrain_inertial_msgs/MipFilterGnssDualAntennaStatusStatusFlags',
        'valid_flags': 'uint16',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['microstrain_inertial_msgs', 'msg'], 'MipHeader'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['microstrain_inertial_msgs', 'msg'], 'MipFilterGnssDualAntennaStatusStatusFlags'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from microstrain_inertial_msgs.msg import MipHeader
        self.header = kwargs.get('header', MipHeader())
        self.time_of_week = kwargs.get('time_of_week', float())
        self.heading = kwargs.get('heading', float())
        self.heading_unc = kwargs.get('heading_unc', float())
        self.fix_type = kwargs.get('fix_type', int())
        from microstrain_inertial_msgs.msg import MipFilterGnssDualAntennaStatusStatusFlags
        self.status_flags = kwargs.get('status_flags', MipFilterGnssDualAntennaStatusStatusFlags())
        self.valid_flags = kwargs.get('valid_flags', int())

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
        if self.header != other.header:
            return False
        if self.time_of_week != other.time_of_week:
            return False
        if self.heading != other.heading:
            return False
        if self.heading_unc != other.heading_unc:
            return False
        if self.fix_type != other.fix_type:
            return False
        if self.status_flags != other.status_flags:
            return False
        if self.valid_flags != other.valid_flags:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def header(self):
        """Message field 'header'."""
        return self._header

    @header.setter
    def header(self, value):
        if __debug__:
            from microstrain_inertial_msgs.msg import MipHeader
            assert \
                isinstance(value, MipHeader), \
                "The 'header' field must be a sub message of type 'MipHeader'"
        self._header = value

    @builtins.property
    def time_of_week(self):
        """Message field 'time_of_week'."""
        return self._time_of_week

    @time_of_week.setter
    def time_of_week(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'time_of_week' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'time_of_week' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._time_of_week = value

    @builtins.property
    def heading(self):
        """Message field 'heading'."""
        return self._heading

    @heading.setter
    def heading(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'heading' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'heading' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._heading = value

    @builtins.property
    def heading_unc(self):
        """Message field 'heading_unc'."""
        return self._heading_unc

    @heading_unc.setter
    def heading_unc(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'heading_unc' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'heading_unc' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._heading_unc = value

    @builtins.property
    def fix_type(self):
        """Message field 'fix_type'."""
        return self._fix_type

    @fix_type.setter
    def fix_type(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'fix_type' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'fix_type' field must be an unsigned integer in [0, 255]"
        self._fix_type = value

    @builtins.property
    def status_flags(self):
        """Message field 'status_flags'."""
        return self._status_flags

    @status_flags.setter
    def status_flags(self, value):
        if __debug__:
            from microstrain_inertial_msgs.msg import MipFilterGnssDualAntennaStatusStatusFlags
            assert \
                isinstance(value, MipFilterGnssDualAntennaStatusStatusFlags), \
                "The 'status_flags' field must be a sub message of type 'MipFilterGnssDualAntennaStatusStatusFlags'"
        self._status_flags = value

    @builtins.property
    def valid_flags(self):
        """Message field 'valid_flags'."""
        return self._valid_flags

    @valid_flags.setter
    def valid_flags(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'valid_flags' field must be of type 'int'"
            assert value >= 0 and value < 65536, \
                "The 'valid_flags' field must be an unsigned integer in [0, 65535]"
        self._valid_flags = value
