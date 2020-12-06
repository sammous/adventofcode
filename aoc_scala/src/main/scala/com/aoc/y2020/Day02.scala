package com.aoc.y2020

object Day02 extends Base2020[List[String], Int, Int] {

  override val input: List[String] = getInputFile
  def validatePassword(entry: String): Int = {
    val entrySplit = entry.split(": ")
    val (policy, password) = (entrySplit(0), entrySplit(1))
    val policyCount = policy.split(" ")(0).split("-") map { _.toInt }
    val occ = password.count(_ == policy.split(" ")(1).charAt(0))
    if (occ >= policyCount(0) && occ <= policyCount(1)) { return 1 }
    else { return 0 }
  }
  override def solvePart1(input: List[String]): Int = {
    input.map(validatePassword).reduce(_ + _)
  }
  def validatePasswordIndex(entry: String): Int = {
    var sum = 0
    val entrySplit = entry.split(": ")
    val (policy, password) = (entrySplit(0), entrySplit(1))
    val policyIndexes = policy.split(" ")(0).split("-") map { _.toInt }
    val occ = policyIndexes
      .foreach(i => {
        if (password.charAt(i - 1) == policy.split(" ")(1).charAt(0)) sum += 1
      })
    if (sum == 1) return 1
    else return 0
  }
  override def solvePart2(input: List[String]): Int = {
    input.map(validatePasswordIndex).reduceLeft(_ + _)
  }
}
