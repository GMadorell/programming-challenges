import org.scalatest.{Matchers, FlatSpec}

class PrimesTest extends FlatSpec with Matchers {
  "isPrime" should "return true for prime numbers" in {
    Primes.isPrime(2) should be (true)
    Primes.isPrime(3) should be (true)
    Primes.isPrime(5) should be (true)
    Primes.isPrime(7) should be (true)
    Primes.isPrime(211) should be (true)
    Primes.isPrime(3083) should be (true)
    Primes.isPrime(3571) should be (true)
  }

  it should "return false for non-prime numbers" in {
    Primes.isPrime(4) should be (false)
    Primes.isPrime(6) should be (false)
    Primes.isPrime(8) should be (false)
    Primes.isPrime(9) should be (false)
    Primes.isPrime(10) should be (false)
  }
}
