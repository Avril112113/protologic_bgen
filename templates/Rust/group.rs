// DO NOT MODIFY, THIS FILE IS GENERATED //


#[link(wasm_import_module = "protologic")]
extern
{
    {% for function in group %}
    pub fn {{function.name}}({% for i in range(len(function.args)) %}{% set arg=function.args[i] %}{{", " if i > 0 else ""}}{{arg.name}}: {{retype(arg.type)}}{% endfor %}){{" -> "+retype(function.result) if function.result else ""}};
    {% endfor %}
}