// DO NOT MODIFY, THIS FILE IS GENERATED //
// VERSION 0.3.0 //


#pragma once

#include "_import.h"
#include "Vector3.h"
#include "Quaternion.h"
#include "RadarTargetInfo.h"
#include "RadarContactInfo.h"


// queries.h


WASM_IMPORT("protologic", "cpu_get_fuel", cpu_get_fuel, int64_t);

WASM_IMPORT("protologic", "ship_get_position_x", ship_get_position_x, float);

WASM_IMPORT("protologic", "ship_get_position_y", ship_get_position_y, float);

WASM_IMPORT("protologic", "ship_get_position_z", ship_get_position_z, float);

WASM_IMPORT("protologic", "ship_get_position_ptr", ship_get_position_ptr, void, Vector3* dst);

WASM_IMPORT("protologic", "ship_get_velocity_x", ship_get_velocity_x, float);

WASM_IMPORT("protologic", "ship_get_velocity_y", ship_get_velocity_y, float);

WASM_IMPORT("protologic", "ship_get_velocity_z", ship_get_velocity_z, float);

WASM_IMPORT("protologic", "ship_get_velocity_ptr", ship_get_velocity_ptr, void, Vector3* dst);

WASM_IMPORT("protologic", "ship_get_orientation_x", ship_get_orientation_x, float);

WASM_IMPORT("protologic", "ship_get_orientation_y", ship_get_orientation_y, float);

WASM_IMPORT("protologic", "ship_get_orientation_z", ship_get_orientation_z, float);

WASM_IMPORT("protologic", "ship_get_orientation_w", ship_get_orientation_w, float);

WASM_IMPORT("protologic", "ship_get_orientation_ptr", ship_get_orientation_ptr, void, Quaternion* dst);

WASM_IMPORT("protologic", "ship_get_angularvelocity_x", ship_get_angularvelocity_x, float);

WASM_IMPORT("protologic", "ship_get_angularvelocity_y", ship_get_angularvelocity_y, float);

WASM_IMPORT("protologic", "ship_get_angularvelocity_z", ship_get_angularvelocity_z, float);

WASM_IMPORT("protologic", "ship_get_angularvelocity_ptr", ship_get_angularvelocity_ptr, void, Vector3* dst);

WASM_IMPORT("protologic", "engine_get_fuel_amount", engine_get_fuel_amount, float);

WASM_IMPORT("protologic", "engine_get_fuel_capacity", engine_get_fuel_capacity, float);

WASM_IMPORT("protologic", "engine_get_throttle", engine_get_throttle, float);

[[deprecated]] WASM_IMPORT("protologic", "radar_get_target_count", radar_get_target_count, int32_t);

[[deprecated]] WASM_IMPORT("protologic", "radar_get_target_distance", radar_get_target_distance, float, int32_t index);

[[deprecated]] WASM_IMPORT("protologic", "radar_get_target_type", radar_get_target_type, int32_t, int32_t index);

[[deprecated]] WASM_IMPORT("protologic", "radar_get_target_id", radar_get_target_id, int64_t, int32_t index);

[[deprecated]] WASM_IMPORT("protologic", "radar_get_target_info", radar_get_target_info, void, int32_t index, RadarTargetInfo* ptr);

[[deprecated]] WASM_IMPORT("protologic", "radar_get_target_list", radar_get_target_list, void, RadarTargetInfo* ptr, int32_t len);

WASM_IMPORT("protologic", "radar_get_noise", radar_get_noise, float);

WASM_IMPORT("protologic", "radar_get_contact_count", radar_get_contact_count, int32_t);

WASM_IMPORT("protologic", "radar_get_contact_type", radar_get_contact_type, int32_t, int32_t index);

WASM_IMPORT("protologic", "radar_get_contact_id", radar_get_contact_id, int64_t, int32_t index);

WASM_IMPORT("protologic", "radar_get_contact_strength", radar_get_contact_strength, float, int32_t index);

WASM_IMPORT("protologic", "radar_get_contact_position_x", radar_get_contact_position_x, float, int32_t index);

WASM_IMPORT("protologic", "radar_get_contact_position_y", radar_get_contact_position_y, float, int32_t index);

WASM_IMPORT("protologic", "radar_get_contact_position_z", radar_get_contact_position_z, float, int32_t index);

WASM_IMPORT("protologic", "radar_get_contact_position_ptr", radar_get_contact_position_ptr, void, int32_t index, Vector3* dst);

WASM_IMPORT("protologic", "radar_get_contact_info", radar_get_contact_info, void, int32_t index, RadarContactInfo* dst);

WASM_IMPORT("protologic", "radar_get_contact_list", radar_get_contact_list, void, RadarContactInfo* ptr, int32_t len);

WASM_IMPORT("protologic", "gun0_get_bearing", gun0_get_bearing, float);

WASM_IMPORT("protologic", "gun0_get_elevation", gun0_get_elevation, float);

WASM_IMPORT("protologic", "gun0_get_refiretime", gun0_get_refiretime, float);

WASM_IMPORT("protologic", "gun0_get_magazine_capacity", gun0_get_magazine_capacity, int32_t);

WASM_IMPORT("protologic", "gun0_get_magazine_remaining", gun0_get_magazine_remaining, int32_t);

WASM_IMPORT("protologic", "gun0_get_magazine_type", gun0_get_magazine_type, int32_t);

WASM_IMPORT("protologic", "gun0_get_magazine_reloadtime", gun0_get_magazine_reloadtime, float);

WASM_IMPORT("protologic", "gun1_get_bearing", gun1_get_bearing, float);

WASM_IMPORT("protologic", "gun1_get_elevation", gun1_get_elevation, float);

WASM_IMPORT("protologic", "gun1_get_refiretime", gun1_get_refiretime, float);

WASM_IMPORT("protologic", "gun1_get_magazine_capacity", gun1_get_magazine_capacity, int32_t);

WASM_IMPORT("protologic", "gun1_get_magazine_remaining", gun1_get_magazine_remaining, int32_t);

WASM_IMPORT("protologic", "gun1_get_magazine_type", gun1_get_magazine_type, int32_t);

WASM_IMPORT("protologic", "gun1_get_magazine_reloadtime", gun1_get_magazine_reloadtime, float);

WASM_IMPORT("protologic", "gun2_get_bearing", gun2_get_bearing, float);

WASM_IMPORT("protologic", "gun2_get_elevation", gun2_get_elevation, float);

WASM_IMPORT("protologic", "gun2_get_refiretime", gun2_get_refiretime, float);

WASM_IMPORT("protologic", "gun2_get_magazine_capacity", gun2_get_magazine_capacity, int32_t);

WASM_IMPORT("protologic", "gun2_get_magazine_remaining", gun2_get_magazine_remaining, int32_t);

WASM_IMPORT("protologic", "gun2_get_magazine_type", gun2_get_magazine_type, int32_t);

WASM_IMPORT("protologic", "gun2_get_magazine_reloadtime", gun2_get_magazine_reloadtime, float);

WASM_IMPORT("protologic", "gun3_get_bearing", gun3_get_bearing, float);

WASM_IMPORT("protologic", "gun3_get_elevation", gun3_get_elevation, float);

WASM_IMPORT("protologic", "gun3_get_refiretime", gun3_get_refiretime, float);

WASM_IMPORT("protologic", "gun3_get_magazine_capacity", gun3_get_magazine_capacity, int32_t);

WASM_IMPORT("protologic", "gun3_get_magazine_remaining", gun3_get_magazine_remaining, int32_t);

WASM_IMPORT("protologic", "gun3_get_magazine_type", gun3_get_magazine_type, int32_t);

WASM_IMPORT("protologic", "gun3_get_magazine_reloadtime", gun3_get_magazine_reloadtime, float);

