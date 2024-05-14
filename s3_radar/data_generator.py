import tempfile
import uuid
from pathlib import Path


def build_target_file_path(local_file_path: Path) -> str:
    return f".speed-test/{local_file_path.name}"


def generate_file(byte_size: int) -> Path:
    try:
        with tempfile.NamedTemporaryFile(delete=False) as file:
            file.write(generate_string(byte_size).encode())
    except BaseException:
        with Path(f"tmp-gen-file-{uuid.uuid4()!s}").open(mode="w+b") as file:
            file.write(generate_string(byte_size).encode())
    return Path(file.name)


def generate_string(byte_size: int) -> str:
    return "a" * byte_size
