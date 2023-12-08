-- DO NOT MODIFY, THIS FILE IS GENERATED --
-- VERSION 0.1.0 --
---@meta

---@class ProtoLogic
---@field cpu_get_fuel fun(): integer
---@field ship_get_position_x fun(): number
---@field ship_get_position_y fun(): number
---@field ship_get_position_z fun(): number
---@field ship_get_position_ptr fun(): number, number, number
---@field ship_get_velocity_x fun(): number
---@field ship_get_velocity_y fun(): number
---@field ship_get_velocity_z fun(): number
---@field ship_get_velocity_ptr fun(): number, number, number
---@field ship_get_orientation_x fun(): number
---@field ship_get_orientation_y fun(): number
---@field ship_get_orientation_z fun(): number
---@field ship_get_orientation_w fun(): number
---@field ship_get_orientation_ptr fun(): number, number, number, number
---@field ship_get_angularvelocity_x fun(): number
---@field ship_get_angularvelocity_y fun(): number
---@field ship_get_angularvelocity_z fun(): number
---@field ship_get_angularvelocity_ptr fun(): number, number, number
---@field engine_get_fuel_amount fun(): number
---@field engine_get_fuel_capacity fun(): number
---@field engine_get_throttle fun(): number
---@field radar_get_noise fun(): number
---@field radar_get_contact_count fun(): integer
---@field radar_get_contact_type fun(index: integer): integer
---@field radar_get_contact_id fun(index: integer): integer
---@field radar_get_contact_strength fun(index: integer): number
---@field radar_get_contact_position_x fun(index: integer): number
---@field radar_get_contact_position_y fun(index: integer): number
---@field radar_get_contact_position_z fun(index: integer): number
---@field radar_get_contact_position_ptr fun(index: integer): number, number, number
---@field radar_get_contact_info fun(index: integer): protologic.RadarContactInfo
---@field gun0_get_bearing fun(): number
---@field gun0_get_elevation fun(): number
---@field gun0_get_refiretime fun(): number
---@field gun1_get_bearing fun(): number
---@field gun1_get_elevation fun(): number
---@field gun1_get_refiretime fun(): number
---@field gun2_get_bearing fun(): number
---@field gun2_get_elevation fun(): number
---@field gun2_get_refiretime fun(): number
---@field gun3_get_bearing fun(): number
---@field gun3_get_elevation fun(): number
---@field gun3_get_refiretime fun(): number
protologic = nil
