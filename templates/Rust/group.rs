// DO NOT MODIFY, THIS FILE IS GENERATED //
// VERSION {{bindings.version}} //

{%- for struct in group.getUsedStructs() %}
mod {{ struct.name }};
{%- endfor %}

{% if group.description %}
{{ desc2comment(group.description, "/// ") }}
{% endif -%}

#[link(wasm_import_module = "{{ group.module }}")]
extern
{
	{%- for function in group %}
	{% if function.description %}{{ desc2comment(function.description, "/// ") }}
	{% endif -%}
	pub fn {{ function.name }}({% for i in range(len(function.args)) %}{% set arg=function.args[i] %}{{ ", " if i > 0 else "" }}{{ arg.name }}: {{ arg.ifPtr("*mut ") }}{{ retype(arg) }}{% endfor %}){{ " -> "+function.getResult(0).ifPtr("*mut ")+retype(function.getResult(0)) if function.getResult(0) else "" }};{{"\n"}}
	{%- endfor %}
}