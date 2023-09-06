from __future__ import annotations

from importlib import resources

# path config
DATA_FILE_PATH: str = "./data"
DATA_ERROR_FILE_PATH: str = "./data/error.json"

# internal configuration files
CONFIG_FILE_ROOT_PATH = resources.files("daas") / "config"
READING_DICT_FILE_PATH: str = str(CONFIG_FILE_ROOT_PATH / "reading_dict.csv")
JUDGE_PASS_DICT_PATH: str = str(CONFIG_FILE_ROOT_PATH / "judge_pass_dict.txt")
JUDGE_REJECT_DICT_PATH: str = str(CONFIG_FILE_ROOT_PATH / "judge_reject_dict.txt")

# text config
TEXT_MAX_LENGTH: int = 30
TIGHT_LENGTH: int = 20
CACHE_SIZE: int = 128

# api config
API_SUCCESS_MSG: str = "success"
API_RESPONSE: dict[str, str] = {"message": API_SUCCESS_MSG}
API_HOST: str = "0.0.0.0"  # noqa: S104
API_PORT: int = 50000
API_DEBUG: bool = False
