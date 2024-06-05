txt = "******************** WELCOME TO THE HARSHIT'S KAUN BANEGA CROREPATI ********************"
x = txt.center(50)
print(x)
print("Enter Your Full Name: ")
fname = input("Enter your First Name: ")
lname = input("Enter your Last Name: ")
print("Hello " + fname + " "+lname + "!")
print("Let's Start the \"HARSHIT'S KAUN BANEGA CROREPATI\".")
#print("Hello " + name +" Let's play the Game!" )


# There We ae using list for this 
question_name = ["Your First Question Display on your Computer Screen.", "Your Second Question Display on your Computer Screen.", "Your Third Question Display on your Computer Screen.", "Your Fourth Question Display on your Computer Screen.", "Your Fifth Question Display on your Computer Screen.", "Your Sixth Question Display on your Computer Screen.", "Your Seventh Question Display on your Computer Screen.", "Your Eight Question Display on your Computer Screen.", "Your Ninth Question Display on your Computer Screen.", "Your Tenth Question Display on your Computer Screen.",]
question_list = ["1. What is the Capital of India?" , "2. Which city known as a \"The Pink City Of India\"?" , "3. Who written \"The National song of India\" and When it was written?", "4. Who is The Prime Minister of Italy?" , "5. Who is The First Indian Female won Miss Universe and when?", "6. When India won its first ODI Cricket world cup and under whose Captaincy?", "7. Who is the Former President of Board of Control for Cricket in India?", "8. Who is the Former President of United States of America?", "9. Who is the Father of Computer?", "10. who is the first book of the Rabindranath Tagore?"]
first_option = ["a. Rajasthan" , "a. Shimla" , "a. Bankim Chandra Chattterjee in 1882" , "a. Narendra Damodardas Modi" , "a. Sushmita Sen on May 21, 1994" , "a. In 2011 Under the leadership of Mahendra Singh Dhoni","a. Sourav Ganguly", "a. Joe Biden", "a. Joseph Marie Charles", "a. Waiting"] 
second_option = ["b. Delhi" , "b. Manipur" , "b. Rabindranath Tagore in 1927" ,"b. Rahul Gandhi" , "b. Lara Dutta on July 25,2000", "b. In 1983 Under the leadership of Kapil Dev", "b. Roger Binny", "b. Donald Trump", "b. Alan Turing", "b. The Post Office"]
third_option = ["c. Uttar Pardesh" , "c. Jaipur" , "c. Harshit Veram in 2023" , "c. Andrea Giambruno" , "c. Priyanka Chopra on Aug 19, 2002", "c. In 2019 Under the leadership of Virat Kohli", "c. Vangipurapu Venkata Sai Laxma", "c. Barack Obama", "c. Herman Hollerith", "c. Bhikharini(\"The Beggar Woman\")"]
fourth_option = ["d. Assam" , "d. Shastri Nagar" , "d. Debendranath Tagore in 1950" ,"d. Giorgia Meloni" , "d. Manushi Chhillar on Sep 20, 2022", "d. In 1983 Under the leadership of Sourav Ganguly", "d. Jay Shah", "d. None of These", "d. Charles Babbage", "d. Gitanjali"]

# all_options - [first_option , secound_option , third_option  ,fourth_option]

ans_key = ["b", "c", "a", "d", "a", "b", "b", "a", "d", "c"]
ans_list = []
correct_answer = 0







price = [1000000 , 2000000 , 3000000 , 4000000 , 5000000 , 6000000 , 7000000 , 8000000 , 9000000 , 10000000]        #money of all answer

a= 0
padav = 1

# this is the main loop of Program 
# and here we use the While loop

while a < len(question_list):
    print(question_name[a])
    print(question_list[a])
    print(first_option[a])
    print(second_option[a])
    print(third_option[a])
    print(fourth_option[a])

    user = input("Enter your answer. ")
    if user == ans_key[a]:
        print("Congratulations! Your Answer is Right, You won:" , price[a])
        print("")
        correct_answer = 1
    else:
        print(f"Sorry! {fname} {lname}, Your Answer is wrong.")
        print("Better Luck Next Time!")
        print("GAME OVER")
        print("")
        break

    a = a+1
    if a%5 == 0:
        print("Congratulations! Yor are completed the first Round and entering in the second Round." , padav)
        print("")
        padav = padav + 1
    ans_list.append(user)   
        # print(len(question_list[a]))
# def Greetings():
#     print(f"Congratulations! {fname} {lname} You Win The \"HARSHIT'S KAUN BANEGA CROREPATI\".")
#     print("Your Win the Price Money 10000000. We will tranfer in your account as soon as possible")
#     print("Good Bye")
# print(Greetings)





