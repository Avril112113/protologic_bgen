// DO NOT MODIFY, THIS FILE IS GENERATED //
// VERSION @(bindings.version) //


#pragma once

#include "_import.h"
@[ for struct in group.getUsedStructs() ]@
#include "@(struct.name).h"
@[ end for ]@


// @( group.name ).h
@[ if group.description ]@
@( desc2comment(group.description, "// ") )
@[ end if ]@


@[ for function in group ]@
@[ if function.description ]@
@( desc2comment(function.description, "// ") )
@[ end if ]@
@[ if function.deprecated ][[deprecated]] @[ end if ]@
WASM_IMPORT(@
"@(group.module)", @
"@(function.name)", @
@(function.name), @
@(retype(function.getResult(0)))@
@[ for arg in function.args ]@
, @(retype(arg))@("*" if not arg.count and not isinstance(arg.type, WasmType) else "") @(arg.name)@("[]" if arg.count else "")@
@[ end for ]@
);

@[ end for ]@
