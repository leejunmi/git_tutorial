// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from microstrain_inertial_msgs:msg/MipGpsTimestamp.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "microstrain_inertial_msgs/msg/detail/mip_gps_timestamp__rosidl_typesupport_introspection_c.h"
#include "microstrain_inertial_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "microstrain_inertial_msgs/msg/detail/mip_gps_timestamp__functions.h"
#include "microstrain_inertial_msgs/msg/detail/mip_gps_timestamp__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void microstrain_inertial_msgs__msg__MipGpsTimestamp__rosidl_typesupport_introspection_c__MipGpsTimestamp_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  microstrain_inertial_msgs__msg__MipGpsTimestamp__init(message_memory);
}

void microstrain_inertial_msgs__msg__MipGpsTimestamp__rosidl_typesupport_introspection_c__MipGpsTimestamp_fini_function(void * message_memory)
{
  microstrain_inertial_msgs__msg__MipGpsTimestamp__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember microstrain_inertial_msgs__msg__MipGpsTimestamp__rosidl_typesupport_introspection_c__MipGpsTimestamp_message_member_array[2] = {
  {
    "tow",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(microstrain_inertial_msgs__msg__MipGpsTimestamp, tow),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "week_number",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT16,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(microstrain_inertial_msgs__msg__MipGpsTimestamp, week_number),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers microstrain_inertial_msgs__msg__MipGpsTimestamp__rosidl_typesupport_introspection_c__MipGpsTimestamp_message_members = {
  "microstrain_inertial_msgs__msg",  // message namespace
  "MipGpsTimestamp",  // message name
  2,  // number of fields
  sizeof(microstrain_inertial_msgs__msg__MipGpsTimestamp),
  microstrain_inertial_msgs__msg__MipGpsTimestamp__rosidl_typesupport_introspection_c__MipGpsTimestamp_message_member_array,  // message members
  microstrain_inertial_msgs__msg__MipGpsTimestamp__rosidl_typesupport_introspection_c__MipGpsTimestamp_init_function,  // function to initialize message memory (memory has to be allocated)
  microstrain_inertial_msgs__msg__MipGpsTimestamp__rosidl_typesupport_introspection_c__MipGpsTimestamp_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t microstrain_inertial_msgs__msg__MipGpsTimestamp__rosidl_typesupport_introspection_c__MipGpsTimestamp_message_type_support_handle = {
  0,
  &microstrain_inertial_msgs__msg__MipGpsTimestamp__rosidl_typesupport_introspection_c__MipGpsTimestamp_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_microstrain_inertial_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, microstrain_inertial_msgs, msg, MipGpsTimestamp)() {
  if (!microstrain_inertial_msgs__msg__MipGpsTimestamp__rosidl_typesupport_introspection_c__MipGpsTimestamp_message_type_support_handle.typesupport_identifier) {
    microstrain_inertial_msgs__msg__MipGpsTimestamp__rosidl_typesupport_introspection_c__MipGpsTimestamp_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &microstrain_inertial_msgs__msg__MipGpsTimestamp__rosidl_typesupport_introspection_c__MipGpsTimestamp_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
