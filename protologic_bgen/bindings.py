from dataclasses import dataclass

from .wasm_type import WasmType


@dataclass(init=True)
class BindingsFunctionResult:
	"""
	A wasm exported function result.
	"""

	name: str
	type: WasmType

	@classmethod
	def fromJson(cls, data: dict):
		return cls(
			name=data["name"],
			type=WasmType(data["type"]),
		)


@dataclass(init=True)
class BindingsFunctionArg:
	"""
	A wasm exported function argument.
	"""

	name: str
	type: WasmType

	@classmethod
	def fromJson(cls, data: dict):
		return cls(
			name=data["name"],
			type=WasmType(data["type"]),
		)


@dataclass(init=True)
class BindingsFunction:
	"""
	A single wasm exported function, and it's related info.
	"""

	name: str
	args: list[BindingsFunctionArg]
	results: list[BindingsFunctionResult]

	@classmethod
	def fromJson(cls, name: str, data: dict):
		return cls(
			name=name,
			args=[BindingsFunctionArg.fromJson(arg) for arg in data["args"]] if "args" in data else [],
			results=[BindingsFunctionResult.fromJson(arg) for arg in data["results"]] if "results" in data else []
		)

	def getArg(self, index: int, default=None):
		if index < 0 or index >= len(self.args):
			return default
		return self.args[index]

	def getResult(self, index: int, default=None):
		if index < 0 or index >= len(self.results):
			return default
		return self.results[index]


@dataclass(init=True)
class BindingsGroup:
	"""
	A collection of BindingsFunction
	"""

	name: str
	functions: dict[str, BindingsFunction]

	@classmethod
	def fromJson(cls, name: str, data: dict):
		return cls(
			name=name,
			functions={name: BindingsFunction.fromJson(name, function) for name, function in data.items()}
		)

	def __iter__(self):
		return self.functions.values().__iter__()

	def __getitem__(self, function: str) -> BindingsFunction:
		return self.functions[function]


@dataclass(init=True)
class Bindings:
	"""
	Top-level class for parsing `protologic_bindings.json`.
	A collection of BindingsGroup
	"""

	groups: dict[str, BindingsGroup]

	@classmethod
	def fromJson(cls, data: dict):
		return cls(
			groups={name: BindingsGroup.fromJson(name, group) for name, group in data["groups"].items()}
		)

	def __iter__(self):
		return self.groups.values().__iter__()

	def __getitem__(self, group: str) -> BindingsGroup:
		return self.groups[group]
