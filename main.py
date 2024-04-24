def sum_numbers():
  try:
      # Asks for beginning and ending numbers
      start_num = int(input("Enter the beginning number: "))
      end_num = int(input("Enter the ending number: "))

      # Checks if numbers are positive
      if start_num <= 0 or end_num <= 0:
          print(f"Only positive integers are allowed. Either \"{start_num}\" or \"{end_num}\" is not positive.")
          return

      # Checks if the ending number is higher than the beginning number
      if end_num <= start_num:
          print(f"The second number \"{end_num}\" cannot be smaller than or equal to the first number \"{start_num}\"")
          return

      # Calculate the sum and display the process
      total = start_num
      for i in range(start_num + 1, end_num + 1):
          print(f"++ {total} + {i} = {total + i}")
          total += i

      print(f"Your result is {total}.")

  except ValueError:
      # what happens if a non int is entered 
      print("Only positive integers are accepted, the provided input does not seem to be an integer.")

# Call the function
sum_numbers()