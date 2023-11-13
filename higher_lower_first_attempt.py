#from game_art import logo, vs
import random
from game_data_test import data

data_copy = data[:]  # copy data list
current_score = 0     # initialize score
first_time = True  # initialize both random seletions
picked_list = []  # keep track of picked selections from list
correct = True
remaining = len(data_copy)

def generate_a():
    A_random_index = random.randint(0,len(data_copy)-1)
    picked_list.append(A_random_index)
    #print(picked_list)
    #print(data_copy[A_random_index]['name'])
    A_name  = (data_copy[A_random_index]['name'])
    A_follower_count  = (data_copy[A_random_index]['follower_count'])
    A_description = (data_copy[A_random_index]['description'])
    A_country = (data_copy[A_random_index]['country'])
    
    #del data_copy[A_random_index]
    return A_name, A_follower_count, A_description, A_country, A_random_index

def generate_b():
    B_random_index = random.randint(0,len(data_copy)-1)
    while B_random_index in picked_list:
        B_random_index = random.randint(0,len(data_copy)-1)
    picked_list.append(B_random_index)    
    #remove entry from list so it doesn't get picked again
    #print(data_copy[B_random_index]['name'])
    #del data_copy[B_random_index]
    #print(len(data_copy))
    B_name  = (data_copy[B_random_index]['name'])
    B_follower_count  = (data_copy[B_random_index]['follower_count'])
    B_description = (data_copy[B_random_index]['description'])
    B_country = (data_copy[B_random_index]['country'])
    return B_name, B_follower_count, B_description, B_country, B_random_index
    
def compare(A_random_index,B_random_index):
    higher = ''
    print(f"A followers: {(data_copy[A_random_index]['follower_count'])}") 
    print(f"B followers: {(data_copy[B_random_index]['follower_count'])}")
    if (data_copy[A_random_index]['follower_count']) > (data_copy[B_random_index]['follower_count']):
        higher = 'A'
    else:
        higher = 'B'
    return higher


def good_choice(score):
    #clear()
    #print(logo)
    print(f"Your're right! Current score: {score}.")
    
def bad_choice(score):
    #clear()
    #print(logo)
    print(f"Sorry, that's wrong. Final score: {score}.")
    
def ask_question(first_time):    
    #print(logo)
    if first_time == True:
        A_name, A_follower_count, A_description, A_country, A_random_index = generate_a()
    else:
        A_name, A_follower_count, A_description, A_country, A_random_index
    print(f"Compare A: {A_name}, {A_description}, from {A_country}.")
    B_name, B_follower_count, B_description, B_country, B_random_index = generate_b()
    #print(vs)
    print(f"Compare B: {B_name}, {B_description}, from {B_country}.")
    
    choice = input("Who has more followers? Type 'A' or 'B': ")
    first_time = False    
    return A_random_index,B_random_index, choice

def execute_test(score):
    #remaining = len(data_copy)
    A_value, B_value, choice = ask_question(first_time)

    higher = compare(A_value,B_value)

    if choice == 'A' and higher == 'A':
        score += 1
        good_choice(current_score + score) #print("Correct")
        #generate_b()  # generate new B
        #compare()  #compare
        is_correct = True
    elif choice == 'B' and higher == 'B':
        score += 1
        good_choice(current_score + score) #print("Correct")
        is_correct = True
        #A_random_index = B_random_index  # swap A with B
        #generate_b()  #generate new B
    else:
        bad_choice(current_score) #print("Incorrect")
        is_correct = False
    remaining = len(data_copy) - len(picked_list)
    return is_correct, remaining, score

while correct == True and remaining > 1:
    correct, remaining, score = execute_test(current_score)
    current_score += score
    