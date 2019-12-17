package com.aoc.y2019

object Day01 extends Base2019[List[Int], Int, Int] {

  override val input: List[Int] = getInputFile map {
    _.toInt
  }

  def get_fuel(mass: Int): Int = (mass / 3) - 2

  override def solvePart1(input: List[Int]): Int = {
    input.map(get_fuel).reduceLeft(_ + _)
  }

  override def solvePart2(input: List[Int]): Int = {
    def rec(mass: Int, total: Int = 0, f: Int => Int = get_fuel): Int = {
      val fuel = f(mass)
      if (fuel < 0) total
      else rec(fuel, total + fuel, f)
    }

    input.map(rec(_)).reduceLeft(_ + _)
  }
}
