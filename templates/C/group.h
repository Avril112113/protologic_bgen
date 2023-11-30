// DO NOT MODIFY, THIS FILE IS GENERATED //
// VERSION {{bindings.version}} //


#pragma once

#include "_import.h"

{% if group.description %}
{{desc2comment(group.description, "// ")}}

{% endif -%}

{% for function in group %}
{% if function.description %}{{desc2comment(function.description, "// ")}}
{% endif -%}
PL_IMPORT({{function.name}}, {{retype(function.getResult(0))}}{% for arg in function.args %}, {{retype(arg)}} {{arg.name}}{% endfor %});
{% endfor %}