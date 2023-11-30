// DO NOT MODIFY, THIS FILE IS GENERATED //


#pragma once

#include "_import.h"

{% for function in group %}
PL_IMPORT({{function.name}}, {{retype(function.getResult(0))}}{% for arg in function.args %}, {{retype(arg)}} {{arg.name}}{% endfor %});
{% endfor %}