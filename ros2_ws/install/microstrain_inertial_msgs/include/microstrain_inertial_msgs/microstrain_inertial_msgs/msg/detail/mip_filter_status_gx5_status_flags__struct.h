// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from microstrain_inertial_msgs:msg/MipFilterStatusGx5StatusFlags.idl
// generated code does not contain a copyright notice

#ifndef MICROSTRAIN_INERTIAL_MSGS__MSG__DETAIL__MIP_FILTER_STATUS_GX5_STATUS_FLAGS__STRUCT_H_
#define MICROSTRAIN_INERTIAL_MSGS__MSG__DETAIL__MIP_FILTER_STATUS_GX5_STATUS_FLAGS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/MipFilterStatusGx5StatusFlags in the package microstrain_inertial_msgs.
/**
  * Message definition for the Status Flags (GX5, CV5, CX5, etc.) field of https://s3.amazonaws.com/files.microstrain.com/GQ7+User+Manual/external_content/dcp/Data/filter_data/data/mip_field_filter_status.htm?Highlight=filter%20status
  *   Note: This message will never be published on it's own, only included in other messages.
 */
typedef struct microstrain_inertial_msgs__msg__MipFilterStatusGx5StatusFlags
{
  bool init_no_attitude;
  bool init_no_position_velocity;
  bool run_imu_unavailable;
  bool run_gps_unavailable;
  bool run_matrix_singularity;
  bool run_position_covariance_warning;
  bool run_velocity_covariance_warning;
  bool run_attitude_covariance_warning;
  bool run_nan_in_solution_warning;
  bool run_gyro_bias_est_high_warning;
  bool run_accel_bias_est_high_warning;
  bool run_gyro_scale_factor_est_high_warning;
  bool run_accel_scale_factor_est_high_warning;
  bool run_mag_bias_est_high_warning;
  bool run_ant_offset_correction_est_high_warning;
  bool run_mag_hard_iron_est_high_warning;
  bool run_mag_soft_iron_est_high_warning;
} microstrain_inertial_msgs__msg__MipFilterStatusGx5StatusFlags;

// Struct for a sequence of microstrain_inertial_msgs__msg__MipFilterStatusGx5StatusFlags.
typedef struct microstrain_inertial_msgs__msg__MipFilterStatusGx5StatusFlags__Sequence
{
  microstrain_inertial_msgs__msg__MipFilterStatusGx5StatusFlags * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} microstrain_inertial_msgs__msg__MipFilterStatusGx5StatusFlags__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MICROSTRAIN_INERTIAL_MSGS__MSG__DETAIL__MIP_FILTER_STATUS_GX5_STATUS_FLAGS__STRUCT_H_
