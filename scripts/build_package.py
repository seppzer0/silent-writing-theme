"""
Script to build a .vsix file.
"""

import io
import os
import sys
import argparse
import subprocess
from pathlib import Path
from typing import Optional

ROOTPATH: Path = Path(__file__).parents[1]
IMAGE_NAME: str = "silent-writing-theme-builder"


def parse_args() -> argparse.Namespace:
    """Parse arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-e", "--env",
        required=False,
        dest="env",
        choices=("local", "docker", "podman"),
        default="local",
        help="choose build environment for package build (default: local)"
    )
    parser.add_argument(
        "-cc", "--clean-cache",
        required=False,
        dest="cc",
        action="store_true",
        help="remove built image from Docker/Podman cache"
    )
    return parser.parse_args()


def run(cmd: str, output: Optional[bool] = False) -> subprocess.CompletedProcess:
    """Invoke shell command via subprocess wrapping.
    
    :param str cmd: Command to execute.
    :param Optional[bool]=False output: Flag to get the output of the command
    """
    if output:
        return subprocess.run(cmd, shell=True, check=True, capture_output=True, universal_newlines=True)
    else:
        return subprocess.run(cmd, shell=True, check=True)


def build_image(env: str) -> None:
    """Build the Docker/Podman image."""
    if IMAGE_NAME not in str(run(f'{env} images --format "{{{{.Repository}}}}"', True).stdout).splitlines():
        print(f"\nBuilding {env.capitalize()} image...\n")
        run(f"{env} image build {ROOTPATH} -f {ROOTPATH / "Dockerfile"} -t {IMAGE_NAME}")
        print("\nDone!\n")


def extend_cmd(cmd: str, env: str, extra_args: Optional[str] = None) -> str:
    """Extend given command with Docker usage.
    
    :param str cmd: Command to be exntended.
    :param str env: Package build environment.
    :param Optional[str]=None extra_args: Extra arguments for Docker/Podman run command.
    """
    if env in ("docker", "podman"):
        return f'{env} run --rm -i {extra_args} {IMAGE_NAME} /bin/sh -c "{cmd}"'
    else:
        return cmd


def build_package(env: str) -> subprocess.CompletedProcess:
    """Build the package.
    
    :param str env: Package build environment.
    """
    version = run(cmd=f'python {ROOTPATH / "scripts" / "get_version.py"}', output=True).stdout.rstrip()
    return run(
        extend_cmd(
            cmd=f"mkdir -p build && vsce package -o build/silent-writing-{version}.vsix",
            extra_args=f"-v {ROOTPATH}:/package -w /package",
            env=env
        )
    )


def clean_cache(env: str) -> subprocess.CompletedProcess:
    """Remove built image from Docker/Podman cache.
    
    :param str env: Package build environment.
    """
    return run(cmd=f"{env} rmi {IMAGE_NAME}")


def main(args: argparse.Namespace) -> None:
    os.chdir(ROOTPATH)
    if args.env in ("docker", "podman"):
        build_image(args.env)
    build_package(args.env)
    if args.cc:
        clean_cache(args.env)


if __name__ == "__main__":
    # for print's to show in the right order in various build / CI/CD systems
    sys.stdout = io.TextIOWrapper(open(sys.stdout.fileno(), "wb", 0), write_through=True)
    main(parse_args())
