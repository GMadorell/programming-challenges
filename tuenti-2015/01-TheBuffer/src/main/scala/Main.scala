import org.apache.commons.io.FilenameUtils

object Main extends App {
  val projectRoot = System.getProperty("user.dir")
  val filesPath = FilenameUtils concat (projectRoot, "files")
  val inputFilePath = FilenameUtils concat (filesPath, "submitInput.txt")
  val outputFilePath = FilenameUtils concat (filesPath, "submitOutput.txt")

  val casesIterator = BufferReader.parseFile(inputFilePath)
  val solutions = casesIterator map BufferSolver.solveCase
  BufferWriter.writeToFile(outputFilePath, solutions)
}
