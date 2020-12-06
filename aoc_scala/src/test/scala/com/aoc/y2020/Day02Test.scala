package com.aoc.y2020

import org.scalatest.{FlatSpec, Matchers}

class Day02Test extends FlatSpec with Matchers {
  "Day02 - validatePassword" should "validate password" in {
    assert(
      Day02.validatePassword("1-3 a: abcde") == 1
    )
  }
  "Day02 - solvePart1" should "solve first task" in {
    assert(
      Day02.solvePart1(
        List("1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc")
      ) == 2
    )
  }
  "Day02 - solvePart2" should "solve second task" in {
    assert(
      Day02.solvePart2(
        List("1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc")
      ) == 1
    )
  }
}
