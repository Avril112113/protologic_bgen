// DO NOT MODIFY, THIS FILE IS GENERATED //
// VERSION @(bindings.version) //

/**
@[ if struct.deprecated is not None ]@
 * @@deprecated
@[ end if ]@
@[ if struct.description ]@
@( desc2comment(struct.description, " * ") )
@[ end if ]@
 */
export class @(struct.name) {
@	@[ for field in struct ]@
	@(field.name): @(retype(field)) = @(getDefault(field));
@	@[ end for ]@
};
