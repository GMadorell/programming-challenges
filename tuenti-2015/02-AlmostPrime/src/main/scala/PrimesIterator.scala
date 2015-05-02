
class PrimesIterator extends Iterator[Int] {
  var lastPrime: Int = -1
  override def hasNext: Boolean = true
  override def next(): Int = {
    if (lastPrime == -1) lastPrime = 2
    else if (lastPrime == 2) lastPrime = 3
    else lastPrime = Primes.getNextPrimeOf(lastPrime)
    lastPrime
  }
}
