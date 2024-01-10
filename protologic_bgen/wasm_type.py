from enum import Enum


class WasmType(Enum):
	u8 = "u8"
	u16 = "u16"
	u32 = "u32"
	u64 = "u64"

	i8 = "i8"
	i16 = "i16"
	i32 = "i32"
	i64 = "i64"

	f32 = "f32"
	f64 = "f64"

	v128 = "v128"

	def __bool__(self):
		return self.value is not None

	@property
	def byteCount(self):
		if self in (WasmType.i8, WasmType.u8):
			return 1
		elif self in (WasmType.i16, WasmType.u16):
			return 2
		elif self in (WasmType.i32, WasmType.u32, WasmType.f32):
			return 4
		elif self in (WasmType.i64, WasmType.u64, WasmType.f64):
			return 8
		elif self in (WasmType.v128,):
			return 16
		else:
			raise ValueError(f"Unknown byte count for {self}")
