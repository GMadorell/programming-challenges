import java.io.{FileOutputStream, OutputStreamWriter, BufferedWriter}
import MapDifferentLast._

object BufferWriter {
  def writeToFile(path: String, solutions: Iterator[Long]) = {
    val writer = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(path)))
    mapDifferentLast(solutions.map(String.valueOf))(_ + "\n")(identity)
      .foreach(writer.write)
    writer.close()
  }
}
