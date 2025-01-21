import os
import ast
import subprocess

# Function to get the imported libraries from a Python file
def get_imports_from_file(file_path):
    with open(file_path, "r") as file:
        tree = ast.parse(file.read())
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module)
    return imports

# Function to scan the directory for all imported libraries
def scan_directory_for_imports(directory):
    all_imports = set()
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                all_imports.update(get_imports_from_file(file_path))
    return all_imports

# Function to get the version of a package using pip show
def get_package_version(package_name):
    try:
        result = subprocess.run(
            ["pip", "show", package_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
            text=True
        )
        version_line = next(line for line in result.stdout.split("\n") if line.startswith("Version"))
        version = version_line.split(":")[1].strip()
        return version
    except subprocess.CalledProcessError:
        return None  # Return None if the package is not installed

# Function to create the environment.yml file based on imports and versions
def create_conda_env_yml(imports, filename="environment.yml"):
    dependencies = []
    for imp in imports:
        version = get_package_version(imp)
        if version:
            dependencies.append(f"{imp}=={version}")
        else:
            dependencies.append(imp)
    
    conda_env = {
        "name": "my_environment",  # You can customize the environment name
        "channels": [
            "defaults",
            "conda-forge"
        ],
        "dependencies": [
            "python=3.8",  # Adjust this to your required Python version
            *dependencies
        ]
    }
    
    # Write the environment.yml file
    with open(filename, "w") as file:
        import yaml
        yaml.dump(conda_env, file, default_flow_style=False)

# Specify the directory to scan
project_directory = "../SSCL"
imports = scan_directory_for_imports(project_directory)

# Create the environment.yml file
create_conda_env_yml(imports)

print(f"environment.yml file has been created with the following dependencies:\n{imports}")
