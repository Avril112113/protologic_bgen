// DO NOT MODIFY, THIS FILE IS GENERATED //


#[link(wasm_import_module = "protologic")]
extern
{
    {% for function in group %}
    pub fn {{function.name}}({% for i in range(len(function.args)) %}{% set arg=function.args[i] %}{{", " if i > 0 else ""}}{{arg.name}}: {{retype(arg)}}{% endfor %}){{" -> "+retype(function.getResult(0)) if function.getResult(0) else ""}};
    {% endfor %}
}