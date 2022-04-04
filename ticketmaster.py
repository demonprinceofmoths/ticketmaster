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
    movie_list = []
    print("Good morning! Enter today's movies, Q to go back...")
    user_input = input("Movie title:")
    while user_input.upper() != "Q":
        movie_list.append(user_input)
        user_input = input("Movie title:")
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
