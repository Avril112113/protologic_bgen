// DO NOT MODIFY, THIS FILE IS GENERATED //
// VERSION {{bindings.version}} //


#pragma once

#include "_import.h"

{% if struct.description %}
{{desc2comment(struct.description, "// ")}}

{% endif -%}

{% if struct.description %}{{desc2comment(struct.description, "// ")}}
{% endif -%}
typedef struct _{{struct.name}} {
	{%- for field in struct %}
	{{ retype(field) }} {{ field.name }};
	{%- endfor %}
} {{struct.name}};
