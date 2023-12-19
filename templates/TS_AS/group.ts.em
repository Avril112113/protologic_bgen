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
// @@ts-ignore
@@external("@(group.module)", "@(function.name)")
declare function _internal_@(function.name)(@
@[ for i in range(len(function.args)) ]@
@{ arg = function.args[i] }@
@(", " if i > 0 else "")@(arg.name): @(retype(arg))@
@[ end for ]@
): @(retype(function.getResult(0)));

/**
@[ if function.deprecated is not None ]@
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
@	@(", " if i > 0 else "")@(arg.name)@
@	@[ end for ]@
@	);
}

@[ end for ]@
