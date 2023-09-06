from __future__ import annotations

import Levenshtein
import numpy as np
from pydantic import BaseModel

from daas import config
from daas.util import text_util


class CacheData(BaseModel):
    text: str
    score: float


class EvalEngine:
    def __init__(self) -> None:
        self.score_cache: list[CacheData] = []

    def exec(self, text: str) -> float:  # noqa: A003
        # preprocessing
        text = text_util.preprocessing(text)
        text = text_util.reading(text)

        # check fuzzy cache
        for cache in self.score_cache:
            if cache.text in text or text in cache.text:
                return cache.score
            if Levenshtein.distance(cache.text, text) <= 2:
                self.__cache(text, cache.score)
                return cache.score

        # score
        reading: str = text_util.reading(text)
        vector: list[int] = text_util.vectorize(reading)
        result = self.eval(vector)

        # store fuzzy cache
        self.__cache(text, result)

        return result

    def eval(self, vector: list[int]) -> float:  # noqa: A003
        rng = np.random.default_rng(sum(vector))
        result = rng.normal(2, 1.3) + 1.0
        if result > 5.0:
            return 5.0 - rng.random() / 5
        if result < 1.0:
            return 1.0 + rng.random() / 5

        return result

    def __cache(self, text: str, score: float) -> None:
        cache_data = CacheData(text=text, score=score)
        if len(self.score_cache) >= config.CACHE_SIZE:
            self.score_cache.pop(0)
            self.score_cache[-1] = cache_data
        else:
            self.score_cache.append(cache_data)
