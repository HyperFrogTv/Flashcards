#libs for listing files
from os import listdir
from os.path import isfile, join

##VARIABLES
flashcard_sets_path = './Sets'
global_flashcard_sets_extension = 'txt'
##VARIABLES


def add_flashcard(flashcard):

# iterator counting lines
    iteration = 0

# open file to count lines
    with open('Database.txt', 'r') as file:
        for line in file:
            pass
            iteration = iteration + 1

# adding new line at the end of file
    with open('Database.txt', 'a') as file:
        line_context = file.write("\n"+str(iteration)+' '+flashcard.word+' '+flashcard.word_meaning)

    return 0



def remove_flashcard(number):
    with open('database.txt', 'w+') as file:
        iterator = 0
        for line in file:
            iterator = iterator+1
            if(number == iterator+1):
                line = ' '
                print('tak')

    return 0


def show_flashcard(number):
    with open('Database.txt', 'r') as file:
        iterator = 0
        for line in file:
            iterator = iterator+1
            if (iterator == number+1):
                print(line)
    return 0





##(finished) - Loads Files to Sets List
# flashcard_sets_path - global variable path to folder
# listWidget - list of names given to flashcard sets
# flashcard_sets_name - list of given names of files (without extension) for example (file1, file2, file3)
def load_flashcard_set(self):

    self.listWidget.clear() #Clear listWidget to not duplicate list

    flashcard_sets_name = [] #List that contain names of files (first to last one in folder)

#for loop that goes threw folder in->(flashcard_sets_path) and adds name to list
    for i in listdir(flashcard_sets_path):
        if (isfile(flashcard_sets_path + '/' + str(i))) and i.endswith('.txt'):
            flashcard_sets_name.append(i[:-4])

#for loop that shows names of sets to user in listWidget
    for i in range(len(flashcard_sets_name)):
            self.listWidget.addItem(str(flashcard_sets_name[i]))
    self.listWidget.repaint()



