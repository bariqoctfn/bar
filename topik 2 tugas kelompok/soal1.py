def calculate_average(numbers):
  try:
      total = sum(numbers)
      average = total / len(numbers)
      return average
  except ZeroDivisionError:
      print("Error: angka tidak boleh 0")
try:
  result = calculate_average("string") #input yang benar adalah list
  print(result)
except:
  print("masukkan harus sebuah list")
