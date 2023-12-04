@{ if "wasi" in group.module: skip() }

-- DO NOT MODIFY, THIS FILE IS GENERATED --
-- VERSION @(bindings.version) --
---@@meta
@[ if group.description ]@
@( desc2comment(group.description, "-- ") )
@[ end if ]@

---@@class ProtoLogic
@[ for function in group ]@
@[ if function.hasPtrArg() ] @[ continue ] @[ end if ]@
@[ if function.description ]@
@( desc2comment(function.description, "--- ") )
@[ end if ]@
---@@field @(function.name) fun(@
@[ for i in range(len(function.args)) ]@
@{ arg = function.args[i] }@
@(", " if i > 0 else "")@(arg.name): @(retype(arg))@
@[ end for ]@
): @(retype(function.getResult(0)))
@[ end for ]@
protologic = nil
