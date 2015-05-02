
object AlmostPrimeCaseSolver {
  def solve(almostPrimeCase: AlmostPrimeCase): Int = {
    List.range(almostPrimeCase.minRange, almostPrimeCase.maxRange + 1)
      .count(isNumberAlmostPrime)
  }

  private var cache = Map[Int, Boolean](1 -> false)
  private var alreadyDiscardedNumbers = List[Int]()
  def isNumberAlmostPrime(n: Int): Boolean = {
    if (! cache.contains(n)) {
      val isMultipleOfDiscardedNumber = isMultipleWithAnyDiscardedNumber(n)
      lazy val hasTwoPrimeFactors = PrimeFactors.hasExactlyTwoPrimeFactors(n)
      val isAlmostPrime = !isMultipleOfDiscardedNumber && hasTwoPrimeFactors
      cache += (n -> isAlmostPrime)
      if (!isAlmostPrime && (isMultipleOfDiscardedNumber || hasTwoPrimeFactors)) {
        alreadyDiscardedNumbers = n :: alreadyDiscardedNumbers
      }
    }
    cache(n)
  }

  def isMultipleWithAnyDiscardedNumber(n: Int): Boolean = {
    alreadyDiscardedNumbers.exists(n % _ == 0)
  }
}
