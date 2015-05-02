import scala.io.Source

object AlmostPrimeReader {
  def parseFile(path: String): Iterator[AlmostPrimeCase] = {
    Source.fromFile(path)
      .getLines()
      .drop(1)
      .map(_.split(" "))
      .map(array => AlmostPrimeCase(array(0).toInt, array(1).toInt))
  }
}
