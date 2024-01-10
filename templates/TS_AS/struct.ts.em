// DO NOT MODIFY, THIS FILE IS GENERATED //
// VERSION @(bindings.version) //

@[ for depStruct in struct.getUsedStructs() ]@
import {@(depStruct.name)} from "./@(depStruct.name)";
@[ end for ]@

/**
@[ if struct.deprecated ]@
 * @@deprecated
@[ end if ]@
@[ if struct.description ]@
@( desc2comment(struct.description, " * ") )
@[ end if ]@
 */
export class @(struct.name) {
	static get DATA_SIZE(): i32 { return @(struct.byteCount); };

    protected _data: StaticArray<u8>;
	protected _offset: usize;

    constructor(_data: StaticArray<u8> = new StaticArray<u8>(@(struct.name).DATA_SIZE), _offset: usize = 0) {
        this._data = _data;
		this._offset = _offset;
    }

	get data(): StaticArray<u8> {
		return this._data;
	}

@	@[ for field in struct.fields.values() ]@
	get @(field.name)(): @(retype(field.type)) {
@	@	@[ if isinstance(field.type, WasmType) ]@
		return load<@(retype(field.type))>(changetype<usize>(this._data) + this._offset, @(field.offset));
@	@	@[ else ]@
		return new @(retype(field.type))(this._data, @(field.offset));
@	@	@[ end if ]@
	}

@	@[ end for ]@
}
