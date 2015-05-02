import org.scalatest.{Matchers, FlatSpec}

class PrimeFactorsTest extends FlatSpec with Matchers {
  "primeFactors" should "return a list with the same number if the given number is prime" in {
    PrimeFactors.primeFactors(2) should be (List(2))
    PrimeFactors.primeFactors(3) should be (List(3))
    PrimeFactors.primeFactors(5) should be (List(5))
    PrimeFactors.primeFactors(7) should be (List(7))
    PrimeFactors.primeFactors(17) should be (List(17))
  }

  it should "return a list with the prime factors for non-prime numbers" in {
    PrimeFactors.primeFactors(4) should be (List(2, 2))
    PrimeFactors.primeFactors(6) should be (List(2, 3))
    PrimeFactors.primeFactors(25) should be (List(5, 5))
    PrimeFactors.primeFactors(81) should be (List(3, 3, 3, 3))
  }
}
