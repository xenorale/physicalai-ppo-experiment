"""Limit the PyTorch GPU allocator before executing the unchanged course script."""

import os
import runpy
import sys

os.environ.setdefault("XLA_PYTHON_CLIENT_PREALLOCATE", "false")
os.environ.setdefault("XLA_PYTHON_CLIENT_MEM_FRACTION", "0.30")

import torch

if torch.cuda.is_available():
    torch.cuda.set_per_process_memory_fraction(0.12, device=0)

target, *arguments = sys.argv[1:]
sys.argv = [target, *arguments]
runpy.run_path(target, run_name="__main__")
