package com.aoc.y2020

object Day01 extends Base2020[List[Int], Int, Unit] {

  override val input: List[Int] = getInputFile map {
    _.toInt
  }

  def rec(input: List[Int], value: Int, toFind: Int = 2020): List[Int] = {
    input.length match {
        case 0 => return List.empty
        case _ => {
            input.foreach( l => {
                if ((l + value) == toFind) return List(l, value)
            })
            return rec(input.tail, input.head)
        }
    } 
  }

  override def solvePart1(input: List[Int]): Int = {
    val l = rec(input.tail, input.head)
    return (l(0) * l(1))
  }

  override def solvePart2(input: List[Int]): Unit = {}
}
