package com.aoc.y2019

import org.scalatest.{FlatSpec, Matchers}

class Day02Test extends FlatSpec with Matchers {
  "Day01 - solvePart1" should "solve first task" in {
    assert(Day02.rec(Array(1, 0, 0, 0, 99), 0) == List(2, 0, 0, 0, 99))
    assert(Day02.rec(Array(2, 3, 0, 3, 99), 0) == List(2, 3, 0, 6, 99))
    assert(Day02.rec(Array(2, 4, 4, 5, 99, 0), 0) == List(2, 4, 4, 5, 99, 9801))
    assert(
      Day02
        .rec(Array(1, 1, 1, 4, 99, 5, 6, 0, 99), 0) == List(30, 1, 1, 4, 2, 5,
        6, 0, 99)
    )

  }
}
