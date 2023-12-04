// DO NOT MODIFY, THIS FILE IS GENERATED //
// VERSION @(bindings.version) //

// Generated lua library utilising the generated C bindings.

#include "lua_protologic.hpp"

#include "protologic/protologic.hpp"


@[ for group in bindings ]@
@[ if "wasi" in group.module ]@[ continue ]@[ end if ]@
// @(group.name) //

@[ for function in group ]@
@[ if function.hasPtrArg() ]@[ continue ]@[ end if ]@
static int lua_protologiclib_@(function.name)(lua_State* state) {
@[ for i in range(len(function.args)) ]@
@{ arg = function.args[i] }@
	@(retype(arg, "WasmType_c")) arg_@(arg.name) = @(retype(arg, "WasmType_lua_c"))(state, @(i+1));
@[ end for ]@
	@[ if len(function.results) > 0 ]@
@	@(retype(function.getResult(0), "WasmType_c")) result = @
@	@[ end if ]@
@(function.name)(@
@[ for i in range(len(function.args)) ]@
@{ arg = function.args[i] }@
@(", " if i != 0 else "")arg_@(arg.name)@
@[ end for ]@
);
@[ if len(function.results) > 0 ]@
	@(retype(function.getResult(0), "WasmType_c_lua"))(state, result);
@[ end if ]@
	return @(1 if len(function.results) > 0 else 0);
}

@[ end for ]@
@[ end for ]@



static const struct luaL_Reg lua_protologiclib [] = {
@[ for group in bindings ]@
@[ if "wasi" in group.module ] @[ continue ] @[ end if ]@
	// {{ group.name }} //
@[ for function in group ]@
@[ if function.hasPtrArg() ] @[ continue ] @[ end if ]@
	{"@(function.name)", lua_protologiclib_@(function.name)},
@[ end for ]@
@[ end for ]@
	/* sentinel */
	{NULL, NULL}
};


int luaopen_protologic(lua_State *state) {
	lua_newtable(state);
	luaL_setfuncs(state, lua_protologiclib, 0);
	return 1;
}