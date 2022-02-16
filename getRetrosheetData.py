###################################################
##  Author:  Joseph Armstrong                    ##
##  Email:   armstrongjoseph08@gmail.com         ##
##  Purpose: Download data from the              ##
##           Retrosheet organization.            ##
###################################################
import requests
import os
from zipfile import ZipFile
from tqdm import tqdm


## Comented out because the method is done better by getRetrosplitsGameLogs()
#def getRetrosheetGameLogZip(start=1871,end=2020):
#    '''
#    getRetrosheetGameLogZip(end=int)
#    Gets all advalible game logs from Retrosheet,
#    starting from 1871, until the end year. 

#    ARGS:
#    start (int): Determines the first season you 
#    want game logs from. By default, this is 1871.
#    end (int): Determines the last season you want
#    game logs from. By defuault, this is 2020.
#    '''
#    #start=1871

#    print('starting up')
#    url = f'https://www.retrosheet.org/gamelogs/gl{start}_{end}.zip'
#    print('Getting the game log zip file.')
#    r = requests.get(url, allow_redirects=True)
#    print('saving off the zip file')
#    open(f'raw_data/zip/gl{start}_{end}.zip', 'wb').write(r.content)
#    print('Unzipping the file to the correct directory.')
#    unzipRetrosheetZipMK1(s=start,e=end)
#    print('All Done!')



def getRetrosheetBioFile():
    '''
    '''
    print('Getting The Bio File From Retrosheet.')
    url = 'https://www.retrosheet.org/BIOFILE.TXT'
    r = requests.get(url, allow_redirects=True)
    open(f'raw_data/BIOFILE.CSV', 'wb').write(r.content)
    print('All done!')
    print()

def getRetrosheetParkFile():
    '''
    '''
    print('Getting the Retrosheet Park File.')
    url = 'https://raw.githubusercontent.com/chadwickbureau/retrosheet/master/misc/parkcode.txt'
    r = requests.get(url, allow_redirects=True)
    open(f'raw_data/PARKFILE.CSV', 'wb').write(r.content)
    print('All Done!')
    print()

def getRetrosheetTransactionFile():
    '''
    '''
    print('Getting the Retrosheet Transaction File.')
    url = 'https://www.retrosheet.org/transactions/tranDB.zip'
    r = requests.get(url, allow_redirects=True)
    open(f'raw_data/zip/transactions.zip', 'wb').write(r.content)
    with ZipFile(f'raw_data/zip/transactions.zip', 'r') as zipObj:
        print('extracting contents')
        # Extract all the contents of zip file in different directory
        zipObj.extractall('raw_data/retrosheet/transactions')
    print('All Done!')
    print()

def getRetrosheetEjectionFile():
    '''
    '''
    print('Getting the Retrohseet Ejection File.')
    url = 'https://www.retrosheet.org/Ejecdata.txt'
    r = requests.get(url, allow_redirects=True)
    open(f'raw_data/retrosheet/ejections/ejections.csv', 'wb').write(r.content)
    print('All Done!')
    print()

def getRetrosheetScheduleFiles():
    '''
    '''
    print('Getting the Retrosheet Schedule Files.')
    url = 'http://www.retrosheet.org/schedule/schedule.zip'
    r = requests.get(url, allow_redirects=True)
    open(f'raw_data/zip/schedules.zip', 'wb').write(r.content)
    with ZipFile(f'raw_data/zip/schedules.zip', 'r') as zipObj:
        print('extracting contents')
        # Extract all the contents of zip file in different directory
        zipObj.extractall('raw_data/retrosheet/schedules')
    print('All Done!')
    print()

def unzipRetrosheetZipMK1(s=1871,e=2020,d='raw_data/team_gamelog'):
    '''
    unzipRetrosheetGameLogZip(s=int,e=int)
    Unzips a game log ZIP file from retrosheet,
    with the format of [type][start]_[end].zip.

    ARGS:
    s (int): Determines the first season you 
    want game logs from. By default, this is 1871.
    e (int): Determines the last season you want
    game logs from. By defuault, this is 2020.    
    '''
    print('starting up')
    with ZipFile(f'raw_data/zip/gl{s}_{e}.zip', 'r') as zipObj:
        print('extracting contents')
        # Extract all the contents of zip file in different directory
        zipObj.extractall(d)
        print('all done')
    print()

def getRetrosplitsGameLogs(start=1901,end=2020):
    '''
    help
    '''
    ## Individual player game logs
    print('Getting the RetroSplit Game Logs.')
    for i in tqdm(range(start,end+1), ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        url = f'https://raw.githubusercontent.com/chadwickbureau/retrosplits/master/daybyday/playing-{i}.csv'
        r = requests.get(url, allow_redirects=True)
        open(f'raw_data/retrosplit/player_gamelog/playing-{i}.csv', 'wb').write(r.content)
    print('All Done!')
    print()

def getRetrosplitsTeamGameLogs(start=1901,end=2020):
    '''
    help
    '''
    ## Individual player game logs
    print('Getting the RetroSplit Team Game Logs.')
    for i in tqdm(range(start,end+1), ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        url = f'https://raw.githubusercontent.com/chadwickbureau/retrosplits/master/daybyday/teams-{i}.csv'
        r = requests.get(url, allow_redirects=True)
        open(f'raw_data/retrosplit/team_gamelog/teams-{i}.csv', 'wb').write(r.content)
    print('All Done!')
    print()

def getRetrosplitsBattingByPosition(start=1974,end=2020):
    '''
    help
    '''
    ## Individual player game logs
    print('Getting the batting by position data from Retrosplit.')
    for i in tqdm(range(start,end+1), ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        url = f'https://raw.githubusercontent.com/chadwickbureau/retrosplits/master/splits/batting-byposition-{i}.csv'
        r = requests.get(url, allow_redirects=True)
        open(f'raw_data/retrosplit/batting_by_position/batting-byposition-{i}.csv', 'wb').write(r.content)
    print('All Done!')
    print()

def getRetrosplitsBattingByRunners(start=1974,end=2020):
    '''
    help
    '''
    ## Individual player game logs
    print('Getting the batting by runners data from Retrosplit.')
    for i in tqdm(range(start,end+1), ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        url = f'https://raw.githubusercontent.com/chadwickbureau/retrosplits/master/splits/batting-byrunners-{i}.csv'
        r = requests.get(url, allow_redirects=True)
        open(f'raw_data/retrosplit/batting_by_runners/batting-by-runners-{i}.csv', 'wb').write(r.content)
    print('All Done!')
    print()

def getRetrosplitsBattingByPlatoon(start=1974,end=2020):
    '''
    help
    '''
    ## Individual player game logs
    print('Getting the batting by platoon data from Retrosplit.')
    for i in tqdm(range(start,end+1), ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        url = f'https://raw.githubusercontent.com/chadwickbureau/retrosplits/master/splits/batting-platoon-{i}.csv'
        r = requests.get(url, allow_redirects=True)
        open(f'raw_data/retrosplit/batting_platoon/batting-platoon-{i}.csv', 'wb').write(r.content)
    print('All Done!')
    print()

def getRetrosplitsBattingHeadToHead(start=1974,end=2020):
    '''
    help
    '''
    ## Individual player game logs
    print('Getting the head-to-head batting data from Retrosplit.')
    for i in tqdm(range(start,end+1), ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        url = f'https://raw.githubusercontent.com/chadwickbureau/retrosplits/master/splits/headtohead-{i}.csv'
        r = requests.get(url, allow_redirects=True)
        open(f'raw_data/retrosplit/batting_head_to_head/headtohead-{i}.csv', 'wb').write(r.content)
    print('All Done!')
    print()

def getRetrosplitsPitchingByRunners(start=1974,end=2020):
    '''
    help
    '''
    ## Individual player game logs
    print('Getting the pitching by runners data from Retrosplit.')
    for i in tqdm(range(start,end+1), ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        url = f'https://raw.githubusercontent.com/chadwickbureau/retrosplits/master/splits/pitching-byrunners-{i}.csv'
        r = requests.get(url, allow_redirects=True)
        open(f'raw_data/retrosplit/pitching_by_runners/batting-by-runners-{i}.csv', 'wb').write(r.content)
    print('All Done!')
    print()

def getRetrosplitsPitchingByPlatoon(start=1974,end=2020):
    '''
    help
    '''
    ## Individual player game logs
    print('Getting the pitching by platoon data from Retrosplit.')
    for i in tqdm(range(start,end+1), ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        url = f'https://raw.githubusercontent.com/chadwickbureau/retrosplits/master/splits/pitching-platoon-{i}.csv'
        r = requests.get(url, allow_redirects=True)
        open(f'raw_data/retrosplit/pitching_platoon/pitching-platoon-{i}.csv', 'wb').write(r.content)
    print('All Done!')
    print()


def main():
    print('Starting up Python!')
    e= 2021
    ## Game Logs
    # getRetrosheetGameLogZip(end=e) #Retrosplits already does this
    #getRetrosheetBioFile()
    #getRetrosheetParkFile()
    #getRetrosheetTransactionFile()
    #getRetrosheetEjectionFile()
    #getRetrosheetScheduleFiles()
    getRetrosplitsGameLogs(end=e)
    #getRetrosplitsTeamGameLogs(end=e)

    
    getRetrosplitsBattingByPosition(end=e)
    getRetrosplitsBattingByRunners(end=e)
    getRetrosplitsBattingByPlatoon(end=e)
    getRetrosplitsBattingHeadToHead(end=e)
    getRetrosplitsPitchingByRunners(end=e)
    getRetrosplitsPitchingByPlatoon(end=e)

if __name__ == "__main__":
    main()