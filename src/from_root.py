from pathlib import Path


def from_root(*relative_paths: str) -> str:
    """Return project root joined with optional relative path segments."""
    root = Path(__file__).resolve().parent.parent
    return str(root.joinpath(*relative_paths))
