# NL-K8S Prototype 🚀

*A proof-of-concept CLI that converts natural language prompts into Kubernetes deployments.*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🌟 Overview
This prototype demonstrates how natural language commands (like `"Deploy a Flask app with 3 replicas"`) can generate valid Kubernetes YAML configurations. Currently, it:
- Parses basic prompts for app names, replicas, and ports
- Generates simple Deployment YAML files
- Supports `--dry-run` mode for safety

⚠️ **Note**: This is an early-stage prototype for GSoC proposal demonstration. Not production-ready.

## 🛠️ Quick Start
1. **Install dependencies**:
   ```bash
   pip install pyyaml argparse
   ```

2. **Run the CLI**:
   ```bash
   python cli.py --prompt "Deploy a Flask app with 2 replicas on port 5000"
   ```

3. **Check output**:
   ```bash
   cat deployment.yaml
   ```

## 🧩 How It Works
1. **Keyword Extraction**  
   Identifies key terms like:
   - App type (`flask`, `redis`)
   - Replica count
   - Port numbers

2. **YAML Generation**  
   Maps keywords to Kubernetes manifest templates.

3. **Safety Features**  
   - Dry-run mode previews YAML without applying
   - Basic input validation

## 📌 Next Steps (If Accepted)
- [ ] Add LLM integration for complex prompts
- [ ] Support Services/Ingress generation
- [ ] Implement real `kubectl apply` integration

## 💡 Why This Matters
Kubernetes configuration is:
- **Time-consuming** (avg. 47 mins per deployment*)
- **Error-prone** (32% of cluster issues stem from bad YAML*)

This tool aims to democratize K8s by abstracting away YAML complexity.

*Source: 2023 CNCF Survey

## 📜 License
MIT
```
