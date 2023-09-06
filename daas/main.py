from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

import tqdm
import uvicorn
from fastapi.testclient import TestClient
from pydantic import BaseModel, TypeAdapter

from . import config, message
from .api.controller import create_app


class DajareData(BaseModel):
    dajare: str
    is_dajare: bool


DajareDataListAdapter = TypeAdapter(list[DajareData])


class ErrorSample(BaseModel):
    dajare: str
    reading: str
    is_dajare: bool
    judge_result: float
    applied_rule: str


def start_mode() -> None:
    app = create_app()
    uvicorn.run(app, host=config.API_HOST, port=config.API_PORT)


def accuracy_mode() -> None:
    # load dajare samples
    data: list[DajareData] = []
    files: list[Path] = list(Path(config.DATA_FILE_PATH).glob("[!error]*.json"))
    for file_name in tqdm.tqdm(files):
        print(message.LOAD_FILE_MSG(str(file_name)))
        with Path(file_name).open(mode="r") as f:
            data.extend(DajareDataListAdapter.validate_python(json.load(f)))

    # specify the number of samples to use
    default_samples: int = len(data)
    input_str = input(message.N_SAMPLES_INPUT_GUIDE(default_samples, len(data))) or default_samples
    n_samples: int = int(input_str)
    data = random.sample(data, n_samples)

    # launch API
    app = TestClient(create_app())

    # measure accuracy
    error_samples: list[ErrorSample] = []
    print(message.MEASURE_ACCURACY_MSG(n_samples))
    for sample in tqdm.tqdm(data):
        judge_res = app.get("judge", params={"dajare": sample.dajare}).json()
        reading_res = app.get("reading", params={"dajare": sample.dajare}).json()
        if judge_res["is_dajare"] != sample.is_dajare:
            error_sample = ErrorSample(
                dajare=sample.dajare,
                reading=reading_res["reading"],
                is_dajare=sample.is_dajare,
                judge_result=judge_res["is_dajare"],
                applied_rule=judge_res["applied_rule"],
            )
            error_samples.append(error_sample)
    print(message.ACCURACY_MSG((n_samples - len(error_samples)) / n_samples))

    # dump error samples
    with Path(config.DATA_ERROR_FILE_PATH).open(mode="w") as f:
        f.write(json.dumps(error_samples, ensure_ascii=False, indent=2))


def parse_args() -> argparse.Namespace:
    # options
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--start", help="start app", action="store_true")
    parser.add_argument("-a", "--accuracy", help="measure accuracy", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.start:
        start_mode()
    if args.accuracy:
        accuracy_mode()


if __name__ == "__main__":
    main()
