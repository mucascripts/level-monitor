from pydantic import BaseModel

from . import evaluators


class Character(BaseModel):
    name: str
    level: int
    resets: int

    @classmethod
    def from_tuple(cls, tuple_: tuple[str, str, str]) -> "Character":
        return cls(
            name=tuple_[0],
            level=tuple_[1],
            resets=tuple_[2],
        )

    def reset_ready(self, table: str) -> bool:
        return evaluators.is_reset_ready(self, table)
