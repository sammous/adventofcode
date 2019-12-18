package com.aoc.y2019

object Day02 extends Base2019[List[Int], Int, Int] {

  override val input: List[Int] = {
    getInputFile.head.split(",").toList.map(_.toInt).toList
  }

  def rec(input: Array[Int], index: Int): List[Int] = {
    input(index) match {
      case 99 => input.toList
      case 1 =>
        rec(
          input.updated(
            input(index + 3),
            input(input(index + 1)) + input(input(index + 2))
          ),
          index + 4
        )
      case 2 =>
        rec(
          input.updated(
            input(index + 3),
            input(input(index + 1)) * input(input(index + 2))
          ),
          index + 4
        )
    }
  }
  override def solvePart1(input: List[Int]): Int =
    rec(input.toArray.updated(1, 12).updated(2, 2), 0).head

  override def solvePart2(input: List[Int]): Int = {
    for {
      noun <- 0 to 99
      verb <- 0 to 99
      if rec(input.toArray.updated(1, noun).updated(2, verb), 0).head == 19690720
    } yield { 100 * noun + verb }
  }.head
}
