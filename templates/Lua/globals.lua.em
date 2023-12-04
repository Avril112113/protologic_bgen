-- DO NOT MODIFY, THIS FILE IS GENERATED --
-- VERSION @(bindings.version) --
---@@meta

-- Consts set by Cpp/constants_vars.cpp


@[ for function in bindings["constants"] ]@
@[ if len(function.results) != 1 ] @[ continue ] @[ end if ]@
---@@type @(retype(function.results[0]))
@(function.name.replace('const_get_', '').upper()) = nil

@[ end for ]@
