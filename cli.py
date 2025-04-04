# cli.py
import argparse
import yaml

def generate_deployment(name, image, replicas, port):
    return {
        "apiVersion": "apps/v1",
        "kind": "Deployment",
        "metadata": {"name": name},
        "spec": {
            "replicas": replicas,
            "selector": {
                "matchLabels": {"app": name}
            },
            "template": {
                "metadata": {"labels": {"app": name}},
                "spec": {
                    "containers": [{
                        "name": name,
                        "image": image,  # Use dynamic image
                        "ports": [{"containerPort": port}]
                    }]
                }
            }
        }
    }

def parse_prompt(prompt: str):
    """Parses the prompt to extract deployment details."""
    name = "my-app"
    image = "nginx"  # Default image

    if "flask" in prompt.lower():
        name, image = "flask-app", "python:3.9"
    elif "node" in prompt.lower():
        name, image = "node-app", "node:20"
    elif "redis" in prompt.lower():
        name, image = "redis-db", "redis"

    replicas = 1
    if "replicas" in prompt.lower():
        try:
            replicas = int(prompt.lower().split("replicas")[1].split()[0])
        except (IndexError, ValueError):
            pass  # Keep default if parsing fails

    port = 80
    if "port" in prompt.lower():
        try:
            port = int(prompt.lower().split("port")[1].split()[0])
        except (IndexError, ValueError):
            pass  # Keep default if parsing fails

    return name, image, replicas, port

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Deploy apps with English!")
    parser.add_argument("--prompt", type=str, required=True)
    parser.add_argument("--dry-run", action="store_true")  # Corrected placement
    args = parser.parse_args()

    name, image, replicas, port = parse_prompt(args.prompt)
    yaml_output = generate_deployment(name, image, replicas, port)

    if args.dry_run:
        print(yaml.dump(yaml_output, default_flow_style=False))
        exit()  # Exit here properly

    with open("deployment.yaml", "w") as f:
        yaml.dump(yaml_output, f, default_flow_style=False)

    print("Generated deployment.yaml!")
