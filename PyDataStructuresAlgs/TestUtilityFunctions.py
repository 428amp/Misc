def timeExecution(fn, input):
  start_time = time()
  fn(input)
  end_time = time()
  return end_time - start_time
