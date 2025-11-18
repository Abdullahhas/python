# Write a genrator function that yields even numbers up to a specificed limit

# generators me function pause ho jata he or apni current state ko store kar lta he , next value bhr bej deta he or jab next value chaye hti he to wahi se reume ho jata he
# multiple values ik ik kar ke deta he
# memory save hti he
# Large sequences generate karne ke liye best


#Example: 1 to 1 Billion Even Numbers
# Return function → RAM crash
# Generator function → Easily work karega, kyunki ek time per sirf ek number generate hota hai

def even_generator(limit):
    for i in range(2,limit+1 , 2) :
        yield i

for num in even_generator(10):
    print(num)