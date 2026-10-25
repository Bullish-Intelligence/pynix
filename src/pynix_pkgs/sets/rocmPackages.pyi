"""Generated: the packages of the package list. Do not edit."""

from builtins import str as _str

from .._pkgref import Pkg as _Pkg
from .._pkgref import Prog as _Prog

class PackageSet_rocmPackages:
    def __getitem__(self, attr: _str) -> _Pkg: ...
    amdsmi: _Prog
    """System management interface for AMD GPUs supported by ROCm. Runs as `amd-smi`."""
    aotriton: _Pkg
    """ROCm Ahead of Time (AOT) Triton Math Library"""
    aqlprofile: _Pkg
    """AQLPROFILE library for AMD HSA runtime API extension support"""
    ck4inductor: _Pkg
    """Pytorch inductor backend which uses composable_kernel universal GEMM implementations"""
    clang: _Pkg
    clr: _Pkg
    """AMD Common Language Runtime for hipamd, opencl, and rocclr"""
    composable_kernel: _Pkg
    """Performance portable programming model for machine learning tensor operators"""
    composable_kernel_base: _Pkg
    """Performance portable programming model for machine learning tensor operators"""
    half: _Pkg
    """C++ library for half precision floating point arithmetics"""
    hipblas: _Pkg
    """ROCm BLAS marshalling library"""
    hipblaslt: _Pkg
    """Library that provides general matrix-matrix operations with a flexible API"""
    hipcc: _Pkg
    """Compiler driver utility that calls clang or nvcc"""
    hipcub: _Pkg
    """Thin wrapper library on top of rocPRIM or CUB"""
    hipfft: _Pkg
    """FFT marshalling library"""
    hipfort: _Prog
    """Fortran interfaces for ROCm libraries. Runs as `hipfc`."""
    hipify: _Pkg
    """Convert CUDA to Portable C++ Code"""
    hiprand: _Pkg
    """HIP wrapper for rocRAND and cuRAND"""
    hiprt: _Pkg
    """Ray tracing library for HIP"""
    hipsolver: _Pkg
    """ROCm SOLVER marshalling library"""
    hipsparse: _Pkg
    """ROCm SPARSE marshalling library"""
    hipsparselt: _Pkg
    """ROCm hipSPARSELt - a SPARSE marshalling library"""
    hsakmt: _Pkg
    """Platform runtime for ROCm"""
    migraphx: _Pkg
    """AMD's graph optimization engine"""
    miopen: _Pkg
    """Machine intelligence library for ROCm"""
    mivisionx: _Pkg
    """Set of comprehensive computer vision and machine intelligence libraries, utilities, and applications"""
    mpi: _Pkg
    """Open source MPI-3 implementation"""
    mscclpp: _Pkg
    openmp: _Pkg
    """Support for the OpenMP language"""
    openmpi: _Pkg
    """Open source MPI-3 implementation"""
    rccl: _Pkg
    """ROCm communication collectives library"""
    rdc: _Pkg
    """Simplifies administration and addresses infrastructure challenges in cluster and datacenter environments"""
    rocalution: _Pkg
    """Iterative sparse solvers for ROCm"""
    rocblas: _Pkg
    """BLAS implementation for ROCm platform"""
    rocdbgapi: _Pkg
    """Debugger support for control of execution and inspection state of AMD's GPU architectures"""
    rocfft: _Pkg
    """FFT implementation for ROCm"""
    rocgdb: _Pkg
    """ROCm source-level debugger for Linux, based on GDB"""
    rocmClangStdenv: _Pkg
    """The default build environment for Unix packages in Nixpkgs"""
    rocminfo: _Prog
    """ROCm Application for Reporting System Info. Runs as `rocminfo`."""
    rocmlir: _Pkg
    """MLIR-based convolution and GEMM kernel generator"""
    rocprim: _Pkg
    """ROCm parallel primitives"""
    rocprofiler: _Pkg
    """Profiling with perf-counters and derived metrics"""
    rocrand: _Pkg
    """Generate pseudo-random and quasi-random numbers"""
    rocshmem: _Pkg
    """The ROCm OpenSHMEM (rocSHMEM) runtime"""
    rocsolver: _Pkg
    """ROCm LAPACK implementation"""
    rocsparse: _Pkg
    """ROCm SPARSE implementation"""
    rocthrust: _Pkg
    """ROCm parallel algorithm library"""
    roctracer: _Pkg
    """Tracer callback/activity library"""
    rocwmma: _Pkg
    """Mixed precision matrix multiplication and accumulation"""
    rpp: _Pkg
    """Comprehensive high-performance computer vision library for AMD processors"""
    stdenv: _Pkg
    """The default build environment for Unix packages in Nixpkgs"""
    tensile: _Pkg
    """GEMMs and tensor contractions"""
    hip_common: _Pkg
    """C++ Heterogeneous-Compute Interface for Portability"""
    hipblas_common: _Pkg
    """Common files shared by hipBLAS and hipBLASLt"""
    hsa_amd_aqlprofile_bin: _Pkg
    """AQLPROFILE library for AMD HSA runtime API extension support"""
    miopen_hip: _Pkg
    """Machine intelligence library for ROCm"""
    mivisionx_cpu: _Pkg
    """Set of comprehensive computer vision and machine intelligence libraries, utilities, and applications"""
    mivisionx_hip: _Pkg
    """Set of comprehensive computer vision and machine intelligence libraries, utilities, and applications"""
    rocm_bandwidth_test: _Prog
    """Bandwidth test for AMD GPUs supported by ROCm. Runs as `rocm-bandwidth-test`."""
    rocm_cmake: _Pkg
    """CMake modules for common build tasks for the ROCm stack"""
    rocm_comgr: _Pkg
    """APIs for compiling and inspecting AMDGPU code objects"""
    rocm_core: _Pkg
    """Utility for getting the ROCm release version"""
    rocm_device_libs: _Pkg
    """Set of AMD-specific device-side language runtime libraries"""
    rocm_docs_core: _Pkg
    """ROCm Documentation Python package for ReadTheDocs build standardization"""
    rocm_runtime: _Pkg
    """Platform runtime for ROCm"""
    rocm_smi: _Pkg
    """System management interface for AMD GPUs supported by ROCm"""
    rocm_tests: _Pkg
    rocm_toolchain: _Pkg
    rocmlir_rock: _Pkg
    """MLIR-based convolution and GEMM kernel generator"""
    rocprof_compute_viewer: _Prog
    """Visualization tool for AMD GPU thread traces from rocprofv3 --att. Runs as `rocprof-compute-viewer`."""
    rocprof_trace_decoder: _Pkg
    """Library for decoding ROCm thread trace data"""
    rocprofiler_register: _Pkg
    """Profiling with perf-counters and derived metrics"""
    rocprofiler_sdk: _Pkg
    """ROCm GPU performance analysis SDK"""
    rocr_debug_agent: _Pkg
    """Library that provides some debugging functionality for ROCr"""
    rpp_cpu: _Pkg
    """Comprehensive high-performance computer vision library for AMD processors"""
    rpp_hip: _Pkg
    """Comprehensive high-performance computer vision library for AMD processors"""
