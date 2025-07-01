import random

def resultPrint(Indian_subjects, Indian_actions, Indian_places):
    flag = True
    while flag:
        random_subject = random.choice(Indian_subjects)
        random_action = random.choice(Indian_actions)
        random_place = random.choice(Indian_places)
        result = f"BREAKING: {random_subject} {random_action} {random_place}"
        print(result)
        users = input("You wanna save this headline in some file? ")
        if users == "yes":
            with open("../FakeHeadlineGenerator/fakeheadlines.txt", "a") as file:
                file.write(result)
                file.write("\n")
        else:
            user = input("Wanna generate another headline: (yes/no)?")
            if user == "yes":
                flag = True
            else:
                print("Goodbye..")
                flag = False

def main():
    Indian_subjects = ["Sharukh khan", "Virat Kohli", "Nirmala Sitharaman", "A Mumbai cat", "A group of Monkey"]
    Indian_actions = ["launches", "cancels", "dances with", "eats", "declares war on"]
    Indian_places = ["at Red fort", "in Mumabi local train", "a plate of samosas", "inside parliment", "at Ganga ghat"]
    resultPrint(Indian_subjects, Indian_actions, Indian_places)


if __name__ == "__main__":
    main()
