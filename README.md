# BaseJumpSTL-cores

This is the core library of [BaseJump STL](https://github.com/bespoke-silicon-group/basejump_stl) to be used with [FuseSoC](https://github.com/olofk/fusesoc).

## Getting Started

### Installing FuseSoC
FuseSoC works on Linux, Windows, and macOS. It is written in Python and can be installed like any other Python package through "pip". Please refer to the full list of system requirements and installation instructions in the Installation section in the [User Guide](https://fusesoc.readthedocs.io/en/stable/user/installation.html).

### Quick Start for FuseSoC
To check if FuseSoC is working, and to get an initial feeling for how FuseSoC
works, you can try to simulate a simple hardware design from our core libray.

First, create and enter an empty workspace

    mkdir workspace
    cd workspace

Install the FuseSoc base library into the workspace

    fusesoc library add fusesoc-cores https://github.com/fusesoc/fusesoc-cores

Get a list of cores found in the workspace

    fusesoc core list

If you have any of the supported simulators installed, you can try to
run a simulation on one of the cores as well. For example,
`fusesoc run --target=sim i2c` will run a regression test on the core
i2c with Icarus Verilog. If you want to try another simulator instead,
add e.g. `--tool=modelsim` or `--tool=xcelium` between `run` and `i2c`.

`fusesoc --help` will give you more information on commands and switches.

## Working with BaseJumpSTL on FuseSoC

### Adding this core library to FuseSoC

    fusesoc library add basejump https://github.com/adithyasunil26/basejump_stl_cores

### Running cores
The cores currently have 2 targets which are verilator lint and testbench. They can be used as follows.

For linting

    fusesoc run --target lint bsg_dff

For verilator testbench

    fusesoc run --target verilator_tb bsg_dff

## Contributing

You are most welcome to add to this library of core files for BaseJump STL cores or update them if changes are made upstream in [BaseJump STL](https://github.com/bespoke-silicon-group/basejump_stl). Kindly refrain from trying to add core files for cores that are not a part of BaseJump STL. 
