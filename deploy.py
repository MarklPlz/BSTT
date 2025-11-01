#!/usr/bin/env python3
from pathlib import Path
import argparse
import subprocess
import tempfile
import shutil
import sys

# Config
SRC_DIR = Path("src")
IGNORE = {".git", "__pycache__", ".DS_Store", "tests"}


def run_shellcmd(cmd, capture_output=False):
    """Run a shell command."""
    result = subprocess.run(
        cmd, shell=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    if result.returncode != 0:
        print("Error:")
        sys.stdout.buffer.write(result.stderr)
        sys.stdout.buffer.write(result.stdout)
        sys.exit(result.returncode)
    return result.stdout.strip() if capture_output else ""


def gather_files():
    """Collect files from SRC_DIR."""
    for path in SRC_DIR.rglob("*"):
        if path.is_file() and not any(part in IGNORE for part in path.parts):
            yield path


def precompile_to_mpy(src_path: Path, build_dir: Path):
    """Compile .py to .mpy, or copy non-.py files."""
    relative = src_path.relative_to(SRC_DIR)
    if src_path.suffix == ".py":
        dest_path = build_dir / relative.with_suffix(".mpy")
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        run_shellcmd(f'mpy-cross "{src_path}" -o "{dest_path}"')
    else:
        dest_path = build_dir / relative
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src_path, dest_path)


# Build and deploy
def deploy_precompiled():
    """Build and upload a full precompiled package."""
    print("Building precompiled package...")

    build_dir = Path(tempfile.mkdtemp(prefix="precompiled_build_"))

    for path in gather_files():
        precompile_to_mpy(path, build_dir)

    # Add a minimal boot.py that launches main.mpy
    boot_path = build_dir / "boot.py"
    boot_path.write_text("import main\n")

    print("Uploading precompiled build to Pico...")
    # By default cp will skip copying files to the remote device if the SHA256 hash of the source and destination file matches.
    run_shellcmd(f'mpremote fs cp -r {build_dir}/* :/')
    
    shutil.rmtree(build_dir)
    print("Precompiled deploy complete.")
    
    run_shellcmd("mpremote soft-reset")


def main():
    parser = argparse.ArgumentParser(description="Build and deploy MicroPython code to Raspberry Pi Pico.")
    parser.add_argument("--clean", action="store_true", help="Wipe Pico filesystem before deploying.")
    args = parser.parse_args()
    
    # Check if mpremote is installed.
    run_shellcmd("mpy-cross --version")
    run_shellcmd("mpremote --version")

    if args.clean:
        print("Wipe filesystem...")
        run_shellcmd("mpremote rm -rv :")
    deploy_precompiled()


if __name__ == "__main__":
    main()

