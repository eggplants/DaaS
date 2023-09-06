from __future__ import annotations

from functools import lru_cache

from daas import config
from daas.model.dajare_model import DajareModel
from daas.service.engine.eval_engine import EvalEngine
from daas.service.engine.judge_engine import JudgeEngine
from daas.service.engine.reading_engine import ReadingEngine


class DajareService:
    def __init__(self) -> None:
        # create core engines
        self.__judge_engine = JudgeEngine()
        self.__eval_engine = EvalEngine()
        self.__reading_engine = ReadingEngine()

    @lru_cache(config.CACHE_SIZE)  # noqa: B019
    def judge_dajare(self, dajare_text: str) -> DajareModel:
        result = DajareModel()
        result.text = dajare_text
        result.is_dajare = self.__judge_engine.exec(dajare_text)
        result.applied_rule = self.__judge_engine.applied_rule
        return result

    @lru_cache(config.CACHE_SIZE)  # noqa: B019
    def eval_dajare(self, dajare_text: str) -> DajareModel:
        result = DajareModel()
        result.text = dajare_text
        result.score = self.__eval_engine.exec(dajare_text)
        return result

    @lru_cache(config.CACHE_SIZE)  # noqa: B019
    def convert_reading(self, dajare_text: str) -> DajareModel:
        result = DajareModel()
        result.text = dajare_text
        result.reading = self.__reading_engine.exec(dajare_text)
        return result
