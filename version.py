import subprocess

def get_latest_tag() -> str:
    try:
        tag = subprocess.check_output(
            ["git", "describe", "--tags", "--abbrev=0"],
            stderr=subprocess.STDOUT
        ).strip().decode()
        print(f"Latest tag: {tag}")
        return tag
    except subprocess.CalledProcessError:
        print("Tag not found falling back to v0.0.0")
        return "v0.0.0"  # Default if no tag is found or git fails

__version__ = get_latest_tag()
