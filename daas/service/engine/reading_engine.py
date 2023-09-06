from __future__ import annotations

from daas.util import text_util


class ReadingEngine:
    def exec(self, text: str) -> str:  # noqa: A003
        # text_util
        result: str = text_util.preprocessing(text)
        return text_util.reading(result)
