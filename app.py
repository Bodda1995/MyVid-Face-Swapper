#!/usr/bin/env python3

import os
import sys

# Performance settings
os.environ["OMP_NUM_THREADS"] = "2"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"

from facefusion import core

if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.argv.extend([
            "run",
            "--execution-providers", "cuda",
            "--video-memory-strategy", "tolerant"
        ])

    core.cli()