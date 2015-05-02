
import org.apache.commons.io.FilenameUtils

object Main extends App {
  val projectRoot = System.getProperty("user.dir")
  val filesPath = FilenameUtils concat (projectRoot, "files")
  val inputFilePath = FilenameUtils concat (filesPath, "testInput.txt")
  val outputFilePath = FilenameUtils concat (filesPath, "testOutput.txt")

  val casesIterator = AlmostPrimeReader.parseFile(inputFilePath)
  val solutions = casesIterator map AlmostPrimeCaseSolver.solve
  AlmostPrimeWriter.writeToFile(outputFilePath, solutions)
}
