package aoc
import scala.io.Source
import scala.util.Try
import java.io.FileNotFoundException

trait Base[I, Part1, Part2] {
  val input : I
  val year: String
  val day: String = this.getClass.getSimpleName.takeRight(2)

  def getInputFile: List[String] = Source.fromResource(s"y$year/day$day.txt").getLines.toList
  def solvePart1(input: I): Part1
  def solvePart2(input: I): Part2


  def main(args: Array[String]): Unit = {
    println(s"[1st star] ${solvePart1(input)}")
    println(s"[2nd star] ${solvePart2(input)}")
  }
}