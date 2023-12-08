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
@[ if function.deprecated is not None ][[deprecated]] @[ end if ]@
WASM_IMPORT(@
"@(group.module)", @
"@(function.name)", @
@(function.name), @
@(retype(function.getResult(0)))@
@[ for arg in function.args ]@
, @(retype(arg))@(arg.ifPtr("*")) @(arg.name)@
@[ end for ]@
);

@[ end for ]@
