// DO NOT MODIFY, THIS FILE IS GENERATED //
// VERSION {{bindings.version}} //

// Generated lua library utilising the generated C bindings.
// This NOT ready-made, is to be copy-pasted.


{% for function in bindings["constants"] if len(function.results) == 1 %}
{{retype(function.results[0], "WasmType_c_lua")}}(state, {{function.name}}());
lua_setglobal(state, "{{function.name.replace('const_get_', '').upper()}}");
{% endfor %}