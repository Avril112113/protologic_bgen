// DO NOT MODIFY, THIS FILE IS GENERATED //
// VERSION {{bindings.version}} //

{% if struct.description %}
{{ desc2comment(struct.description, "/// ") }}
{% endif -%}
#[repr(C)]
pub struct {{ struct.name }}
{
	{%- for field in struct %}
    pub {{ field.name }}: {{ retype(field) }},
    {%- endfor %}
}
impl {{ struct.name }}
{
    pub(crate) fn default() -> {{ struct.name }}
    {
        return {{ struct.name }} {
			{%- for field in struct %}
			{{ field.name }}: {{ getdefault(field) }},
			{%- endfor %}
        };
    }
}