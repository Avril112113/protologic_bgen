# ProtoLogic BGen
Un-official protologic bindings generator.

### Supports
~~Rust - [Protologic/Protologic.rs](https://github.com/Protologic/Protologic.rs)~~ (Not used by this repo yet?)  
C/C++ - [Avril112113/protologic-tool-c_cpp](https://github.com/Avril112113/protologic-tool-c_cpp)  
AssemblyScript - [Avril112113/protologic-tool-assemblyscript](https://github.com/Avril112113/protologic-tool-assemblyscript)  
Lua - [Avril112113/protologic-lua](https://github.com/Avril112113/protologic-lua)  

### Updating the bindings
Currently, `protologic_bindings.json` is manually managed.  
Once `protologic_bindings.json` is updated, run `python main.py` with Python 3.10.  
Bindings in `./out` will be updated.  


## TODO
Support indexed QuickState field types, to allow for, eg `gun_bearing(2)`.  
Re-add Lua bindings.  
Create QuickJS bindings.  
Create Python bindings.  
Generate WIT file.  
Create C# bindings.  


## Credits
[martindevans](https://github.com/martindevans) - Creator of ProtoLogic  
[Avril112113](https://github.com/Avril112113) - Creator of ProtoLogic BGen (This repo)  
[Solon](https://github.com/1solon) - Initial work on AssemblyScript bindings.  
