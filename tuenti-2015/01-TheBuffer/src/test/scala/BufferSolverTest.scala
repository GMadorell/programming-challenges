import org.scalatest.{Matchers, FlatSpec}

class BufferSolverTest extends FlatSpec with Matchers {
  it should "return the correct value" in {
    BufferSolver solveCase 1 should be (1)
    BufferSolver solveCase 2 should be (1)
    BufferSolver solveCase 3 should be (2)
    BufferSolver solveCase 4 should be (2)
    BufferSolver solveCase 5 should be (3)
  }
}
