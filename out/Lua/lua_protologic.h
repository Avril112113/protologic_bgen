#pragma once

#ifdef __cplusplus
extern "C" {
#endif


#include "lua.h"
#include "lualib.h"
#include "lauxlib.h"

int luaopen_protologic(lua_State *state);


#ifdef __cplusplus
}
#endif