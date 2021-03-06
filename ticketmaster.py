###########
# IMPORTS
###########
import sys
############
# GLOBAL VARIABLES
############
global screen_one
global screen_two
global screen_three
global screen_four
global screen_five
############
# HELPER METHODS
############
def set_movie_list():
    ##########
    # allows the user to enter a list of movies for each screen
    # can only do this before starting the day because it doesn't really make sense otherwise
    # if i had more time i'd let one edit this but i think i should probably go ahead and turn this in
    ##########
    # user selects a screen and inputs movies for that screen until finished
    movie_list = [[], [], [], [], []]
    #movie_list = [['1.1', '1.2', '1.3'], ['2.1', '2.2', '2.3'], ['3.1', '3.2', '3.3'], ['4.1', '4.2', '4.3'], ['5.1', '5.2', '5.3']]
    print("Good morning! Enter today's movies.")
    print("Select a screen to begin. (Q to go back)")
    print("1. Screen One 2. Screen Two 3. Screen Three 4. Screen Four 5. Screen Five")
    user_input = input(">")
    while user_input.upper() != "Q":
        #are there more efficient ways to do this? yes. are we doing those? no.
        match user_input:
            case "1":
                print("Screen One selected.")
                user_input = input("Movie title: ")
                while user_input.upper() != "Q":
                    movie_list[0].append(user_input)
                    user_input = input("Movie title: ")
            case "2":
                print("Screen Two selected.")
                user_input = input("Movie title: ")
                while user_input.upper() != "Q":
                    movie_list[1].append(user_input)
                    user_input = input("Movie title: ")
            case "3":
                print("Screen Three selected.")
                user_input = input("Movie title: ")
                while user_input.upper() != "Q":
                    movie_list[2].append(user_input)
                    user_input = input("Movie title: ")
            case "4":
                print("Screen Four selected.")
                user_input = input("Movie title: ")
                while user_input.upper() != "Q":
                    movie_list[3].append(user_input)
                    user_input = input("Movie title: ")
            case "5":
                print("Screen Five selected.")
                user_input = input("Movie title: ")
                while user_input.upper() != "Q":
                    movie_list[4].append(user_input)
                    user_input = input("Movie title: ")
            case _:
                print("Invalid input.")
        print("1. Screen One 2. Screen Two 3. Screen Three 4. Screen Four 5. Screen Five")
        user_input = input(">")
    return movie_list
def setup_sales(movie_list):
    ########
    #i'm assuming the requirements are intentionally vague so we're just doing
    # this the way i think it should probably be done
    # five screens, each showing a certain subset of movies and a certain number
    # of seats for each
    # it is much easier to assume that a movie will only be shown on one screen
    # begins the sales day
    # @param movie_list - the array generated by set_movie_list
    #########
    screen_one = []
    screen_two = []
    screen_three = []
    screen_four = []
    screen_five = []
    movies = []

    #add movies to screens based on today's set_movie_list
    #each theoater has a set number of seats in it
    for movie in movie_list[0]:
        screen_one.append([movie, 35])
    for movie in movie_list[1]:
        screen_two.append([movie, 40])
    for movie in movie_list[2]:
        screen_three.append([movie, 20])
    for movie in movie_list[3]:
        screen_four.append([movie, 50])
    for movie in movie_list[4]:
        screen_five.append([movie, 55])

    #movie no longer looks like a word
    count_sales([screen_one, screen_two, screen_three, screen_four, screen_five])

def print_selections(screens):
    #######
    # ideally prints every movie with a number in front of it for selection purposes
    # @param screens - array of screens provided by setup_sales to count_sales
    #######
    for i in range(0, len(screens)):
        print("Screen " + str(i+1) + ":")
        j = 1
        for movie in screens[i]:
            print(str(j) + ". " + movie[0] + ", " + str(movie[1]) + " seats remaining")
            j+= 1

def count_sales(screens):
    ###########
    # I'm assuming that this program is being used by employees and not customers
    # (cause if customers can see this there's hella security issues)
    # and employees are capable of learning how to key in codes
    # @param screens - array of screen data provided by setup_sales
    ############
    user_input = ""
    while user_input.upper() != "CLOSE":
    # in a loop
        #print movie selection
        print_selections(screens)
        #accept input (including close command)
        #user should enter a key value pair like 1,2 corresponding to screen and movie
        user_input = input("Select movie. >")
        if user_input.upper() != "CLOSE":
            screen, item = user_input.split(",")
            #avoiding index out of bounds exceptions
            if int(screen)-1 > len(screens):
                print("Invalid input.")
            elif int(item)-1 > len(screens[int(screen)-1]):
                print("Invalid input.")
            else:
                #decrease remaining seats for that screening
                seats = input("Input number of tickets (q to cancel)>")
                if seats.upper() != "Q":
                    if int(seats) > screens[int(screen)-1][int(item)-1][1]:
                        print("That number of seats is unavailable.")
                    else:
                        screens[int(screen)-1][int(item)-1][1] -= int(seats)
    if user_input.upper() == "CLOSE":
        user_input = input("Are you sure you want to close sales for the day? This cannot be undone. (Y/N)")
        if user_input.upper() == "N":
            count_sales(screens)
        elif user_input.upper() == "Y":
            #if closed
            #print sales writeup
            print("Closing sales.")
            print("Generating report...")
            #this could also technically be done more efficiently
            #but it would require more data storage
            #if i had more time i'd probably revamp a lot of this
            print("Screen One")
            for movie in screens[0]:
                print(movie[0] + " sold " + str(35-movie[1]) + " tickets")
            print("Screen Two")
            for movie in screens[1]:
                print(movie[0] + " sold " + str(40-movie[1]) + " tickets")
            print("Screen Three")
            for movie in screens[2]:
                print(movie[0] + " sold " + str(20-movie[1]) + " tickets")
            print("Screen Four")
            for movie in screens[3]:
                print(movie[0] + " sold " + str(50-movie[1]) + " tickets")
            print("Screen Five")
            for movie in screens[4]:
                print(movie[0] + " sold " + str(55-movie[1]) + " tickets")
            sys.exit()
        else:
            #panic
            print("Invalid input.")

#############
# MAIN
#############
def main():
    print("Ticket Manager v1.0.3")
    #don't ever do this but this is where we are today
    user_input = "HELP"
    movies = []
    while user_input != "QUIT":
        match user_input:
            case "START":
                setup_sales(movies)
            case "SWAP":
                movies = set_movie_list()
                #print(movies)
            case "HELP":
                print("Hello, please input one of the following commands:")
                print("START - begin sales for the day")
                print("SWAP - set today's movie list")
                print("HELP - reprint list of commands")
                print("QUIT - exit program")
            case "QUIT":
                #exit program
                break
            case _:
                print("Invalid command, please try again")
        user_input = input(">>").upper()
    sys.exit()

if __name__ == '__main__':
    main()
