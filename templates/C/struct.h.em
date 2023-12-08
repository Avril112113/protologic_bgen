// DO NOT MODIFY, THIS FILE IS GENERATED //
// VERSION @(bindings.version) //


#pragma once

#include "_import.h"


@[ if struct.description ]@
@( desc2comment(struct.description, "// ") )
@[ end if ]@
typedef struct @
@[ if struct.deprecated is not None ][[deprecated]] @[ end if ]@
_@(struct.name) {
@[ for field in struct ]@
	@(retype(field)) @(field.name);
@[ end for ]@
} @(struct.name);
