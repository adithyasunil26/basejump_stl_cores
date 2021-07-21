# BaseJumpSTL-cores

This is the core library of [BaseJump STL](https://github.com/bespoke-silicon-group/basejump_stl) to be used with [FuseSoC](https://github.com/olofk/fusesoc).

Visit [FuseSoC](https://github.com/olofk/fusesoc) for install isntructions for FuseSoC.

### Adding core library to FuseSoC
```bash
fusesoc library add alu https://github.com/adithyasunil26/basejump_stl_cores
```

### Running cores
The cores currently have 2 targets which are verilator lint and testbench. They can be used as follows.

For linting
```bash
fusesoc run --target lint <name_of_core>
```

For verilator testbench
```bash
fusesoc run --target verilator_tb <name_of_core>
```