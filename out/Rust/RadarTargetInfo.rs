// DO NOT MODIFY, THIS FILE IS GENERATED //
// VERSION 0.0.2 //


/// Target info.
#[repr(C)]
pub struct RadarTargetInfo
{
    pub id: i64,
    pub type: i32,
    pub distance: f32,
}
impl RadarTargetInfo
{
    pub(crate) fn default() -> RadarTargetInfo
    {
        return RadarTargetInfo {
			id: -1,
			type: -1,
			distance: -1,
        };
    }
}