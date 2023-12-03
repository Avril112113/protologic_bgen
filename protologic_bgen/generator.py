from typing import TypedDict
from jinja2 import Environment, FileSystemLoader
from glob import iglob
import os.path
import json
import sys
import re

from .wasm_type import WasmType
from .bindings import Bindings, BindingsDef, BindingsStruct


class _TemplateConfig(TypedDict):
	WasmType: dict[str, str]


class Generator:
	TEMPLATE_SPECIAL_FILES = [r"config\.json", r"struct\..*", r"group\..*"]

	bindings: Bindings

	def __init__(self, bindings: Bindings):
		self.bindings = bindings

	def generate(self):
		for config_path in iglob("templates/*/config.json"):
			template_name = os.path.basename(os.path.dirname(config_path))
			template_root = f"./templates/{template_name}"
			out_path = f"./out/{template_name}"

			print(f"Processing '{template_root}' -> '{out_path}'")
			with open(config_path) as f:
				config: _TemplateConfig = json.loads(f.read())
			env = Environment(
				loader=FileSystemLoader(template_root),
				autoescape=False
			)
			env.globals["warn"] = lambda msg: print(f"{template_name} WARN: {msg}", file=sys.stderr)
			env.globals["print"] = print
			env.globals["len"] = len

			_skip = False

			def setSkip():
				nonlocal _skip
				_skip = True

			common_args = {
				"bindings": self.bindings,
				"config": config,
				"retype": self.__template_retype(config),
				"getdefault": self.__template_getdefault(config),
				"desc2comment": self.__template_desc2comment,
				"skip": setSkip
			}

			# Process struct file
			struct_templates = env.list_templates(filter_func=lambda path: re.search(r"struct\..*", path) is not None)
			if len(struct_templates) <= 0:
				print(f"Missing struct file for {template_root}")
			elif len(struct_templates) > 1:
				print(f"Multiple struct files for {template_root}")
			else:
				struct_template = env.get_template(struct_templates[0])
				for struct in self.bindings.structs.values():
					_skip = False
					struct_result = struct_template.render(**common_args, struct=struct)
					if not _skip:
						struct_out_path = os.path.join(out_path, struct_template.name.replace("struct", struct.name))
						if not os.path.isdir(os.path.dirname(struct_out_path)):
							os.makedirs(os.path.dirname(struct_out_path))
						with open(struct_out_path, "w") as f:
							f.write(struct_result)

			# Process group file
			group_templates = env.list_templates(filter_func=lambda path: re.search(r"group\..*", path) is not None)
			if len(group_templates) <= 0:
				print(f"Missing group file for '{template_root}'")
			elif len(group_templates) > 1:
				print(f"Multiple group files for '{template_root}'")
			else:
				group_template = env.get_template(group_templates[0])
				for group in self.bindings.groups.values():
					_skip = False
					group_result = group_template.render(**common_args, group=group)
					if not _skip:
						group_out_path = os.path.join(out_path, group_template.name.replace("group", group.name))
						if not os.path.isdir(os.path.dirname(group_out_path)):
							os.makedirs(os.path.dirname(group_out_path))
						with open(group_out_path, "w") as f:
							f.write(group_result)

			# Process all non-special files
			files = env.list_templates(filter_func=self.__template_filter)
			for file in files:
				template = env.get_template(file)
				_skip = False
				result = template.render(**common_args)
				if not _skip:
					file_out_path = os.path.join(out_path, file)
					if not os.path.isdir(os.path.dirname(file_out_path)):
						os.makedirs(os.path.dirname(file_out_path))
					with open(file_out_path, "w") as f:
						f.write(result)

	@classmethod
	def __template_filter(cls, path: str):
		return not any(re.search(pattern, path) for pattern in cls.TEMPLATE_SPECIAL_FILES)

	@classmethod
	def __template_retype(cls, config: _TemplateConfig):
		# noinspection PyTypedDict
		# Support `retype_structs` from config
		def retype(bdef: BindingsDef | WasmType | str | None, config_entry="WasmType", struct=True):
			if bdef is None:
				return config[config_entry].get("NONE", "")
			if isinstance(bdef, WasmType):
				bdef = bdef.name
			elif isinstance(bdef, BindingsDef):
				if struct and bdef.ptr is not None:
					return bdef.ptr.name
				bdef = bdef.type.name
			elif isinstance(bdef, BindingsStruct):
				return bdef.name
			return config[config_entry].get(bdef)
		return retype

	@classmethod
	def __template_getdefault(cls, config: _TemplateConfig):
		def getdefault(bdef: BindingsDef):
			if bdef.default:
				return bdef.default
			return 0
		return getdefault

	@classmethod
	def __template_desc2comment(cls, description: str, comment: str):
		if description is None:
			return comment
		return comment + description.strip().replace("\n", f"\n{comment}")
