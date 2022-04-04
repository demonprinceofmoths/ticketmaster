###########
# IMPORTS
###########
import sys
############
# GLOBAL VARIABLES
############
############
# HELPER METHODS
############
def set_movie_list():
    # user selects a screen and inputs movies for that screen until finished
    movie_list = [[], [], [], [], []]
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
            case "CLOSE":
                #print the report
                print("Closing")
            case "HELP":
                print("Hello, please input one of the following commands:")
                print("START - begin sales for the day")
                print("SWAP - set today's movie list")
                print("CLOSE - close sales for the day")
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
