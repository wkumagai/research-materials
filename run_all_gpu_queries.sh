#!/bin/bash
# Run all 5 GPU research queries sequentially, then combine results.
# Each query may take 7-30 minutes with gpt-5.4-pro + web_search_preview.
cd /Users/kumacmini/research-materials

echo "=== Starting all GPU research queries at $(date) ==="

for i in 1 2 3 4 5; do
    echo ""
    echo "============================================"
    echo "Running Query $i at $(date)"
    echo "============================================"
    python3 "run_gpu_q${i}.py"
    echo "Query $i finished at $(date)"
    sleep 5
done

echo ""
echo "=== All queries complete. Combining results... ==="
python3 combine_gpu_results.py

echo ""
echo "=== All done at $(date) ==="
