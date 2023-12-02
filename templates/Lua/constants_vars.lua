-- DO NOT MODIFY, THIS FILE IS GENERATED --
-- VERSION {{bindings.version}} --
---@meta

-- Provided by Cpp/lua_consts.cpp

{% for function in bindings["constants"] if len(function.results) == 1 %}
---@type {{retype(function.results[0])}}
{{function.name.replace('const_get_', '').upper()}} = nil
{% endfor %}
