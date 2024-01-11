// DO NOT MODIFY, THIS FILE IS GENERATED //
// VERSION @(bindings.version) //

import {@(struct.name)} from "./@(struct.name)";
import {@(quickstate.init_function.name)} from "./@(quickstate.init_function_group.name)";
@[ for depStruct in struct.getUsedStructs() ]@
import {@(depStruct.name)} from "./@(depStruct.name)";
@[ end for ]@


let _data: @(struct.name) = new @(struct.name)();

// Used by sched_yield() to make things happy... It was angry for some reason...
export function __internal_init_@(struct.name)(): void {
	@(quickstate.init_function.name)(_data, @(struct.name).DATA_SIZE);
}
__internal_init_@(struct.name)();

export class @(quickstate.name) {
@	@[ for field in struct.fields.values() ]@
	static get @(field.name)(): @(retype(field.type)) {
		return _data.@(field.name);
	}

@	@[ end for ]@
}
