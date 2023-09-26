def linearSearchproduct(productList, targetProduct):
  indices = []

  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)

  return indices

# Example usage:
products =["shoes", "boot","Loafer", "shoes", "Sandal", "shoes"]
target = "shoes"
target2 ='apple'
result = linearSearchproduct(products, target)
print(result)

      