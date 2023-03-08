"""
Run this to initialize a new training config to a file.
"""

import sys
from pathlib import Path
from typing import List

from dolma import TrainConfig
from dolma.exceptions import DolmaCliError
from dolma.util import clean_opt, echo, prepare_cli_environment


def main(save_path: Path, args_list: List[str]) -> None:
    cfg = TrainConfig.new(overrides=args_list)
    echo.info("Configuration:", cfg)
    cfg.save(save_path)
    echo.success(f"Config saved to {save_path}")


if __name__ == "__main__":
    prepare_cli_environment()

    try:
        save_path, args_list = sys.argv[1], sys.argv[2:]
    except IndexError:
        raise DolmaCliError(f"Usage: {sys.argv[0]} [SAVE_PATH] [OPTIONS]")

    main(Path(save_path), [clean_opt(s) for s in args_list])