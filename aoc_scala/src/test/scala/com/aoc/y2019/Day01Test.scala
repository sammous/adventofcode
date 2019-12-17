package com.aoc.y2019

import org.scalatest.{FlatSpec, Matchers}

class Day01Test extends FlatSpec with Matchers {
  "Day01 - solvePart1" should "solve first task" in {
    assert(Day01.solvePart1(List(12, 14, 1969, 100756)) == 34241)
  }
  "Day01 - solvePart2" should "solve second task" in {
    assert(Day01.solvePart2(List(12, 1969, 100756)) == 51314)
  }
}
