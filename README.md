# NL2KubeFlow: Natural Language to Kubeflow Pipelines (Prototype)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A proof-of-concept CLI that converts keyword-based prompts into valid Kubeflow Pipeline YAML configurations.

## 📖 Overview
This prototype demonstrates:
- Basic prompt parsing using keyword detection
- Generation of valid Kubeflow workflow templates
- Foundation for future NLP integration

## 🚀 Quick Start
1. Install dependencies:
   ```bash
   pip install pyyaml
2 Generate pipeline:
   ```bash
  python cli.py --prompt "Create pipeline with train and deploy steps
3 Output (build/pipeline.yaml):
