// DO NOT MODIFY, THIS FILE IS GENERATED //
// VERSION @(bindings.version) //


#pragma once

#include <string.h>
#include <stdint.h>
#include <stdlib.h>
#include "@(struct.name).h"
#include "@(quickstate.init_function_group.name).h"
@[ for depStruct in struct.getUsedStructs() ]@
#include "@(depStruct.name).h"
@[ end for ]@


// @( quickstate.name ).h

static @(struct.name)* __@(quickstate.name) = (@(struct.name)*)malloc(@(struct.name)_SIZE);
static bool __@(quickstate.name)_has_init = false;

@[ for field in struct.fields.values() ]@
@[ if isinstance(field.type, WasmType) ]@
inline @(retype(field.type)) @(quickstate.name)_get_@(field.name)() {
	if (!__@(quickstate.name)_has_init) {
		@(quickstate.init_function.name)(__@(quickstate.name), @(struct.name)_SIZE);
		__@(quickstate.name)_has_init = true;
	}
	@(retype(field.type)) tmp;
	@(struct.name)_get_@(field.name)(__@(quickstate.name), &tmp);
	return tmp;
}
@[ else ]@
inline @(retype(field.type))* @(quickstate.name)_get_@(field.name)() {
	if (!__@(quickstate.name)_has_init) {
		@(quickstate.init_function.name)(__@(quickstate.name), @(struct.name)_SIZE);
		__@(quickstate.name)_has_init = true;
	}
	return (@(retype(field.type))*)(__@(quickstate.name) + @(field.offset));
}
@[ end if ]@

@[ end for ]@
