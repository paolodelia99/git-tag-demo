import subprocess

def get_latest_tag():
    try:
        tag = subprocess.check_output(
            ["git", "describe", "--tags", "--abbrev=0"],
            stderr=subprocess.STDOUT
        ).strip().decode()
        return tag
    except subprocess.CalledProcessError:
        return "v0.0.0"  # Default if no tag is found or git fails

__version__ = get_latest_tag()
