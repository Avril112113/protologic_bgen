from collections import OrderedDict
from typing import Self, Union

from .wasm_type import WasmType


class BindingsDef:
	name: str
	type: Union["BindingsStruct",WasmType]
	description: str = ""
	count: str | None = None
	offset: int|None = None

	def __init__(self, bindings: "Bindings"):
		self._bindings = bindings

	def __repr__(self):
		return f"<{self.__class__.__name__} name=\"{self.name}\">"

	def updateFromJson(self, data: dict) -> Self:
		self.name = data["name"]
		type_name = data["type"]
		if type_name in WasmType:
			self.type = WasmType(type_name)
		elif type_name in self._bindings.structs:
			self.type = self._bindings.structs[type_name]
		else:
			raise ValueError(f"Invalid type '{type_name}'")
		self.description = data.get("description", self.description)
		self.count = data.get("count", self.count)
		self.offset = data.get("offset", self.offset)
		return self


class BindingsQuickStateInfo:
	name: str
	_func_name: str
	init_function: "BindingsFunction"

	def __init__(self, bindings: "Bindings"):
		self._bindings = bindings

	def updateFromJson(self, data: dict) -> Self:
		self.name = data["name"]
		self._func_name = data["init_function"]
		return self

	@property
	def init_function_group(self):
		found_groups = tuple([group for group in self._bindings.groups.values() if self._func_name in group.functions])
		if len(found_groups) <= 0:
			raise ValueError(f"Missing init_function '{self._func_name}'")
		elif len(found_groups) > 1:
			raise ValueError(f"Multiple init_function '{self._func_name}'")
		return found_groups[0]

	@property
	def init_function(self):
		return self.init_function_group.functions[self._func_name]


class BindingsStruct:
	name: str
	description: str = ""
	deprecated: bool = False
	fields: OrderedDict[str, BindingsDef]
	quickstate: BindingsQuickStateInfo|None = None
	_has_updated = False

	def __init__(self, bindings: "Bindings", name: str):
		self._bindings = bindings
		self.name = name
		self.fields = OrderedDict()

	def __repr__(self):
		return f"<{self.__class__.__name__} name=\"{self.name}\">"

	def __iter__(self):
		return self.fields.values().__iter__()

	def __getitem__(self, name: str):
		return self.fields.get(name, None)

	def updateFromJson(self, data: dict) -> Self:
		self._has_updated = True
		self.description = data.get("description", self.description)
		self.deprecated = data.get("deprecated", self.deprecated)
		self.quickstate = BindingsQuickStateInfo(self._bindings).updateFromJson(data["quickstate"]) if "quickstate" in data else None
		for fieldData in data["fields"]:
			field = self.fields.get(fieldData["name"], BindingsDef(self._bindings))
			field.updateFromJson(fieldData)
			self.fields[field.name] = field
		if not all(field.offset is not None for field in self.fields.values()):
			raise ValueError(f"All fields in struct '{self.name}' must have an offset defined.")
		return self

	def getUsedStructs(self):
		structs = []
		for field in self.fields.values():
			if isinstance(field.type, BindingsStruct) and field.type not in structs:
				structs.append(field.type)
		return structs

	@property
	def byteCount(self):
		lastField = None
		for field in self.fields.values():
			if lastField is None or lastField.offset < field.offset:
				lastField = field
		if lastField is None:
			return 0
		return lastField.offset + lastField.type.byteCount


class BindingsFunction:
	name: str
	description: str = ""
	deprecated: bool = False
	args: list[BindingsDef]
	results: list[BindingsDef]

	def __init__(self, bindings: "Bindings", name: str):
		self._bindings = bindings
		self.name = name
		self.args = []
		self.results = []

	def __repr__(self):
		return f"<{self.__class__.__name__} name=\"{self.name}\">"

	def updateFromJson(self, data: dict) -> Self:
		self.description = data.get("description", self.description)
		self.deprecated = data.get("deprecated", self.deprecated)
		for argData in data.get("args", []):
			self.args.append(BindingsDef(self._bindings).updateFromJson(argData))
		for resultData in data.get("results", []):
			self.results.append(BindingsDef(self._bindings).updateFromJson(resultData))
		return self

	@property
	def isMultiResult(self):
		return len(self.results) > 1

	@property
	def hasCountArg(self):
		return any(arg.count is not None for arg in self.args)

	@property
	def hasStructArg(self):
		return any(isinstance(arg.type, BindingsStruct) for arg in self.args)

	def getResult(self, idx=0):
		if idx >= len(self.results):
			return None
		return self.results[idx]

	def getUsedStructs(self):
		structs = []
		for arg in self.args:
			if isinstance(arg.type, BindingsStruct) and arg.type not in structs:
				structs.append(arg.type)
		for result in self.results:
			if isinstance(result.type, BindingsStruct) and result.type not in structs:
				structs.append(result.type)
		return structs


class BindingsGroup:
	name: str
	module: str
	description: str = ""
	functions: OrderedDict[str, BindingsFunction]

	def __init__(self, bindings: "Bindings", name: str):
		self._bindings = bindings
		self.name = name
		self.functions = OrderedDict()

	def __repr__(self):
		return f"<{self.__class__.__name__} name=\"{self.name}\">"

	def __iter__(self):
		return self.functions.values().__iter__()

	def updateFromJson(self, data: dict) -> Self:
		self.module = data["module"]
		self.description = data.get("description", self.description)
		for name, funcData in data["functions"].items():
			self.functions[name] = BindingsFunction(self._bindings, name).updateFromJson(funcData)
		return self

	def getUsedStructs(self):
		structs = []
		for func in self.functions.values():
			for struct in func.getUsedStructs():
				if struct not in structs:
					structs.append(struct)
		return structs


class Bindings:
	version: str

	def __init__(self):
		self.structs: dict[str, BindingsStruct] = {}
		self.groups: dict[str, BindingsGroup] = {}

	def __repr__(self):
		return f"<{self.__class__.__name__} version=\"{self.version}\">"

	def updateFromJson(self, data: dict) -> Self:
		self.version = data["version"]
		for name, structData in data["structs"].items():
			self.structs[name] = BindingsStruct(self, name).updateFromJson(structData)
		for name, groupData in data["groups"].items():
			self.groups[name] = BindingsGroup(self, name).updateFromJson(groupData)
		for struct in self.structs.values():
			# noinspection PyProtectedMember
			if not struct._has_updated:
				raise ValueError(f"Missing struct definition {struct.name}")
		return self
