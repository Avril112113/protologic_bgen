// DO NOT MODIFY, THIS FILE IS GENERATED //
// VERSION {{bindings.version}} //

// Generated lua library utilising the generated C bindings.

#include "lua_protologic.h"

#include "protologic/protologic.h"


{% for group in bindings %}
// {{ group.name }} //
{% for function in group %}
static int lua_protologiclib_{{function.name}}(lua_State* state) {
	{%- for i in range(len(function.args)) %}{% set arg=function.args[i] %}
	{{retype(arg, "WasmType_c")}} arg_{{arg.name}} = {{retype(arg, "WasmType_lua_c")}}(state, {{i+1}});
	{%- endfor %}
	{% if len(function.results) > 0 -%}{{retype(function.getResult(0), "WasmType_c")}} result = {% endif -%}
	{{function.name}}({%- for i in range(len(function.args)) %}{% set arg=function.args[i] %}{{", " if i != 0 else ""}}arg_{{arg.name}}{%- endfor %});
	{% if len(function.results) > 0 -%}{{retype(function.getResult(0), "WasmType_c_lua")}}(state, result);{%- endif %}
	return {{1 if len(function.results) > 0 else 0}};
}
{% endfor %}

{% endfor %}


static const struct luaL_Reg lua_protologiclib [] = {
{% for group in bindings %}
	// {{ group.name }} //
{% for function in group %}
	{"{{function.name}}", lua_protologiclib_{{function.name}}},
{% endfor %}
{% endfor %}
	{NULL, NULL}  /* sentinel */
};


int luaopen_protologic(lua_State *state) {
	lua_newtable(state);
	luaL_setfuncs(state, lua_protologiclib, 0);
	return 1;
}