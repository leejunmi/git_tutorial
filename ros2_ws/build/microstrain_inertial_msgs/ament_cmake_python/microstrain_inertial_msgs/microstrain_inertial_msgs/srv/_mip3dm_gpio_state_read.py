# generated from rosidl_generator_py/resource/_idl.py.em
# with input from microstrain_inertial_msgs:srv/Mip3dmGpioStateRead.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Mip3dmGpioStateRead_Request(type):
    """Metaclass of message 'Mip3dmGpioStateRead_Request'."""

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
                'microstrain_inertial_msgs.srv.Mip3dmGpioStateRead_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__mip3dm_gpio_state_read__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__mip3dm_gpio_state_read__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__mip3dm_gpio_state_read__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__mip3dm_gpio_state_read__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__mip3dm_gpio_state_read__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Mip3dmGpioStateRead_Request(metaclass=Metaclass_Mip3dmGpioStateRead_Request):
    """Message class 'Mip3dmGpioStateRead_Request'."""

    __slots__ = [
        '_pin',
    ]

    _fields_and_field_types = {
        'pin': 'uint8',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.pin = kwargs.get('pin', int())

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
        if self.pin != other.pin:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def pin(self):
        """Message field 'pin'."""
        return self._pin

    @pin.setter
    def pin(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'pin' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'pin' field must be an unsigned integer in [0, 255]"
        self._pin = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_Mip3dmGpioStateRead_Response(type):
    """Metaclass of message 'Mip3dmGpioStateRead_Response'."""

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
                'microstrain_inertial_msgs.srv.Mip3dmGpioStateRead_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__mip3dm_gpio_state_read__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__mip3dm_gpio_state_read__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__mip3dm_gpio_state_read__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__mip3dm_gpio_state_read__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__mip3dm_gpio_state_read__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Mip3dmGpioStateRead_Response(metaclass=Metaclass_Mip3dmGpioStateRead_Response):
    """Message class 'Mip3dmGpioStateRead_Response'."""

    __slots__ = [
        '_pin',
        '_state',
    ]

    _fields_and_field_types = {
        'pin': 'uint8',
        'state': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.pin = kwargs.get('pin', int())
        self.state = kwargs.get('state', bool())

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
        if self.pin != other.pin:
            return False
        if self.state != other.state:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def pin(self):
        """Message field 'pin'."""
        return self._pin

    @pin.setter
    def pin(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'pin' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'pin' field must be an unsigned integer in [0, 255]"
        self._pin = value

    @builtins.property
    def state(self):
        """Message field 'state'."""
        return self._state

    @state.setter
    def state(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'state' field must be of type 'bool'"
        self._state = value


class Metaclass_Mip3dmGpioStateRead(type):
    """Metaclass of service 'Mip3dmGpioStateRead'."""

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
                'microstrain_inertial_msgs.srv.Mip3dmGpioStateRead')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__mip3dm_gpio_state_read

            from microstrain_inertial_msgs.srv import _mip3dm_gpio_state_read
            if _mip3dm_gpio_state_read.Metaclass_Mip3dmGpioStateRead_Request._TYPE_SUPPORT is None:
                _mip3dm_gpio_state_read.Metaclass_Mip3dmGpioStateRead_Request.__import_type_support__()
            if _mip3dm_gpio_state_read.Metaclass_Mip3dmGpioStateRead_Response._TYPE_SUPPORT is None:
                _mip3dm_gpio_state_read.Metaclass_Mip3dmGpioStateRead_Response.__import_type_support__()


class Mip3dmGpioStateRead(metaclass=Metaclass_Mip3dmGpioStateRead):
    from microstrain_inertial_msgs.srv._mip3dm_gpio_state_read import Mip3dmGpioStateRead_Request as Request
    from microstrain_inertial_msgs.srv._mip3dm_gpio_state_read import Mip3dmGpioStateRead_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
