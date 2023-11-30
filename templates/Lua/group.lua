-- DO NOT MODIFY, THIS FILE IS GENERATED --
-- VERSION {{bindings.version}} --
---@meta
{% if group.description -%}
{{desc2comment(group.description, "--- ")}}
{% endif %}

---@class ProtoLogic
{%- for function in group %}
{% if function.description -%} {{desc2comment(function.description, "--- ")}} {% endif -%}
---@field {{function.name}} fun({% for i in range(len(function.args)) %}{% set arg=function.args[i] %}{{", " if i > 0 else ""}}{{arg.name}}: {{retype(arg)}}{% endfor %}): {{retype(function.getResult(0))}}
{%- endfor %}
protologic = nil
