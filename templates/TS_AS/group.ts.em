// DO NOT MODIFY, THIS FILE IS GENERATED //
// VERSION @(bindings.version) //

@# TODO: Deal with duplicate includes due to same struct used in differenat groups
@[ for struct in group.getUsedStructs() ]@
import {@(struct.name)} from "./@(struct.name)";
@[ end for ]@


// @( group.name ).ts
@[ if group.description ]@
@( desc2comment(group.description, "// ") )
@[ end if ]@


@[ for function in group ]@
@[ if function.hasCountArg ]@[ continue ]@[ end if ]@
// @@ts-ignore
@@external("@(group.module)", "@(function.name)")
declare function _internal_@(function.name)(@
@[ for i in range(len(function.args)) ]@
@{ arg = function.args[i] }@
@(", " if i > 0 else "")@
@(arg.name): @
@[ if isinstance(arg.type, WasmType) ]@
@(retype(arg.type))@
@[ else ]@
StaticArray<u8>@
@[ end if ]@
@[ end for ]@
): @(retype(function.getResult(0)));

/**
@[ if function.deprecated ]@
 * @@deprecated
@[ end if ]@
@[ if function.description ]@
@( desc2comment(function.description, " * ") )
@[ end if ]@
 */
export function @(function.name)(@
@[ for i in range(len(function.args)) ]@
@{ arg = function.args[i] }@
@(", " if i > 0 else "")@(arg.name): @(retype(arg))@
@[ end for ]@
): @(retype(function.getResult(0))) {
	return _internal_@(function.name)(@
@	@[ for i in range(len(function.args)) ]@
@	@{ arg = function.args[i] }@
@	@(", " if i > 0 else "")@
@	@(arg.name)@
@	@[ if not isinstance(arg.type, WasmType) ]@
@	.data@
@	@[ end if ]@
@	@[ end for ]@
@	);
}

@[ end for ]@
