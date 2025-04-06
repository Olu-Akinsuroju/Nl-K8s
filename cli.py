import argparse
import yaml
import os

def parse_prompt(prompt: str):
    """Simple keyword detection."""
    steps = []
    prompt = prompt.lower()
    if "preprocess" in prompt:
        steps.append("preprocess")
    if "train" in prompt:
        steps.append("train")
    if "deploy" in prompt:
        steps.append("deploy")
    if not steps:
        steps.append("preprocess")
    return steps

def generate_pipeline(steps: list):
    """Generate Kubeflow Pipeline YAML from identified steps."""
    return {
        "apiVersion": "argoproj.io/v1alpha1",
        "kind": "Workflow",
        "metadata": {"generateName": "pipeline-"},
        "spec": {
            "entrypoint": "main",
            "templates": [
                {
                    "name": "main",
                    "steps": [[{"name": step, "template": step} for step in steps]]
                },
                *[{
                    "name": step,
                    "container": {
                        "image": f"kubeflow/{step}:latest",
                        "command": ["python", f"/app/{step}.py"]
                    }
                } for step in steps]
            ]
        }
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Kubeflow Pipelines from natural language prompts.")
    parser.add_argument("--prompt", type=str, required=True, help="Description of desired pipeline.")
    args = parser.parse_args()

    try:
        steps = parse_prompt(args.prompt)
        pipeline_config = generate_pipeline(steps)

        os.makedirs("build", exist_ok=True)
        with open("build/pipeline.yaml", "w") as f:
            yaml.dump(pipeline_config, f, sort_keys=False, default_flow_style=False)

        print("✅ Successfully generated build/pipeline.yaml!")
        print(f"📋 Detected steps: {', '.join(steps)}")

    except Exception as e:
        print(f"❌ Error: {str(e)}")
        exit(1)

