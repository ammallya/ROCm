.. meta::
    :description: Environment variables reference
    :keywords: AMD, ROCm, environment variables, environment, reference

.. role:: cpp(code)
   :language: cpp

.. _env-variables-reference:

*************************************************************
ROCm environment variables
*************************************************************

The following table lists the most commonly used environment variables in the ROCm software stack. These variables help to perform simple tasks such as building a ROCm library or running applications on AMDGPUs.

.. list-table::
    :header-rows: 1
    :widths: 70,30

    * - **Environment variable**
      - **Value**

    * - | ``HIP_PATH``
        | The path of the HIP SDK on Microsoft Windows.
      - Default: ``C:/hip``

    * - | ``HIP_DIR``
        | The path of the HIP SDK on Microsoft Windows. This variable is ignored, if ``HIP_PATH`` is set.
      - Default: ``C:/hip``

    * - | ``ROCM_PATH``
        | The path of the installed ROCm software stack on Linux.
      - Default: ``/opt/rocm``

    * - | ``HIP_PLATFORM``
        | The platform targeted by HIP. If ``HIP_PLATFORM`` is not set, then HIPCC attempts to auto-detect the platform, if it can find NVCC.
      - ``amd``, ``nvidia``

HIP environment variables
=========================

The following tables list the HIP environment variables:

.. include_remote:: https://raw.githubusercontent.com/ROCm/HIP/refs/heads/env_variable_rst/docs/data/env_variables_hip.rst

ROCR-Runtime environment variables
==================================

.. https://github.com/ROCm/ROCR-Runtime/blob/master/src/core/util/flag.h
.. We need to extend the following list.

The following table lists the ROCR-Runtime environment variables:

.. list-table::
    :header-rows: 1
    :widths: 35,14,51

    * - **Environment variable**
      - **Default value**
      - **Value**

    * - | ``ROCR_VISIBLE_DEVICES``
        | Specifies a list of device indices or UUIDs to be exposed to the applications.
      - None
      - ``0,GPU-DEADBEEFDEADBEEF``

    * - | ``HSA_SCRATCH_MEM``
        | Specifies the maximum amount of scratch memory that can be used per process per GPU.
      -
      -

    * - | ``HSA_XNACK``
        | Enables XNACK.
      - None
      - 1: Enable

    * - | ``HSA_CU_MASK``
        | Sets the mask on a lower level of queue creation in the driver.
        | This mask is also applied to the queues being profiled.
      - None
      - ``1:0-8``

    * - | ``HSA_ENABLE_SDMA``
        | Enables the use of direct memory access (DMA) engines in all copy directions (Host-to-Device, Device-to-Host, Device-to-Device), when using any of the following APIs:
        | ``hsa_memory_copy``,
        | ``hsa_amd_memory_fill``,
        | ``hsa_amd_memory_async_copy``,
        | ``hsa_amd_memory_async_copy_on_engine``.
      - ``1``
      - | 0: Disable
        | 1: Enable

    * - | ``HSA_ENABLE_PEER_SDMA``
        | **Note**: This environment variable is ignored if ``HSA_ENABLE_SDMA`` is set to 0.
        | Enables the use of DMA engines for Device-to-Device copies, when using any of the following APIs:
        | ``hsa_memory_copy``,
        | ``hsa_amd_memory_async_copy``,
        | ``hsa_amd_memory_async_copy_on_engine``.
      - ``1``
      - | 0: Disable
        | 1: Enable

