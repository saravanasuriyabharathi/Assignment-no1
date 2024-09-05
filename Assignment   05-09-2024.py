def collect_inputs():
    # This list is used to store user input data 
    inputs = []
    print("If you Enter exit program will stop getting value")
    # This loop is used to get the input form the user
    
    while (True):
        
        user_input =input("Enter the input: ")
        if user_input.lower() == 'exit':
            break
        inputs.append(int(user_input))
    
    print("Your listed Inputs:")
    for item in inputs:
        print(item)
    if inputs:# Ensure the list is not empty
        
        # the below line is used to collect the return value form the calculate function
        #we can say the below line as the function call.
        
        min_value, max_value, total_sum = calculate(inputs)
        
        # The below statnemnt are used to print the min,max and sum value
        
        print("Minimum value:", min_value)
        print("Maximum value:", max_value)
        print("Sum of values:", total_sum)

# This is the function to calculate the min,max and sum

def calculate(numbers):
    """Return the minimum, maximum, and sum of the list of inputs that given in the above function ."""
    
    min_value = min(numbers)
    max_value = max(numbers)
    total_sum = sum(numbers)
    
    # the below return statement is used to return the values to the function called place
    
    return min_value, max_value, total_sum

#The below line is used to call the funtion

collect_inputs()
    
    
