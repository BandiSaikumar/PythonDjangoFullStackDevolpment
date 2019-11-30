zoo = ['lion', "elephant", 'monkey']

if __name__ == "__main__":
    f = open("output.txt","w")

    for i in zoo:

        # add the whole zoo to the output.txt
        f = open("output.txt","w")
        f.write("Contents\n")
        f.write("Lion--Elephant--Monkey--Tiger--Donkey")
    f.close()