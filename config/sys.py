import os

################################
# System wide vars
################################

def get_project_root() -> str:
    """Get the project root directory"""
    return os.path.join(os.path.dirname(os.path.abspath(__file__)))
