// DO NOT MODIFY, THIS FILE IS GENERATED //
// VERSION @(bindings.version) //

// Generated lua library utilising the generated C bindings.

#include "lua_protologic.hpp"

#include "protologic/protologic.hpp"
@[ for group in bindings ]@
@# TODO: Deal with duplicate includes due to same struct used in differenat groups
@[ for struct in group.getUsedStructs() ]@
#include "protologic/@(struct.name).h"
@[ end for ]@
@[ end for ]@


@[ for group in bindings ]@
@[ if "wasi" in group.module ]@[ continue ]@[ end if ]@
// @(group.name) //

@[ for function in group ]@
@[ if function.hasPtrArg() and len(function.args) > 1 ]@[ continue ]@[ end if ]@
static int lua_protologiclib_@(function.name)(lua_State* state) {
@[ for i in range(len(function.args)) ]@
@{ arg = function.args[i] }@
@	@[ if arg.ptr is None ]@
	@(retype(arg, "WasmType_c")) arg_@(arg.name) = @(retype(arg, "WasmType_lua_c"))(state, @(i+1));
@	@[ else ]@
	@(retype(arg, "WasmType_c"))* arg_@(arg.name) = new @((retype(arg, "WasmType_c")))();
@	@[ end if ]@
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
@{ ptrArgs = filter(lambda arg: arg.ptr is not None, function.args) }@
@{ ptrReturns = list(map(lambda arg: (arg.name, (*arg.ptr.fields.values(),)) if arg.ptr.name in config.get("struct_as_multi_return") else (arg.name, (arg.ptr,)), ptrArgs)) }@
@[ for argName, ptrRets in ptrReturns ]@
@[ for ptrRet in ptrRets ]@
	@(retype(ptrRet, "WasmType_c_lua"))(state, arg_@(argName)->@(ptrRet.name));
@[ end for ]@
	delete arg_@(argName);
@[ end for ]@
@[ if len(function.results) > 0 ]@
	@(retype(function.getResult(0), "WasmType_c_lua"))(state, result);
@[ end if ]@
	return @(sum(len(ptrRets) for argName, ptrRets in ptrReturns) + min(len(function.results), 1));
}

@[ end for ]@
@[ end for ]@



static const struct luaL_Reg lua_protologiclib [] = {
@[ for group in bindings ]@
@[ if "wasi" in group.module ] @[ continue ] @[ end if ]@
	// {{ group.name }} //
@[ for function in group ]@
@[ if function.hasPtrArg() and len(function.args) > 1 ]@[ continue ]@[ end if ]@
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