.. meta::
    :description: This page lists supported graph safe ROCm libraries.
    :keywords: AMD, ROCm, HIP, hipGRAPH

********************************************************************************
Graph safe library support
********************************************************************************

A library designed to operate safely within HIP execution graphs is known as a HIP graph-safe library. :ref:`hip:how_to_HIP_graph` are an alternative way of executing
tasks on a  GPU that can provide performance benefits over launching kernels
using the standard method via streams. 

In a graph-safe library, functions and routines are designed to work without
causing issues like race conditions, deadlocks, or unintended dependencies. To know if a ROCm library is graph-safe, see the following table:

.. list-table::
    :header-rows: 1

    *
      - ROCm library
      - Graph safe support
    * 
      - `rocBLAS <https://github.com/ROCm/rocBLAS>`_
      - ✅ (See :doc:`details <rocblas:reference/beta-features>`)
    * 
      - `hipBLAS <https://github.com/ROCm/hipBLAS>`_
      - ✅
    * 
      - `Tensile <https://github.com/ROCm/Tensile>`_
      - ✅
    * 
      - `rocFFT <https://github.com/ROCm/rocFFT>`_
      - ✅
    * 
      - `hipFFT <https://github.com/ROCm/hipFFT>`_
      - ✅
    * 
      - `rocRAND <https://github.com/ROCm/rocRAND>`_
      - ✅
    * 
      - `rocPRIM <https://github.com/ROCm/rocPRIM>`_
      - ✅
    * 
      - `rocSPARSE <https://github.com/ROCm/rocSPARSE>`_
      - ⚠️ (experimental)
    * 
      - `hipSPARSE <https://github.com/ROCm/hipSPARSE>`_
      - ✅
    * 
      - `rocHPCG <https://github.com/ROCm/rocHPCG>`_
      - ❌
    * 
      - `rocALUTION <https://github.com/ROCm/rocALUTION>`_
      - ❌
    * 
      - `MIVisionX <https://github.com/ROCm/MIVisionX>`_
      - N/A
    * 
      - `RPP <https://github.com/ROCm/rpp>`_
      - ⚠️
    * 
      - `rocAL <https://github.com/ROCm/rocAL>`_
      - ❌
    * 
      - `rocDecode <https://github.com/ROCm/rocDecode>`_
      - ❌
    * 
      - `rocThrust <https://github.com/ROCm/rocThrust>`_
      - ❌ (See :doc:`details <rocthrust:hipgraph-support>`)
    * 
      - `MIOpen <https://github.com/ROCm/MIOpen>`_
      - ❌
    * 
      - `TUNA <https://github.com/ROCm/TUNA>`_
      - N/A
    * 
      - `hipCUB <https://github.com/ROCm/hipCUB>`_
      - ✅
    * 
      - `rocSOLVER <https://github.com/ROCm/rocSOLVER>`_
      - ⚠️ (experimental)
    * 
      - `hipSOLVER <https://github.com/ROCm/hipSOLVER>`_
      - ⚠️ (experimental)
    * 
      - `RCCL <https://github.com/ROCm/rccl>`_
      - ✅
    * 
      - `rocWMMA <https://github.com/ROCm/rocWMMA>`_
      - N/A (GPU header library)
    * 
      - `hipTensor <https://github.com/ROCm/hipTensor>`_
      - ❌
    * 
      - `composable kernel <https://github.com/ROCm/composable_kernel>`_
      - ❌
    * 
      - `hipBLASLt <https://github.com/ROCm/hipBLASLt>`_
      - ⚠️
    * 
      - `hipFORT <https://github.com/ROCm/hipFORT>`_
      - N/A
    * 
      - `hipSPARSELt <https://github.com/ROCm/hipSPARSELt>`_
      - ⚠️ (experimental)
    * 
      - `rocJPEG <https://github.com/ROCm/rocJPEG>`_
      - ❌

✅: full support

⚠️: partial support

❌: not supported
