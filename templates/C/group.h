// DO NOT MODIFY, THIS FILE IS GENERATED //
// VERSION {{bindings.version}} //


#pragma once

#include "_import.h"

{%- for struct in group.getUsedStructs() %}
#include "{{struct.name}}.h"
{%- endfor %}

{% if group.description %}
{{ desc2comment(group.description, "// ") }}

{% endif -%}

{% for function in group %}
{% if function.description %}{{ desc2comment(function.description, "// ") }}
{% endif -%}
WASM_IMPORT("{{ group.module }}", "{{ function.name }}", {{ function.name }}, {{ retype(function.getResult(0)) }}{% for arg in function.args %}, {{ retype(arg) }}{{ arg.ifPtr("*") }} {{ arg.name }}{% endfor %});
{% endfor %}