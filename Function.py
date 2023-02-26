#function declaration
def function_name(name):
    print("welcome to phython class"+name)
    print("function is completed here.")

#declaring another function
def Menu():
    name=input("What is your name : ")
    food=input("What would u like to have in food : ")
    dessert= input("What do u want to in dessert : ")
    drink=input("What you like to have in drink : ")
    print(name +" : I woule like "+food+ " I want to drink "+drink+" i want "+dessert+" as a dessert")

#function call
function_name("Rohit")
Menu()