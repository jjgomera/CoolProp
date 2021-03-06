.. _static_library:

**************
Static Library
**************

Static libraries can be used to compile all of CoolProp into one compilation unit, and then link that with user code.  This can be advantageous as CoolProp only needs to be compiled once and fast compilation of the user-defined code is then possible.

When writing your own C++ code, it is advised to compile CoolProp to a static library and then link CoolProp and your own code

Pre-compiled Binaries
=====================
Pre-compiled release binaries can be downloaded from :sfdownloads:`static_library`.  Development binaries coming from the buildbot server can be found at :bbbinaries:`static_library`.  These static libraries are only useful if the compiler used to make the static library agrees with the static library that will be used to build your other code.  So best to follow the below instructions to build your own static library.

User-Compiled Binaries
======================

Common Requirements
-------------------
Compilation of the static library requires a few :ref:`common wrapper pre-requisites <wrapper_common_prereqs>`

Compile
-------

You can build the static library using::

    # Check out the sources for CoolProp
    git clone https://github.com/CoolProp/CoolProp --recursive
    # Move into the folder you just created
    cd CoolProp
    # Make a build folder
    mkdir -p build && cd build
    # Build the makefile using CMake
    cmake .. -DCOOLPROP_STATIC_LIBRARY=ON
    # Make the static library
    make VERBOSE=1
