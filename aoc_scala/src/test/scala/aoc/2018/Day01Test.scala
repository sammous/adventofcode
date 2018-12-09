package aoc

import org.scalatest.{FlatSpec, Matchers}

class Day01Test extends FlatSpec with Matchers {
  "Day01 - solvePart1" should "solve first task" in {
    assert(Day01.solvePart1(List("+1", "+1","+1")) == 3)
  }
}
