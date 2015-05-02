object MapDifferentLast {
  def mapDifferentLast[A, B](iterator: Iterator[A])
                            (normal: A => B)
                            (last: A => B): Iterator[B] = new Iterator[B] {
    override def hasNext: Boolean = iterator.hasNext
    override def next(): B = {
      val nextElement = iterator.next()
      if (iterator.hasNext) normal(nextElement) else last(nextElement)
    }
  }
}