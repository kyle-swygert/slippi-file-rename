'''
    Slippi File Renaming Script: Rename Slippi Files based on the characters and in-game tags used
    Filename Specification:
        CharacterName(TAG)-Vs-CharacterName(TAG)<year-month-day-hour-minute-second>.slp

            ex) CaptainFalcon(DOOM)-Vs-Jigglypuff<20191010191914>.slp

        Written by Kyle "1ncredibr0" Swygert
        Using py-slippi v1.3.1
'''

'''

NOTE: there may be a difference when parsing replays captured from a Wii vs a connection to a PC. Make sure that the PC captured replays are parsed the same as the Wii captured files. 

TODO: Rename replays against CPUs using the tag CPU for the character to make sure it is not a human player. 

TODO: generate file that lists the files that caused and error and the error that was caused. 

'''



from slippi import *
from os import walk, listdir, rename, path

def generate_file_name(slippiFile):
    '''
    TODO: create cases in this function in the future to rename files based on the type of game being played. 
        ex) singles, doubles, free for all. 

    if is teams game:
        generate_doubles_game_name()

    else:

        if 2 players in game:
            generate_singles_game_name()

        elif more than 2 players in game:
            # either a 3 or 4 person free for all match. 
            generate_free_for_all_game_name()

    '''
    print('implement the file name function')

    pass

def generate_doubles_game_name(slippiFile):
    '''
    Team Naming Guide Idea: TeamGreen(Falco+(H E L P))-Vs-TeamBlue(CaptainFalcon+(S E L F))_datetime.slp
    TeamColor(char1(TAG)-char2(TAG))-Vs-TeamColor(char3(TAG)-char4(TAG))_datetime.slp
    

    TODO: test the execution of the doubles renaming function. stops executing when hitting (if player.team == firstTeamPlayers[0].team) [Nonetype object has no attribute team]

    TODO: check if any of the players in the game are CPUs. If there are any CPUs, add that in the filename. 

    TODO: improve the try except blocks in the program to further locate where the program is having difficulties executing. 


    '''

    # NOTE: assuming that all doubles games are full, meaning two teams of 2 players each. 

    newFile = ''
    firstTeamPlayers = []
    secondTeamPlayers = []

    firstTeamParts = []
    secondTeamParts = []

    # the team that the player is on is in the Player object of the game file. 

    # TODO: check that there are 4 players in this game. this teams game could be 2v1, which could cause an issue. it also might not cause an issue. 

    # add the first player to the lists. Compare all other players to this player for building the lists of players in the same team. 
    firstTeamPlayers.append(slippiFile.start.players[0])

    for player in slippiFile.start.players[1:]:

        if player != None:

            if player.team == firstTeamPlayers[0].team:
                firstTeamPlayers.append(player)
            else:
                secondTeamPlayers.append(player)


    # players have been separated by team, now build the list of strings for the team names. 

    #firstPlayer = False


    # build the first team list of strings

    # remove the '.' between the team and the color strings. 
    [firstTeamParts.append(item) for item in str(firstTeamPlayers[0].team).split('.')]

    firstTeamParts.append('(')

    for player in firstTeamPlayers:

        if player.tag != '':
            # add only the tag of the player to the filename
            firstTeamParts.append(player.tag)


        else:
            # add only the character name to the filename

            [firstTeamParts.append(item.lower().capitalize()) for item in str(player.character).split('.')[-1].split('_')]

        firstTeamParts.append('-')

    firstTeamParts.pop()


    firstTeamParts.append(')')



    # build the second team list of names
    # remove the '.' between the team and the color strings. 
    [secondTeamParts.append(item) for item in str(secondTeamPlayers[0].team).split('.')]

    secondTeamParts.append('(')

    for player in secondTeamPlayers:

        if player.tag != '':
            # add only the tag of the player to the filename
            secondTeamParts.append(player.tag)


        else:
            # add only the character name to the filename

            [secondTeamParts.append(item.lower().capitalize()) for item in str(player.character).split('.')[-1].split('_')]


        secondTeamParts.append('-')

    secondTeamParts.pop()

    secondTeamParts.append(')')


    # append first team strings to file name
    for item in firstTeamParts:
        newFile += item

    # append '-Vs-' between the team names
    newFile += '-Vs-'

    for item in secondTeamParts:
        newFile += item


    newFile += '_' + str(slippiFile.metadata.date).split('+')[0].replace(' ', '').replace('-', '').replace(':', '').split('.')[0]    



    newFile += '.slp'

    #print('New Doubles match name: {}'.format(newFile))


    #print(firstTeamPlayers)
    #print('\n\n\n\n\n')
    #print(secondTeamPlayers)


    return newFile



def generate_free_for_all_game_name(slippiFile):
    '''
    iterate through all the players in the game
    build a list of strings of the character names and '-Vs-'
    Ex) Fox-Vs-Falco-Vs-Sheik_20191010143456.slp


    '''
    #print('implement the free-for-all function')

    newFile = ''

    # list used to build the new Filename
    newFileNameParts = []

    newFileNameParts.append('FFA_')


    #firstChar = False

    # iterate over players in the game
    for player in slippiFile.start.players:

        # append the formatted character name from the character object to the list
        [newFileNameParts.append(item.lower().capitalize()) for item in str(player.character).split('.')[-1].split('_')] if player != None else None

        # append the player tag to the list if they were using one
        #newFileNameParts.append('(' + player.tag + ')') if player != None and player.tag != '' else None

        # append the '-vs-' string to the list no matter what. 
        newFileNameParts.append('-Vs-') if player != None else None

        
    # remove the redundant '-vs-' string from the list. 
    newFileNameParts.pop()

    # Build the new Filename
    for item in newFileNameParts:
        newFile += item

    # appending the date and time that the game was played to reduce chance of overwriting files
                
    # Could I do list comprehension here to replace the multiple different characters with nothing?
    # NOTE: the previous format of <date>.slp is not allowed on the windows platform, so it is now replaced with _date.slp
    newFile += '_' + str(slippiFile.metadata.date).split('+')[0].replace(' ', '').replace('-', '').replace(':', '').split('.')[0] #  + '_'

    newFile += '.slp'

    #print(newFile)

    return newFile


def generate_singles_game_name(slippiFile):
    '''
    this function will build a string based on the characters used in the game. 

    '''

    newFile = ''

    # list used to build the new Filename
    newFileNameParts = []

    firstChar = False

    # iterate over players in the game
    for player in slippiFile.start.players:


        # NOTE: this CPU player check is causing the program to execute improperly. figure out why and how to append the 'CPU' string to the list of strings. I removed the statements entirely to get rid of the issue. 

        # append the formatted character name from the character object to the list
        [newFileNameParts.append(item.lower().capitalize()) for item in str(player.character).split('.')[-1].split('_')] if player != None else None

        # append the player tag to the list if they were using one
        newFileNameParts.append('(' + player.tag + ')') if player != None and player.tag != '' else None

        # append '-Vs-' string to list if this is the first player being added to the list
        if newFileNameParts != [] and firstChar == False:
            firstChar = True
            newFileNameParts.append('-Vs-')


    # Build the new Filename
    for item in newFileNameParts:
        newFile += item

    # appending the date and time that the game was played to reduce chance of overwriting files
                
    # Could I do list comprehension here to replace the multiple different characters with nothing?
    # NOTE: the previous format of <date>.slp is not allowed on the windows platform, so it is now replaced with _date.slp
    newFile += '_' + str(slippiFile.metadata.date).split('+')[0].replace(' ', '').replace('-', '').replace(':', '').split('.')[0] #  + '_'

    newFile += '.slp'

    #print(newFile)

    return newFile


def rename_files_in_folder(folder):
    '''
    this function accepts the name of a folder as a string and will rename all the .slp files in the directory and sub-directories. 
    '''

    print('folder that contains all the slippi files: {}'.format(folder))

    # check that the folder exists in the system. 
    if path.exists(folder) == False:
        print(f'{folder} does not exist in the system')
        return

    print(f'{folder} exists, renaming all files in the folder...')

    for root, dirs, files in walk(folder):
        # root represents the current directory that is being processed
        # dirs represents the sub-directories in the currently processing directory
        # files represents the files inside the root directory

        # I want to store the file back into the directory that it came from in the directories, and I believe that I will need the root string to do that. 
        #print(root + " " + str(files))

        # TODO: in the future, reorganize the code so that the path.join() method is only called once in this funtion. will make this code cleaner in my opinion. 


        for curr in files:
            #print(root + curr)

            '''when using the rename() function:

                dst += .slp

                dst = root + '/' + dst
                src = root + '/' + originalFileName

            '''

            # check if the file ends in .slp
            # check that the game is not a teams or FFA
            # if only a 2 player game, send the SlippiGame file to the generate_file_name() function. 

            #print(curr)

            if curr.split('.')[-1] == 'slp':

                # NOTE: when building the pathname, we can use the os.path.join() function to insert the '/' characters into the path automatically. 

                #currFilePath = root + '/' + curr

                currFilePath = path.join(root, curr)

                #print('can process file {}'.format(currFilePath))


                try:

                    tempGame = Game(currFilePath)
                    
            
                    
                    #tempGame = Game(curr)
                    

                    if tempGame.start.is_teams != True:

                        # Count number of players in current game
                        currentPlayers = 0
                        for player in tempGame.start.players:
                            if player != None:
                                currentPlayers += 1


                        #print('number of players in game: {}'.format(currentPlayers))

                        if currentPlayers != 2:
                        
                            ffaFile = ''
                            ffaFile = generate_free_for_all_game_name(tempGame)

                            ffaFile = path.join(root, ffaFile)

                            #print('old file name: {}'.format(currFilePath))
                            #print('new file name: {}\n\n'.format(ffaFile))

                            rename(currFilePath, ffaFile)

                            #print('RENAMED A FREE FOR ALL GAME: ')


                        else: 

                            try:

                                #print('the game only has 2 players')

                                try:
                                        

                                    newFileName = ''
                                    newFileName = generate_singles_game_name(tempGame)

                                except:
                                    print('could not create single game name')

                                #print('just created a file name: {}'.format(newFileName))

                                #newFileName += '.slp'

                                #print("new file name: {}".format(newFileName))

                                #newFileName = root + '/' + newFileName

                                try:

                                    newFileName = path.join(root, newFileName)

                                except:
                                    print('could not join the root and the new file name')

                                #print('old file name: {}'.format(currFilePath))
                                #print('new file name: {}\n\n'.format(newFileName))


                                try:
                                        

                                    rename(currFilePath, newFileName) # note: this line here is causing issues when running on windows... I wonder why this is happening... This might be because of the file path differences between Linux and windows...
                                    #print('successfully renamed the file')

                                except:
                                    print(f"Can't RENAME: {currFilePath}")

                            except:
                                print(f"Can't process SINGLES: {currFilePath}")
                            
                    else:
                    
                        try:

                            doubles = ''
                            doubles = generate_doubles_game_name(tempGame)

                            doubles = path.join(root, doubles)

                            rename(currFilePath, doubles)

                        except:
                            print(f"Can't process TEAMS: {currFilePath}")

                except:
                    # TODO: look into why the renaming program breaks here. what exception is being thrown? This might be because of the replay being cut off when the connection was cut. see if there is any way to tell if a file is malformed...

                    # TODO: look into if this block is reached ONLY if the file is corrupt. 

                    print(f'CORRUPTED: {currFilePath}')
                    

            else:
                print(f'WRONG FORMAT: {currFilePath}')


    print(f"finished renaming files in {folder}")


# NOTE: this is where the program starts executing when run as a command line program. 
# TODO: change the folder input parameter for the function to be based on the command line argument that the user has given rather than being a hard coded directory name. 
#rename_files_in_folder('.\slp') # NOTE: '/' for linux, '\' for windows. 

# NOTE: these function calls below will only execute when the file itself is executed. When the file is exported as a module, then these function calls will not execute automatically. 
if __name__ == "__main__":


    directory = path.join(path.dirname(path.realpath(__file__)), 'slp')

    rename_files_in_folder(directory)

    print("All files in the directory have been renamed.")
