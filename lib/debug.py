# #!/usr/bin/env python3
# import ipdb;
 


# if __name__ == '__main__':
# #  WRITE YOUR TEST CODE HERE ###









# # DO NOT REMOVE THIS
#     ipdb.set_trace()

#!/usr/bin/env python3
import ipdb
from Customer import Customer
from Restaurant import Restaurant
from Review import Review

if __name__ == '__main__':
    
    customer1 = Customer("John", "Doe")
    customer2 = Customer("Jane", "Smith")

    
    restaurant1 = Restaurant("Restaurant A")
    restaurant2 = Restaurant("Restaurant B")

    
    review1 = Review(customer1, restaurant1, 4)
    review2 = Review(customer2, restaurant1, 5)
    review3 = Review(customer1, restaurant2, 3)

     
    customer1.add_review(restaurant1, 4)
    customer2.add_review(restaurant1, 5)
    customer1.add_review(restaurant2, 3)

     
    print(restaurant1.name())   
    print(restaurant1.reviews())   
    print(restaurant1.customers())  
    print(restaurant1.average_star_rating())   

    print(customer1.full_name())   
    print(customer1.restaurants())   

     
    ipdb.set_trace()

