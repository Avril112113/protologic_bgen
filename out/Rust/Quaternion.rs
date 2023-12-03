// DO NOT MODIFY, THIS FILE IS GENERATED //
// VERSION 0.0.2 //

#[repr(C)]
pub struct Quaternion
{
    pub x: f32,
    pub y: f32,
    pub z: f32,
    pub w: f32,
}
impl Quaternion
{
    pub(crate) fn default() -> Quaternion
    {
        return Quaternion {
			x: 0,
			y: 0,
			z: 0,
			w: 0,
        };
    }
}