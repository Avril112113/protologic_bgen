from collections import OrderedDict
from dataclasses import dataclass

from .wasm_type import WasmType


@dataclass(init=True)
class BindingsDef:
	"""
	A wasm exported function argument.
	"""

	_bindings: "Bindings"
	name: str
	type: WasmType
	ptr: "BindingsStruct | None"
	ptrCount: "str | None"
	default: int | float | None
	description: str | None

	@classmethod
	def fromJson(cls, _bindings: "Bindings", data: dict):
		return cls(
			_bindings=_bindings,
			name=data["name"],
			type=WasmType(data["type"]),
			ptr=_bindings.structs[data["ptr"]] if "ptr" in data else None,
			ptrCount=data.get("ptrCount", None),
			default=data.get("default", None),
			description=data.get("description", None),
		)

	@property
	def is_ptr(self):
		return self.ptr is not None

	def ifPtr(self, s: str, default=""):
		return s if self.ptr is not None else default


@dataclass(init=True)
class BindingsFunction:
	"""
	A single wasm exported function, and it's related info.
	"""

	_bindings: "Bindings"
	name: str
	deprecated: str | None
	description: str | None
	args: list[BindingsDef]
	results: list[BindingsDef]

	@classmethod
	def fromJson(cls, _bindings: "Bindings", name: str, data: dict):
		return cls(
			_bindings=_bindings,
			name=name,
			deprecated=data.get("deprecated", None),
			description=data.get("description", None),
			args=[BindingsDef.fromJson(_bindings, arg) for arg in data["args"]] if "args" in data else [],
			results=[BindingsDef.fromJson(_bindings, result) for result in data["results"]] if "results" in data else []
		)

	def getArg(self, index: int, default=None):
		if index < 0 or index >= len(self.args):
			return default
		return self.args[index]

	def getResult(self, index: int, default=None):
		if index < 0 or index >= len(self.results):
			return default
		return self.results[index]

	def getUsedStructs(self, deprecated=True) -> list["BindingsStruct"]:
		structs = []
		for arg in self.args:
			if arg.ptr is not None and arg.ptr not in structs:
				structs.append(arg.ptr)
		for result in self.results:
			if result.ptr is not None and result.ptr not in structs:
				structs.append(result.ptr)
		return structs

	def hasPtrArg(self):
		return any(arg.ptr is not None for arg in self.args)

	def hasPtrCountArg(self):
		return any(arg.ptrCount is not None for arg in self.args)


@dataclass(init=True)
class BindingsGroup:
	"""
	A collection of BindingsFunction
	"""

	_bindings: "Bindings"
	name: str
	description: str | None
	module: str
	functions: dict[str, BindingsFunction]

	@classmethod
	def fromJson(cls, _bindings: "Bindings", name: str, data: dict):
		return cls(
			_bindings=_bindings,
			name=name,
			description=data.get("description", None),
			module=data["module"],
			functions={name: BindingsFunction.fromJson(_bindings, name, function) for name, function in data["functions"].items()}
		)

	def getUsedStructs(self) -> list["BindingsStruct"]:
		structs = []
		for func in self.functions.values():
			structs.extend(struct for struct in func.getUsedStructs() if struct not in structs)
		return structs

	def __iter__(self):
		return self.functions.values().__iter__()

	def __getitem__(self, function: str) -> BindingsFunction:
		return self.functions[function]


@dataclass(init=True)
class BindingsStruct:
	"""
	A single struct defining the layout of a pointer.
	"""

	_bindings: "Bindings"
	name: str
	deprecated: str | None
	description: str | None
	fields: OrderedDict[str, BindingsDef]

	@classmethod
	def fromJson(cls, _bindings: "Bindings", name: str, data: dict):
		return cls(
			_bindings=_bindings,
			name=name,
			deprecated=data.get("deprecated", None),
			description=data.get("description", None),
			fields=OrderedDict((field["name"], BindingsDef.fromJson(_bindings, field)) for field in data["fields"])
		)

	def __iter__(self):
		return self.fields.values().__iter__()

	def __getitem__(self, field: str) -> BindingsDef:
		return self.fields[field]


class Bindings:
	"""
	Top-level class for parsing `protologic_bindings.json`.
	A collection of BindingsGroup
	"""

	version: str
	structs: dict[str, BindingsStruct]
	groups: dict[str, BindingsGroup]

	@classmethod
	def fromJson(cls, data: dict):
		_bindings = cls()
		_bindings.version = data["version"]
		_bindings.structs = {name: BindingsStruct.fromJson(_bindings, name, struct) for name, struct in data["structs"].items()}
		_bindings.groups = {name: BindingsGroup.fromJson(_bindings, name, group) for name, group in data["groups"].items()}
		return _bindings

	def __iter__(self):
		return self.groups.values().__iter__()

	def __getitem__(self, group: str) -> BindingsGroup:
		return self.groups[group]
