package aoc

import scala.util.parsing.combinator.RegexParsers

object Day01 extends Base2018[List[String], Int, Int] with RegexParsers {

  override val input: List[String] = getInputFile

  val pattern = "([+-])([0-9]+)".r

  def get_sign(s: String) : Int  = {
    val pattern(sign, n) = s
    if (sign == "+") + n.toInt
    else - n.toInt
  }

  override def solvePart1(input: List[String]) : Int = {
    input.map(get_sign).reduceLeft(_ + _)
  }

  override def solvePart2(input: List[String]): Int = {
    0
  }
 }
