import org.scalatest.{Matchers, FlatSpec}

class AlmostPrimeCaseSolverTest extends FlatSpec with Matchers {
  it should "return the amount of almost prime numbers in the case interval" in {
    AlmostPrimeCaseSolver.solve(AlmostPrimeCase(1, 10)) should be (4)
    AlmostPrimeCaseSolver.solve(AlmostPrimeCase(10, 20)) should be (3)
  }
}
