how_many_snakes = 1
snake_string = ("\n"
                "Welcome to Python3!\n"
                "\n"
                "             ____\n"
                "            / . .\\\n"
                "            \  ---<\n"
                "             \  /\n"
                "   __________/ /\n"
                "-=:___________/\n"
                "\n"
                "<3, Juno\n")

print(snake_string * how_many_snakes)

# to read a file
f = open('name.txt', 'r')
file_data = f.read()
print(file_data)
f.close()

# to write in a file
f = open('name.txt', 'w')
file_data = f.write("this is scripting in python.")
print(file_data)
f.close()


'''Importing Local Scripts.
We can actually import Python code from other scripts, which is helpful if you are working on a bigger project where you want to organize your code into multiple files and reuse code in those files'''
