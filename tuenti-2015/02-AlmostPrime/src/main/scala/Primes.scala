
object Primes {
  def isPrime(n: Int): Boolean = {
    if (n <= 1) {
      false
    } else if (n == 2) {
      true
    } else {
      Iterator.range(2, Math.sqrt(n).toInt + 1) forall (n % _ != 0)
    }
  }

  def getNextPrimeOf(n: Int): Int = {
    var prime = n
    do {
      prime += 2
    } while (!Primes.isPrime(prime))
    prime
  }
}
