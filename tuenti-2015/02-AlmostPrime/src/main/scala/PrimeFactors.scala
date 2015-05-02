
object PrimeFactors {
  private var primesList = new PrimesIterator().take(10000).toList.reverse

  def primeFactors(number: Int): List[Int] = {
    require(number > 1, "Prime factors of numbers <= 1 are not supported (and probably don't make sense, too).")
    def primeFactorsR(n: Int, ps: List[Int]): List[Int] =
      if (Primes.isPrime(n)) List(n)
      else if (n % ps.head == 0) ps.head :: primeFactorsR(n / ps.head, ps)
      else primeFactorsR(n, ps.tail)
    ensurePrimesListBigEnough(number)
    primeFactorsR(number, primesList)
  }

  def hasExactlyTwoPrimeFactors(number: Int): Boolean = {
    hasLessThanThreePrimeFactors(number) && primeFactors(number).length == 2
  }

  def hasLessThanThreePrimeFactors(number: Int): Boolean = {
    require(number > 1, "Prime factors of numbers <= 1 are not supported (and probably don't make sense, too).")
    def primeFactorsR(n: Int, ps: List[Int], accum: Int): Boolean =
      if (Primes.isPrime(n)) accum > 0
      else if (n % ps.head == 0) accum - 1 > 0 && primeFactorsR(n / ps.head, ps, accum - 1)
      else primeFactorsR(n, ps.tail, accum)
    ensurePrimesListBigEnough(number)
    primeFactorsR(number, primesList, 2)
  }

  private def ensurePrimesListBigEnough(number: Int) = {
    if (number > primesList.head) primesList = Primes.getNextPrimeOf(primesList.head) :: primesList
  }
}
