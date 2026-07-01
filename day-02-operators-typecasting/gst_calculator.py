# Take a price as string
# input like "249.99" — cast it to float, add 18% GST to it, print the final price.

price = input("Enter price:")
print(float(price))
gst = float(price) * 0.18
final_price = float(price) + gst
print("Final price is: ", final_price)