import scala.io.Source

object BufferReader {
  def parseFile(path: String): Iterator[Long] = {
    Source.fromFile(path)
      .getLines()
      .drop(1)
      .map(_.toLong)
  }
}
