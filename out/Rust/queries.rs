// DO NOT MODIFY, THIS FILE IS GENERATED //
// VERSION 0.0.2 //
mod Vector3;
mod RadarTargetInfo;

#[link(wasm_import_module = "protologic")]
extern
{
	pub fn cpu_get_fuel() -> i64;

	pub fn ship_get_position_x() -> f32;

	pub fn ship_get_position_y() -> f32;

	pub fn ship_get_position_z() -> f32;

	pub fn ship_get_position_ptr(dst: *mut Vector3);

	pub fn ship_get_velocity_x() -> f32;

	pub fn ship_get_velocity_y() -> f32;

	pub fn ship_get_velocity_z() -> f32;

	pub fn ship_get_velocity_ptr(dst: *mut Vector3);

	pub fn ship_get_orientation_x() -> f32;

	pub fn ship_get_orientation_y() -> f32;

	pub fn ship_get_orientation_z() -> f32;

	pub fn ship_get_orientation_w() -> f32;

	pub fn ship_get_orientation_ptr(dst: *mut Vector3);

	pub fn ship_get_angularvelocity_x() -> f32;

	pub fn ship_get_angularvelocity_y() -> f32;

	pub fn ship_get_angularvelocity_z() -> f32;

	pub fn ship_get_angularvelocity_ptr(dst: *mut Vector3);

	pub fn engine_get_fuel_amount() -> f32;

	pub fn engine_get_fuel_capacity() -> f32;

	pub fn engine_get_throttle() -> f32;

	pub fn radar_get_target_count() -> i32;

	pub fn radar_get_target_distance(index: i32) -> f32;

	pub fn radar_get_target_type(index: i32) -> i32;

	pub fn radar_get_target_id(index: i32) -> i64;

	pub fn radar_get_target_info(index: i32, ptr: *mut RadarTargetInfo);

	pub fn radar_get_target_list(ptr: *mut RadarTargetInfo, len: i32);

	pub fn gun0_get_bearing() -> f32;

	pub fn gun0_get_elevation() -> f32;

	pub fn gun0_get_refiretime() -> f32;

	pub fn gun1_get_bearing() -> f32;

	pub fn gun1_get_elevation() -> f32;

	pub fn gun1_get_refiretime() -> f32;

	pub fn gun2_get_bearing() -> f32;

	pub fn gun2_get_elevation() -> f32;

	pub fn gun2_get_refiretime() -> f32;

	pub fn gun3_get_bearing() -> f32;

	pub fn gun3_get_elevation() -> f32;

	pub fn gun3_get_refiretime() -> f32;

}