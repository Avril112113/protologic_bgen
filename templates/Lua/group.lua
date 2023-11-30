-- DO NOT MODIFY, THIS FILE IS GENERATED --
---@meta


---@class ProtoLogic
{%- for function in group %}
---@field {{function.name}} fun({% for i in range(len(function.args)) %}{% set arg=function.args[i] %}{{", " if i > 0 else ""}}{{arg.name}}: {{retype(arg)}}{% endfor %}): {{retype(function.getResult(0))}}
{%- endfor %}
protologic = nil
