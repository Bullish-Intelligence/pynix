"""Generated: the packages of the package list. Do not edit."""

from builtins import str as _str

from .._pkgref import Pkg as _Pkg
from .._pkgref import Prog as _Prog

class PackageSet_llvmPackages:
    def __getitem__(self, attr: _str) -> _Pkg: ...
    bintools: _Pkg
    """System binary utilities (wrapper script)"""
    bintoolsNoLibc: _Pkg
    """System binary utilities (wrapper script)"""
    bolt: _Pkg
    """LLVM post-link optimizer"""
    clang: _Prog
    """C language family frontend for LLVM (wrapper script). Runs as `clang`."""
    clangNoCompilerRt: _Prog
    """C language family frontend for LLVM (wrapper script). Runs as `clang`."""
    clangNoCompilerRtWithLibc: _Prog
    """C language family frontend for LLVM (wrapper script). Runs as `clang`."""
    clangNoLibc: _Prog
    """C language family frontend for LLVM (wrapper script). Runs as `clang`."""
    clangNoLibcNoRt: _Prog
    """C language family frontend for LLVM (wrapper script). Runs as `clang`."""
    clangNoLibcWithBasicRt: _Prog
    """C language family frontend for LLVM (wrapper script). Runs as `clang`."""
    clangNoLibcxx: _Prog
    """C language family frontend for LLVM (wrapper script). Runs as `clang`."""
    clangUseLLVM: _Prog
    """C language family frontend for LLVM (wrapper script). Runs as `clang`."""
    clangWithLibcAndBasicRt: _Prog
    """C language family frontend for LLVM (wrapper script). Runs as `clang`."""
    clangWithLibcAndBasicRtAndLibcxx: _Prog
    """C language family frontend for LLVM (wrapper script). Runs as `clang`."""
    flang: _Prog
    """LLVM-based Fortran frontend (wrapper script). Runs as `flang`."""
    libc: _Pkg
    """Standard C library for LLVM"""
    libclang: _Prog
    """C language family frontend for LLVM. Runs as `clang`."""
    libcxx: _Pkg
    """C++ standard library"""
    libcxxClang: _Prog
    """C language family frontend for LLVM (wrapper script). Runs as `clang`."""
    libcxxStdenv: _Pkg
    """The default build environment for Unix packages in Nixpkgs"""
    libllvm: _Pkg
    """Collection of modular and reusable compiler and toolchain technologies"""
    libstdcxxClang: _Prog
    """C language family frontend for LLVM (wrapper script). Runs as `clang`."""
    libunwind: _Pkg
    """LLVM's unwinder library"""
    lld: _Pkg
    """LLVM linker (unwrapped)"""
    lldb: _Prog
    """Next-generation high-performance debugger. Runs as `lldb`."""
    llvm: _Pkg
    """Collection of modular and reusable compiler and toolchain technologies"""
    mlir: _Pkg
    """Multi-Level IR Compiler Framework"""
    openmp: _Pkg
    """Support for the OpenMP language"""
    stdenv: _Pkg
    """The default build environment for Unix packages in Nixpkgs"""
    systemLibcxxClang: _Prog
    """C language family frontend for LLVM (wrapper script). Runs as `clang`."""
    tblgen: _Pkg
    bintools_unwrapped: _Pkg
    clang_manpages: _Pkg
    """man page for Clang 21.1.8"""
    clang_tools: _Pkg
    """Standalone command line tools for C++ development"""
    clang_unwrapped: _Prog
    """C language family frontend for LLVM. Runs as `clang`."""
    compiler_rt: _Pkg
    """Compiler runtime libraries"""
    compiler_rt_libc: _Pkg
    """Compiler runtime libraries"""
    compiler_rt_no_libc: _Pkg
    """Compiler runtime libraries"""
    flang_rt: _Pkg
    """LLVM Fortran Runtime"""
    flang_unwrapped: _Prog
    """LLVM-based Fortran frontend. Runs as `flang`."""
    libc_full: _Pkg
    """Standard C library for LLVM"""
    libc_overlay: _Pkg
    """Standard C library for LLVM"""
    lldb_manpages: _Pkg
    """man pages for LLDB 21.1.8"""
    llvm_manpages: _Pkg
    """man pages for LLVM 21.1.8"""
