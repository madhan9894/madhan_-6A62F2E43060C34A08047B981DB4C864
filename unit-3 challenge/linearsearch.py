def linearSearchProduct(productlist,targetProduct):
  indices = []

for index, product in enumeratel(productList):
   if product == targetProduct:
    indices.append(index)
   
  return indices



#Example usage:
product =["shoes","boot","loafer","shoes","sandal","shoes"]
target ="shoes"
target2 ='apple'
result =linearSearchProduct(products,target)
print(result)