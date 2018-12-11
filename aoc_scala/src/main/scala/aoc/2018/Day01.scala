package aoc

object Day01 extends Base2018[List[String], Int, Int] {

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
    def loop(l: List[Int]) : Int = {
      l.diff(l.distinct).distinct.length match {
        case 0 => loop(l.dropRight(1) ++ input.map(get_sign).scanLeft(l.last)(_ + _))
        case x => l.diff(l.distinct).distinct.head
      }
    }

    loop(l=input.map(get_sign).scanLeft(0)(_ + _))
  }

}
