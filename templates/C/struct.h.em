// DO NOT MODIFY, THIS FILE IS GENERATED //
// VERSION @(bindings.version) //


#pragma once

#include <string.h>
#include <stdint.h>
@[ for depStruct in struct.getUsedStructs() ]@
#include "@(depStruct.name).h"
@[ end for ]@


// @( struct.name ).h
@[ if struct.description ]@
@( desc2comment(struct.description, "// ") )
@[ end if ]@

#define @(struct.name)_SIZE @(struct.byteCount)
typedef volatile uint8_t @(struct.name);

@[ for field in struct.fields.values() ]@
@[ if isinstance(field.type, WasmType) ]@
inline void @(struct.name)_get_@(field.name)(@(struct.name)* ptr, @(retype(field.type))* dest) {
	memcpy(dest, ((uint8_t*)ptr) + @(field.offset), sizeof(@(retype(field.type))));
}
inline @(retype(field.type)) @(struct.name)_get_@(field.name)_ret(@(struct.name)* ptr) {
	@(retype(field.type)) tmp;
	@(struct.name)_get_@(field.name)(ptr, &tmp);
	return tmp;
}
@[ else ]@
inline @(retype(field.type))* @(struct.name)_get_@(field.name)(@(struct.name)* ptr) {
	return (@(retype(field.type))*)(ptr + @(field.offset));
}
@[ end if ]@

@[ end for ]@
