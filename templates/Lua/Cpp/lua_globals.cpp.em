// DO NOT MODIFY, THIS FILE IS GENERATED //
// VERSION @(bindings.version) //

// Generated lua library utilising the generated C bindings.
// This NOT ready-made, is to be copy-pasted.

#include "lua_globals.hpp"

#include "protologic/protologic.hpp"


void lua_protologic_set_globals(lua_State* state) {
@[ for function in bindings["constants"] ]@
@[ if function.deprecated is not None ]@[ continue ]@[ end if ]@
@[ if len(function.results) != 1 ] @[ continue ] @[ end if ]@
	@(retype(function.results[0], "WasmType_c_lua"))(state, @(function.name)());
	lua_setglobal(state, "@(function.name.replace('const_get_', '').upper())");

@[ end for ]@
}