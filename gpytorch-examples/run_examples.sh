#!/usr/bin/env bash
#
# run_examples.sh -- Execute GPyTorch example notebooks locally on Apple M1 Max (MPS backend).
#
# Category A: Notebooks that run on CPU (no CUDA references, or CPU-only).
# Category B: Notebooks originally written for CUDA; patched to MPS before execution.
#
# Usage:
#   ./run_examples.sh              # Run all Category A and B notebooks
#   ./run_examples.sh --category A # Run only Category A
#   ./run_examples.sh --category B # Run only Category B
#   ./run_examples.sh --list       # List notebooks without running
#   ./run_examples.sh --dry-run    # Show what would be done without executing
#

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="${SCRIPT_DIR}/.venv"
PATCH_SCRIPT="${SCRIPT_DIR}/patch_cuda_to_mps.py"
LOG_DIR="${SCRIPT_DIR}/logs"

# ── Activate virtual environment ──────────────────────────────────────────────
if [[ ! -d "${VENV_DIR}" ]]; then
    echo "ERROR: Virtual environment not found at ${VENV_DIR}"
    echo "Create it with: python3.11 -m venv ${VENV_DIR} && ${VENV_DIR}/bin/pip install gpytorch torch torchvision jupyter matplotlib scipy"
    exit 1
fi
source "${VENV_DIR}/bin/activate"

# ── Notebook lists ────────────────────────────────────────────────────────────

# Category A: Notebooks that work without CUDA device patching.
# Includes directories 00-05 (excluding CUDA-named files), 07, and 08 (excluding TorchScript_Variational).
CATEGORY_A=(
    # 00_Basic_Usage
    "00_Basic_Usage/Hyperparameters.ipynb"
    "00_Basic_Usage/Implementing_a_custom_Kernel.ipynb"
    "00_Basic_Usage/Metrics.ipynb"
    "00_Basic_Usage/Saving_and_Loading_Models.ipynb"
    "00_Basic_Usage/kernels_with_additive_or_product_structure.ipynb"

    # 01_Exact_GPs
    "01_Exact_GPs/GP_Regression_DistributionalKernel.ipynb"
    "01_Exact_GPs/GP_Regression_Fully_Bayesian.ipynb"
    "01_Exact_GPs/GP_Regression_on_Classification_Labels.ipynb"
    "01_Exact_GPs/Simple_GP_Regression.ipynb"
    "01_Exact_GPs/Spectral_Delta_GP_Regression.ipynb"
    "01_Exact_GPs/Spectral_Mixture_GP_Regression.ipynb"

    # 02_Scalable_Exact_GPs (CPU-only ones)
    "02_Scalable_Exact_GPs/Exact_GP_Posterior_Sampling_with_CIQ.ipynb"
    "02_Scalable_Exact_GPs/Grid_GP_Regression.ipynb"
    "02_Scalable_Exact_GPs/KISSGP_Regression.ipynb"
    "02_Scalable_Exact_GPs/KeOps_GP_Regression.ipynb"
    "02_Scalable_Exact_GPs/Simple_GP_Regression_With_LOVE_Fast_Variances_and_Sampling.ipynb"

    # 03_Multitask_Exact_GPs
    "03_Multitask_Exact_GPs/Batch_Independent_Multioutput_GP.ipynb"
    "03_Multitask_Exact_GPs/Hadamard_Multitask_GP_Regression.ipynb"
    "03_Multitask_Exact_GPs/ModelList_GP_Regression.ipynb"
    "03_Multitask_Exact_GPs/Multitask_GP_Regression.ipynb"

    # 04_Variational_and_Approximate_GPs (CPU-only ones)
    "04_Variational_and_Approximate_GPs/Approximate_GP_Objective_Functions.ipynb"
    "04_Variational_and_Approximate_GPs/GP_Regression_with_Uncertain_Inputs.ipynb"
    "04_Variational_and_Approximate_GPs/Modifying_the_variational_strategy_and_distribution.ipynb"
    "04_Variational_and_Approximate_GPs/Natural_Gradient_Descent.ipynb"
    "04_Variational_and_Approximate_GPs/Non_Gaussian_Likelihoods.ipynb"
    "04_Variational_and_Approximate_GPs/PolyaGamma_Binary_Classification.ipynb"
    "04_Variational_and_Approximate_GPs/SVGP_CIQ.ipynb"
    "04_Variational_and_Approximate_GPs/SVGP_Multitask_GP_Regression.ipynb"
    "04_Variational_and_Approximate_GPs/VNNGP.ipynb"

    # 05_Deep_Gaussian_Processes (DGP_Multitask only per task spec)
    "05_Deep_Gaussian_Processes/DGP_Multitask_Regression.ipynb"

    # 07_Pyro_Integration
    "07_Pyro_Integration/Clustered_Multitask_GP_Regression.ipynb"
    "07_Pyro_Integration/Cox_Process_Example.ipynb"
    "07_Pyro_Integration/Pyro_GPyTorch_High_Level.ipynb"
    "07_Pyro_Integration/Pyro_GPyTorch_Low_Level.ipynb"

    # 08_Advanced_Usage (excluding TorchScript_Variational)
    "08_Advanced_Usage/SVGP_Model_Updating.ipynb"
    "08_Advanced_Usage/Simple_Batch_Mode_GP_Regression.ipynb"
    "08_Advanced_Usage/Simple_GP_Regression_Derivative_Information_1d.ipynb"
    "08_Advanced_Usage/Simple_GP_Regression_Derivative_Information_2d.ipynb"
    "08_Advanced_Usage/TorchScript_Exact_Models.ipynb"
)

# Category B: Notebooks with CUDA references that need to be patched to MPS.
CATEGORY_B=(
    "02_Scalable_Exact_GPs/SGPR_Regression_CUDA.ipynb"
    "02_Scalable_Exact_GPs/Scalable_Kernel_Interpolation_for_Products_CUDA.ipynb"
    "02_Scalable_Exact_GPs/Simple_GP_Regression_CUDA.ipynb"
    "02_Scalable_Exact_GPs/Simple_MultiGPU_GP_Regression.ipynb"
    "04_Variational_and_Approximate_GPs/SVGP_Regression_CUDA.ipynb"
    "06_PyTorch_NN_Integration_DKL/Deep_Kernel_Learning_DenseNet_CIFAR_Tutorial.ipynb"
    "06_PyTorch_NN_Integration_DKL/KISSGP_Deep_Kernel_Regression_CUDA.ipynb"
)

# ── Parse arguments ───────────────────────────────────────────────────────────
CATEGORY="AB"
LIST_ONLY=false
DRY_RUN=false

while [[ $# -gt 0 ]]; do
    case "$1" in
        --category)
            CATEGORY="$2"
            shift 2
            ;;
        --list)
            LIST_ONLY=true
            shift
            ;;
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        *)
            echo "Unknown argument: $1"
            exit 1
            ;;
    esac
done

# ── Helper functions ──────────────────────────────────────────────────────────
mkdir -p "${LOG_DIR}"

run_notebook() {
    local nb_path="$1"
    local full_path="${SCRIPT_DIR}/${nb_path}"
    local log_name
    log_name="$(echo "${nb_path}" | tr '/' '_' | sed 's/.ipynb$//')"
    local log_file="${LOG_DIR}/${log_name}.log"

    echo "  Running: ${nb_path}"
    if jupyter nbconvert \
        --to notebook \
        --execute \
        --ExecutePreprocessor.timeout=600 \
        --ExecutePreprocessor.kernel_name=python3 \
        --output-dir="${LOG_DIR}" \
        "${full_path}" \
        > "${log_file}" 2>&1; then
        echo "    [OK]"
        return 0
    else
        echo "    [FAILED] -- see ${log_file}"
        return 1
    fi
}

patch_and_run_notebook() {
    local nb_path="$1"
    local full_path="${SCRIPT_DIR}/${nb_path}"
    local patched_dir="${LOG_DIR}/patched"
    mkdir -p "${patched_dir}"

    local basename
    basename="$(basename "${nb_path}")"
    local patched_path="${patched_dir}/${basename}"

    echo "  Patching: ${nb_path}"
    python "${PATCH_SCRIPT}" "${full_path}" --output "${patched_path}"

    local log_name
    log_name="$(echo "${nb_path}" | tr '/' '_' | sed 's/.ipynb$//')"
    local log_file="${LOG_DIR}/${log_name}.log"

    echo "  Running (patched): ${nb_path}"
    if jupyter nbconvert \
        --to notebook \
        --execute \
        --ExecutePreprocessor.timeout=600 \
        --ExecutePreprocessor.kernel_name=python3 \
        --output-dir="${LOG_DIR}" \
        "${patched_path}" \
        > "${log_file}" 2>&1; then
        echo "    [OK]"
        return 0
    else
        echo "    [FAILED] -- see ${log_file}"
        return 1
    fi
}

list_notebooks() {
    local category="$1"
    shift
    local -a notebooks=("$@")
    echo ""
    echo "Category ${category}:"
    for nb in "${notebooks[@]}"; do
        echo "  ${nb}"
    done
}

# ── Main ──────────────────────────────────────────────────────────────────────
echo "==========================================="
echo "GPyTorch Examples Runner (Apple MPS Backend)"
echo "==========================================="
echo "Python:   $(python --version 2>&1)"
echo "PyTorch:  $(python -c 'import torch; print(torch.__version__)')"
echo "GPyTorch: $(python -c 'import gpytorch; print(gpytorch.__version__)')"
echo "MPS:      $(python -c 'import torch; print("available" if torch.backends.mps.is_available() else "NOT available")')"
echo "==========================================="

if ${LIST_ONLY}; then
    if [[ "${CATEGORY}" == *A* ]] || [[ "${CATEGORY}" == "AB" ]]; then
        list_notebooks "A (CPU/MPS-compatible)" "${CATEGORY_A[@]}"
    fi
    if [[ "${CATEGORY}" == *B* ]] || [[ "${CATEGORY}" == "AB" ]]; then
        list_notebooks "B (CUDA -> MPS patched)" "${CATEGORY_B[@]}"
    fi
    echo ""
    echo "Total: $(( ${#CATEGORY_A[@]} + ${#CATEGORY_B[@]} )) notebooks"
    exit 0
fi

PASSED=0
FAILED=0
FAILED_NAMES=()

# Run Category A
if [[ "${CATEGORY}" == *A* ]] || [[ "${CATEGORY}" == "AB" ]]; then
    echo ""
    echo "=== Category A: CPU/MPS-compatible notebooks ==="
    for nb in "${CATEGORY_A[@]}"; do
        if ${DRY_RUN}; then
            echo "  [dry-run] Would run: ${nb}"
        else
            if run_notebook "${nb}"; then
                PASSED=$((PASSED + 1))
            else
                FAILED=$((FAILED + 1))
                FAILED_NAMES+=("${nb}")
            fi
        fi
    done
fi

# Run Category B (patch CUDA -> MPS first)
if [[ "${CATEGORY}" == *B* ]] || [[ "${CATEGORY}" == "AB" ]]; then
    echo ""
    echo "=== Category B: CUDA -> MPS patched notebooks ==="
    for nb in "${CATEGORY_B[@]}"; do
        if ${DRY_RUN}; then
            echo "  [dry-run] Would patch and run: ${nb}"
        else
            if patch_and_run_notebook "${nb}"; then
                PASSED=$((PASSED + 1))
            else
                FAILED=$((FAILED + 1))
                FAILED_NAMES+=("${nb}")
            fi
        fi
    done
fi

# Summary
echo ""
echo "==========================================="
echo "Summary: ${PASSED} passed, ${FAILED} failed"
if [[ ${FAILED} -gt 0 ]]; then
    echo "Failed notebooks:"
    for name in "${FAILED_NAMES[@]}"; do
        echo "  - ${name}"
    done
fi
echo "Logs: ${LOG_DIR}/"
echo "==========================================="

exit ${FAILED}
