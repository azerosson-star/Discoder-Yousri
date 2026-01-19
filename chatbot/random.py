"""Compat layer for broken stdlib `random`.

This workspace runs on a Python distribution where `Lib/random.py` is incomplete
(missing `randint`, `choice`, etc.). A number of dependencies (and this project)
expect the standard API.

Placing this module in the project root ensures it is found on `sys.path` before
the incomplete stdlib module.

Note: This is intentionally a small subset of CPython's `random` module.
"""

from __future__ import annotations

from typing import Any, MutableSequence, Sequence, TypeVar

import _random
import os

T = TypeVar("T")


class Random:
    def __init__(self, seed: Any | None = None):
        self._rng = _random.Random()
        if seed is not None:
            self.seed(seed)

    def seed(self, a: Any | None = None) -> None:
        self._rng.seed(a)

    def random(self) -> float:
        return self._rng.random()

    def randrange(self, start: int, stop: int | None = None, step: int = 1) -> int:
        if step == 0:
            raise ValueError("step argument must not be zero")
        if stop is None:
            start, stop = 0, start
        if stop is None:
            raise TypeError("stop cannot be None")
        width = stop - start
        if step == 1 and width > 0:
            return start + int(self._rng.random() * width)

        # Generic (but simple) implementation
        n = (width + step - 1) // step if step > 0 else (width + step + 1) // step
        if n <= 0:
            raise ValueError("empty range for randrange()")
        return start + step * int(self._rng.random() * n)

    def randint(self, a: int, b: int) -> int:
        return self.randrange(a, b + 1)

    def choice(self, seq: Sequence[T]) -> T:
        if not seq:
            raise IndexError("Cannot choose from an empty sequence")
        return seq[self.randrange(len(seq))]

    def choices(
        self,
        population: Sequence[T],
        weights: Sequence[float] | None = None,
        cum_weights: Sequence[float] | None = None,
        k: int = 1,
    ) -> list[T]:
        if k < 0:
            raise ValueError("k must be a non-negative integer")
        if not population:
            raise IndexError("Cannot choose from an empty population")

        if weights is not None and cum_weights is not None:
            raise TypeError("Cannot specify both weights and cum_weights")

        if weights is None and cum_weights is None:
            return [self.choice(population) for _ in range(k)]

        if cum_weights is None:
            total = 0.0
            cum: list[float] = []
            for w in weights or []:
                total += float(w)
                cum.append(total)
            cum_weights = cum

        if len(cum_weights) != len(population):
            raise ValueError("The number of weights does not match the population")

        total = float(cum_weights[-1])
        if total <= 0:
            raise ValueError("Total of weights must be > 0")

        result: list[T] = []
        for _ in range(k):
            r = self.random() * total
            # linear search (small k/pop; good enough here)
            idx = 0
            for idx, cw in enumerate(cum_weights):
                if r < float(cw):
                    break
            result.append(population[idx])
        return result

    def shuffle(self, x: MutableSequence[T]) -> None:
        for i in range(len(x) - 1, 0, -1):
            j = self.randrange(i + 1)
            x[i], x[j] = x[j], x[i]

    def uniform(self, a: float, b: float) -> float:
        return a + (b - a) * self.random()


class SystemRandom(Random):
    """PRNG basé sur os.urandom (équivalent simplifié de `random.SystemRandom`)."""

    def __init__(self, seed: Any | None = None):
        # `SystemRandom` ignore le seed
        super().__init__(seed=None)

    def seed(self, a: Any | None = None) -> None:  # pragma: no cover
        return None

    def randbits(self, k: int) -> int:
        if k < 0:
            raise ValueError("number of bits must be non-negative")
        if k == 0:
            return 0
        nbytes = (k + 7) // 8
        x = int.from_bytes(os.urandom(nbytes), "big")
        return x >> (nbytes * 8 - k)

    # API stdlib
    getrandbits = randbits

    def random(self) -> float:
        # 53 bits de précision comme CPython
        return self.randbits(53) / (1 << 53)

    def _randbelow(self, n: int) -> int:
        if n <= 0:
            raise ValueError("n must be > 0")
        k = n.bit_length()
        while True:
            r = self.randbits(k)
            if r < n:
                return r

    def randrange(self, start: int, stop: int | None = None, step: int = 1) -> int:
        if step == 0:
            raise ValueError("step argument must not be zero")
        if stop is None:
            start, stop = 0, start
        if stop is None:
            raise TypeError("stop cannot be None")

        width = stop - start
        if step == 1:
            if width <= 0:
                raise ValueError("empty range for randrange()")
            return start + self._randbelow(width)

        n = (width + step - 1) // step if step > 0 else (width + step + 1) // step
        if n <= 0:
            raise ValueError("empty range for randrange()")
        return start + step * self._randbelow(n)


_inst = Random()


def seed(a: Any | None = None) -> None:
    _inst.seed(a)


def random() -> float:
    return _inst.random()


def randrange(start: int, stop: int | None = None, step: int = 1) -> int:
    return _inst.randrange(start, stop, step)


def randint(a: int, b: int) -> int:
    return _inst.randint(a, b)


def choice(seq: Sequence[T]) -> T:
    return _inst.choice(seq)


def choices(
    population: Sequence[T],
    weights: Sequence[float] | None = None,
    cum_weights: Sequence[float] | None = None,
    k: int = 1,
) -> list[T]:
    return _inst.choices(population, weights=weights, cum_weights=cum_weights, k=k)


def shuffle(x: MutableSequence[T]) -> None:
    _inst.shuffle(x)


def uniform(a: float, b: float) -> float:
    return _inst.uniform(a, b)


__all__ = [
    "Random",
    "SystemRandom",
    "seed",
    "random",
    "randrange",
    "randint",
    "choice",
    "choices",
    "shuffle",
    "uniform",
]
