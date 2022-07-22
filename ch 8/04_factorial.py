# n!=1*2*3*4*5*...*n
# n!=1*2*3*4*5*... *(n-1)*n
# n!=n*(n-1)!
# n=5
# product=1
# for i in range(n):
#     product=product*(i+1)
    
# print(product)

# function
# n=5
def factorial_iter(n):
    product=1
    for i in range(n):
        product=product*(i+1)
    return product


# facroial_recursive
def factorial_recursive(n):
    if n==1 or n==0:
        return 1
    return n*factorial_recursive(n-1)
    


# f=factorial_iter(5)
f=factorial_recursive(4)
print(f)
