#!/usr/bin/env python3
import argparse
from pathlib import Path


def create_project_structure(project_name, project_type="standard"):
    structures = {
        "standard": {
            "folders": ["src", "tests", "docs"],
            "files": ["README.md", ".gitignore", "requirements.txt"]
        },
        "python": {
            "folders": ["src", "tests", "docs", ".github"],
            "files": ["README.md", ".gitignore", "requirements.txt", "setup.py"]
        },
        "web": {
            "folders": ["src", "public", "tests", "docs"],
            "files": ["README.md", ".gitignore", "requirements.txt", "index.html"]
        }
    }
    
    if project_type not in structures:
        print(f"Unknown project type: {project_type}")
        print(f"Available types: {', '.join(structures.keys())}")
        return False
    
    structure = structures[project_type]
    project_path = Path(project_name)
    
    if project_path.exists():
        print(f"Error: '{project_name}' already exists!")
        return False
    
    project_path.mkdir()
    print(f"Created project folder: {project_name}/")
    
    for folder in structure["folders"]:
        folder_path = project_path / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        
        gitkeep = folder_path / ".gitkeep"
        gitkeep.touch()
        print(f"  {folder}/")
    
    file_contents = {
        "README.md": f"# {project_name}\n\nA description of your project goes here.\n\n## Installation\n\n```bash\npip install -r requirements.txt\n```\n\n## Usage\n\nDescribe how to use your project.\n\n## License\n\nMIT License",
        ".gitignore": "__pycache__/\n*.py[cod]\n*$py.class\n*.so\n.Python\nbuild/\ndevelop-eggs/\ndist/\ndownloads/\neggs/\n.eggs/\nlib/\nlib64/\nparts/\nsdist/\nvar/\nwheels/\n.venv/\nvenv/\nENV/\n.vscode/\n.idea/\n.DS_Store\n",
        "requirements.txt": "",
        "setup.py": f"from setuptools import setup, find_packages\n\nsetup(\n    name='{project_name}',\n    version='0.1.0',\n    description='A brief description',\n    packages=find_packages(),\n    python_requires='>=3.7',\n)\n",
        "index.html": '<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>' + project_name + '</title>\n</head>\n<body>\n    <h1>' + project_name + '</h1>\n</body>\n</html>\n'
    }
    
    for file_name in structure["files"]:
        file_path = project_path / file_name
        content = file_contents.get(file_name, f"# {file_name}\n")
        file_path.write_text(content)
        print(f"  {file_name}")
    
    print(f"\nProject '{project_name}' created successfully!")
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Generate a standard folder structure for new projects"
    )
    parser.add_argument(
        "project_name",
        help="Name of the project to create"
    )
    parser.add_argument(
        "-t", "--type",
        choices=["standard", "python", "web"],
        default="standard",
        help="Type of project structure (default: standard)"
    )
    
    args = parser.parse_args()
    
    create_project_structure(args.project_name, args.type)


if __name__ == "__main__":
    main()
