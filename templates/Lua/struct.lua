{%- if struct.name in config["struct_as_multi_return"] -%} {{ skip() }} {%- endif -%}

-- DO NOT MODIFY, THIS FILE IS GENERATED --
-- VERSION {{bindings.version}} --
---@meta
{% if struct.description -%}
{{ desc2comment(struct.description, "--- ") }}
{% endif %}

---@class protologic.{{ struct.name }}
{%- for field in struct %}
---@field {{ field.name }} {{ retype(field) }}
{%- endfor %}
