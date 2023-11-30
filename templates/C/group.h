// DO NOT MODIFY, THIS FILE IS GENERATED //


#pragma once

#include "_import.h"

{% for function in group %}
PL_IMPORT({{function.name}}, {{retype(function.result)}}{% for arg in function.args %}, {{retype(arg.type)}} {{arg.name}}{% endfor %});
{% endfor %}