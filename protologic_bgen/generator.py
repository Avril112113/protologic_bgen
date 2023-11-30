from typing import TypedDict
from jinja2 import Environment, FileSystemLoader
from glob import iglob
import os.path
import json
import sys
import re

from .wasm_type import WasmType
from .bindings import Bindings


class _TemplateConfig(TypedDict):
	WasmType: dict[str, str]


class Generator:
	TEMPLATE_SPECIAL_FILES = [r"config\.json", r"group\..*"]

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

			common_args = {
				"bindings": self.bindings,
				"config": config,
				"retype": self.__template_retype(config)
			}

			# Process group file
			group_templates = env.list_templates(filter_func=lambda path: re.search(r"group\..*", path) is not None)
			if len(group_templates) <= 0:
				print(f"Missing group file for {os.path.dirname(config_path)}", file=sys.stderr)
			elif len(group_templates) > 1:
				print(f"Multiple group files for {os.path.dirname(config_path)}", file=sys.stderr)
			group_template = env.get_template(group_templates[0])
			for group in self.bindings:
				group_result = group_template.render(**common_args, group=group)
				group_out_path = os.path.join(out_path, group_template.name.replace("group", group.name))
				if not os.path.isdir(os.path.dirname(group_out_path)):
					os.makedirs(os.path.dirname(group_out_path))
				with open(group_out_path, "w") as f:
					f.write(group_result)

			# Process all non-special files
			files = env.list_templates(filter_func=self.__template_filter)
			for file in files:
				template = env.get_template(file)
				result = template.render(**common_args)
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
		def retype(wasm_type: WasmType|str|None):
			if wasm_type is None:
				return config["WasmType"].get("NONE", "")
			if isinstance(wasm_type, WasmType):
				wasm_type = wasm_type.name
			return config["WasmType"].get(wasm_type)
		return retype
