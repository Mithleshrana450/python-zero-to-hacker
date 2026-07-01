# Take a price as string
# input like "249.99" — cast it to float, add 18% GST to it, print the final price.
price = ("249.99")
print(float(price))
final_price = float(price) + (float(price) * 0.18)
print("Final price is: ", final_price)