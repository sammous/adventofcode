package aoc

import org.scalatest.{FlatSpec, Matchers}

class Day01Test extends FlatSpec with Matchers {
  "Day01 - solvePart1" should "solve first task" in {
    assert(Day01.solvePart1(List("+1", "+1","+1")) == 3)
  }

  "Day01 - solvePart2" should "solve second task" in {
    assert(Day01.solvePart2(List("+7", "+7", "-2", "-7", "-4")) == 14)
    assert(Day01.solvePart2(List("-6", "+3", "+8", "+5", "-6")) == 5)
  }
}
