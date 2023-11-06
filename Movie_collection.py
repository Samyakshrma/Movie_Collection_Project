
movies = [
    {"Iron Man": "01 November 2023"},
    {"Avengers": "02 November 2023"}
    ]

def Ui():
    print("Please select what you want to do\n1) View your collection \n2) Add a new movie\n3) Edit existing list")
    print("\n\n4) Exit the application")
    print("Enter your choice : ")
    x = int(input())

    if x == 1:
        for movie in movies:
            for key,value in movie.items():
                print(f"{key} \n _____________\n{value}\n\n")
        Ui()
    elif x == 2:
        movie = input("Enter the new movie you want to add")
        Date = input("Enter the date")
        Genre = input("Enter the genre of the movie")
        Rating = int(input("Enter the rating you want to give to this movie"))
        About = f"Watched this movie on  : {Date} \nMovie belongs to Genre : {Genre}\nrating  : {Rating} Stars "
        movies.append({movie: About})
        print(f"Changes made {movie} added to the list")
        Ui()
    elif x == 3:
        movie = input("Enter the movie you want to edit : ")
        namelist = []
        for i in movies:
            z = list(i.keys())
            for j in z:
                if movie == j:
                    print("Make the changes")
                    Date = input("Enter the date")
                    Genre = input("Enter the genre of the movie")
                    Rating = int(input("Enter the rating you want to give to this movie"))
                    About = f"Watched this movie on  : {Date} \nMovie belongs to Genre : {Genre}\nrating  : {Rating} Stars "
                    i.update({movie:About})
                    print(f"Changes made {movie} added to the list")
                    


        else:
            print(f"You dont have any movie named {movie}")
            Ui()
    elif x == 4:
        print("Thanks for using this application")

    else:
        print(f"Choose a valid option, Please")
        Ui()

Ui()










