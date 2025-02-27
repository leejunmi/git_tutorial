// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from microstrain_inertial_msgs:msg/MipFilterGnssPositionAidingStatusStatus.idl
// generated code does not contain a copyright notice

#ifndef MICROSTRAIN_INERTIAL_MSGS__MSG__DETAIL__MIP_FILTER_GNSS_POSITION_AIDING_STATUS_STATUS__STRUCT_H_
#define MICROSTRAIN_INERTIAL_MSGS__MSG__DETAIL__MIP_FILTER_GNSS_POSITION_AIDING_STATUS_STATUS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/MipFilterGnssPositionAidingStatusStatus in the package microstrain_inertial_msgs.
/**
  * Message definition for the Status field of https://s3.amazonaws.com/files.microstrain.com/GQ7+User+Manual/external_content/dcp/Data/filter_data/data/mip_field_filter_gnss_pos_aid_status.htm?Highlight=gnss%20position%20aiding
  *   Note: This message will never be published on it's own, only included in other messages.
 */
typedef struct microstrain_inertial_msgs__msg__MipFilterGnssPositionAidingStatusStatus
{
  /// If 1, the Kalman filter is processing raw range information from this GNSS module
  bool tight_coupling;
  /// If 1, the Kalman filter is processing RTK corrections from this GNSS module
  bool differential;
  /// If 1, the Kalman filter has an RTK integer fix from this GNSS module, indicating the best position performance possible
  bool integer_fix;
  /// If 1, the Kalman filter is using GPS L1 measurements
  bool gps_l1;
  /// If 1, the Kalman filter is using GPS L2 measurements
  bool gps_l2;
  /// If 1, the Kalman filter is using GPS L5 measurements
  bool gps_l5;
  /// If 1, the Kalman filter is using GLONASS L1 measurements
  bool glo_l1;
  /// If 1, the Kalman filter is using GLONASS L2 measurements
  bool glo_l2;
  /// If 1, the Kalman filter is using Galileo E1 measurements
  bool gal_e1;
  /// If 1, the Kalman filter is using Galileo E5 measurements
  bool gal_e5;
  /// If 1, the Kalman filter is using Galileo E6 measurements
  bool gal_e6;
  /// If 1, the Kalman filter is using Beidou B1 measurements (not enabled on GQ7 currently)
  bool bei_b1;
  /// If 1, the Kalman filter is using Beidou B2 measurements (not enabled on GQ7 currently)
  bool bei_b2;
  /// If 1, the Kalman filter is using Beidou B3 measurements (not enabled on GQ7 currently)
  bool bei_b3;
  /// If 1, this GNSS module is reporting no position fix
  bool no_fix;
  /// If 1, there is likely an issue with the antenna offset for this GNSS module
  bool config_error;
} microstrain_inertial_msgs__msg__MipFilterGnssPositionAidingStatusStatus;

// Struct for a sequence of microstrain_inertial_msgs__msg__MipFilterGnssPositionAidingStatusStatus.
typedef struct microstrain_inertial_msgs__msg__MipFilterGnssPositionAidingStatusStatus__Sequence
{
  microstrain_inertial_msgs__msg__MipFilterGnssPositionAidingStatusStatus * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} microstrain_inertial_msgs__msg__MipFilterGnssPositionAidingStatusStatus__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MICROSTRAIN_INERTIAL_MSGS__MSG__DETAIL__MIP_FILTER_GNSS_POSITION_AIDING_STATUS_STATUS__STRUCT_H_
