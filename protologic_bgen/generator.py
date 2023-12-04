from glob import glob, iglob
import os.path
from fnmatch import fnmatch
import json
import sys
import em
import re

from .wasm_type import WasmType
from .bindings import Bindings, BindingsDef, BindingsStruct


def _files_to_file(files: list[str], missing_msg: str):
	if len(files) <= 0:
		print(missing_msg)
		return None
	elif len(files) > 1:
		print(f"Multiple files exist {files}")
		return None
	return files[0]


class GeneratorTemplate:
	_SPECIAL_FILES = [r"struct.*.em", r"group.*.em"]

	def __init__(self, bindings: Bindings, template_root: str, out_path: str):
		self.bindings = bindings
		self.template_root = template_root
		self.out_path = out_path

		with open(os.path.join(template_root, "config.json"), "r") as f:
			self.config = json.loads(f.read())

		self.template_globals = {
			"bindings": self.bindings,
			"config": self.config,
			"desc2comment": self._template_desc2comment,
			"retype": self._template_retype,
			"getDefault": self._template_getdefault,
		}
		self.template_config = em.Configuration(useProxy=False)

	def generate(self):
		group_file = _files_to_file(glob(os.path.join(self.template_root, "group.*.em")), f"Missing group file in {self.template_root}")
		struct_file = _files_to_file(glob(os.path.join(self.template_root, "struct.*.em")), f"Missing struct file in {self.template_root}")
		extra_files = list(
			filter(
				lambda file: not any(fnmatch(file, os.path.join(self.template_root, patt)) for patt in self._SPECIAL_FILES),
				iglob(os.path.join(self.template_root, "**", "*.em"), recursive=True)
			)
		)

		if group_file is not None:
			for group in self.bindings.groups.values():
				out_file = os.path.join(self.out_path, group.name + group_file[group_file.find("."):group_file.rfind(".")])
				self.render(group_file, out_file, {
					"group": group
				})

		if struct_file is not None:
			for struct in self.bindings.structs.values():
				out_file = os.path.join(self.out_path, struct.name + struct_file[struct_file.find("."):struct_file.rfind(".")])
				self.render(struct_file, out_file, {
					"struct": struct
				})

		for extra_file in extra_files:
			out_file = extra_file[:extra_file.rfind(".")].replace(self.template_root, self.out_path)
			self.render(extra_file, out_file, {})

	def render(self, file: str, out: str, extra_variables: dict):
		print(f"- '{file}' -> '{out}'")
		skip = False
		def setSkip():
			nonlocal skip
			skip = True

		variables: dict = {
			"skip": setSkip,
		}
		variables.update(self.template_globals)
		variables.update(extra_variables)
		with open(file, "r") as f:
			data = f.read()
		with em.Interpreter(config=self.template_config) as interp:
			result = interp.expand(data, name=file, locals=variables)
		if skip:
			return
		if not os.path.exists(os.path.dirname(out)):
			os.mkdir(os.path.dirname(out))
		with open(out, "w") as f:
			f.write(result)

	@classmethod
	def _template_desc2comment(cls, description: str, comment: str):
		if description is None:
			return comment
		return comment + description.strip().replace("\n", f"\n{comment}")

	def _template_retype(self, bdef: BindingsDef | WasmType | str | None, config_entry="WasmType", struct=True):
		# noinspection PyTypedDict
		if bdef is None:
			return self.config[config_entry].get("NONE", "")
		if isinstance(bdef, WasmType):
			bdef = bdef.name
		elif isinstance(bdef, BindingsDef):
			if struct and bdef.ptr is not None:
				return bdef.ptr.name
			bdef = bdef.type.name
		elif isinstance(bdef, BindingsStruct):
			return bdef.name
		return self.config[config_entry].get(bdef)

	@classmethod
	def _template_getdefault(cls, bdef: BindingsDef):
		if bdef.default:
			return bdef.default
		return 0


class Generator:
	bindings: Bindings

	def __init__(self, bindings: Bindings):
		self.bindings = bindings

	def generate(self):
		for config_path in iglob(os.path.join("templates", "*", "config.json")):
			template_name = os.path.basename(os.path.dirname(config_path))
			template_root = os.path.dirname(config_path)
			out_path = os.path.join("out", template_name)
			print(f"Processing '{template_root}' -> '{out_path}'")
			template = GeneratorTemplate(self.bindings, template_root, out_path)
			template.generate()


	# @classmethod
	# def __template_filter(cls, path: str):
	# 	return not any(re.search(pattern, path) for pattern in cls.TEMPLATE_SPECIAL_FILES)

