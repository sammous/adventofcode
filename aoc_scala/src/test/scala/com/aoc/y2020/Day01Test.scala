package com.aoc.y2020

import org.scalatest.{FlatSpec, Matchers}

class Day01Test extends FlatSpec with Matchers {
  "Day01 - solvePart1" should "solve first task" in {
    assert(Day01.solvePart1(List(1721, 979, 366, 299, 675, 1456)) == 514579)
  }
  "Day01 - solvePart2" should "solve first task" in {
    assert(Day01.solvePart2(List(1721, 979, 366, 299, 675, 1456)) == 241861950)
  }
}
