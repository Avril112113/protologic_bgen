@{ if "wasi" in group.module: skip() }@
@
-- DO NOT MODIFY, THIS FILE IS GENERATED --
-- VERSION @(bindings.version) --
---@@meta
@[ if group.description ]@
@( desc2comment(group.description, "-- ") )
@[ end if ]@

---@@class ProtoLogic
@[ for function in group ]@
@[ if function.hasPtrArg() and len(function.args) > 1 ]@[ continue ]@[ end if ]@
@[ if function.description ]@
@( desc2comment(function.description, "--- ") )
@[ end if ]@
---@@field @(function.name) fun(@
@{ simpleArgs = list(filter(lambda arg: arg.ptr is None, function.args)) }@
@[ for i in range(len(simpleArgs)) ]@
@{ arg = simpleArgs[i] }@
@(", " if i > 0 else "")@(arg.name): @(retype(arg))@
@[ end for ]@
@{ ptrArgs = filter(lambda arg: arg.ptr is not None, function.args) }@
@{ ptrReturns = [v for t in map(lambda arg: (*arg.ptr.fields.values(),) if arg.ptr.name in config.get("struct_as_multi_return") else (arg.ptr,), ptrArgs) for v in t] }@
@{ returns = [*ptrReturns, *function.results] }@
): @
@[ for i in range(len(returns)) ]@
@{ ret = returns[i] }@
@(", " if i > 0 else "")@(retype(ret))@
@[ end for ]@
@[ if len(returns) <= 0 ]nil@[ end if ]@

@[ end for ]@
protologic = nil
