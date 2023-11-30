from enum import Enum


class WasmType(Enum):
	NONE = None
	i32 = "i32"
	i64 = "i64"
	f32 = "f32"
	f64 = "f32"
	v128 = "v128"

	def __bool__(self):
		return self.value is not None
