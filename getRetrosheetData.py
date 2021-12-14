###################################################
##  Author:  Joseph Armstrong                    ##
##  Email:   armstrongjoseph08@gmail.com         ##
##  Purpose: Download and parse data from the    ##
##           Retrosheet organization.            ##
###################################################
import requests
import os
from zipfile import ZipFile
from tqdm import tqdm

def getRetrosheetGameLogZip(start=1871,end=2020):
    '''
    getRetrosheetGameLogZip(end=int)
    Gets all advalible game logs from Retrosheet,
    starting from 1871, until the end year. 

    ARGS:
    start (int): Determines the first season you 
    want game logs from. By default, this is 1871.
    end (int): Determines the last season you want
    game logs from. By defuault, this is 2020.
    '''
    #start=1871

    print('starting up')
    url = f'https://www.retrosheet.org/gamelogs/gl{start}_{end}.zip'
    print('Getting the game log zip file.')
    r = requests.get(url, allow_redirects=True)
    print('saving off the zip file')
    open(f'raw_data/zip/gl{start}_{end}.zip', 'wb').write(r.content)
    print('Unzipping the file to the correct directory.')
    unzipRetrosheetZipMK1(s=start,e=end)
    print('All Done!')

def getRetrosheetBioFile():
    '''
    '''
    url = 'https://www.retrosheet.org/BIOFILE.TXT'
    r = requests.get(url, allow_redirects=True)
    open(f'raw_data/BIOFILE.CSV', 'wb').write(r.content)

def getRetrosheetParkFile():
    '''
    '''
    url = 'https://raw.githubusercontent.com/chadwickbureau/retrosheet/master/misc/parkcode.txt'
    r = requests.get(url, allow_redirects=True)
    open(f'raw_data/PARKFILE.CSV', 'wb').write(r.content)

def getRetrosheetTransactionFile():
    '''
    '''
    url = 'https://www.retrosheet.org/transactions/tranDB.zip'
    r = requests.get(url, allow_redirects=True)
    open(f'raw_data/zip/transactions.zip', 'wb').write(r.content)
    with ZipFile(f'raw_data/zip/transactions.zip', 'r') as zipObj:
        print('extracting contents')
        # Extract all the contents of zip file in different directory
        zipObj.extractall('raw_data/retrosheet/transactions')

def getRetrosheetEjectionFile():
    '''
    '''
    url = 'https://www.retrosheet.org/Ejecdata.txt'
    r = requests.get(url, allow_redirects=True)
    open(f'raw_data/retrosheet/ejections/ejections.csv', 'wb').write(r.content)

def getRetrosheetScheduleFiles():
    '''
    '''
    url = 'https://www.retrosheet.org/transactions/tranDB.zip'
    r = requests.get(url, allow_redirects=True)
    open(f'raw_data/zip/schedules.zip', 'wb').write(r.content)
    with ZipFile(f'raw_data/zip/schedules.zip', 'r') as zipObj:
        print('extracting contents')
        # Extract all the contents of zip file in different directory
        zipObj.extractall('raw_data/retrosheet/schedules')


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

def getRetrosplitsGameLogs(start=1901,end=2020):
    '''
    help
    '''
    ## Individual player game logs
    for i in tqdm(range(start,end+1), ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        url = f'https://raw.githubusercontent.com/chadwickbureau/retrosplits/master/daybyday/playing-{i}.csv'
        r = requests.get(url, allow_redirects=True)
        open(f'raw_data/retrosplit/player_gamelog/playing-{i}.csv', 'wb').write(r.content)

def getRetrosplitsTeamGameLogs(start=1901,end=2020):
    '''
    help
    '''
    ## Individual player game logs
    for i in tqdm(range(start,end+1), ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        url = f'https://raw.githubusercontent.com/chadwickbureau/retrosplits/master/daybyday/teams-{i}.csv'
        r = requests.get(url, allow_redirects=True)
        open(f'raw_data/retrosplit/team_gamelog/teams-{i}.csv', 'wb').write(r.content)

def getRetrosplitsBattingByPosition(start=1974,end=2020):
    '''
    help
    '''
    ## Individual player game logs
    for i in tqdm(range(start,end+1), ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        url = f'https://raw.githubusercontent.com/chadwickbureau/retrosplits/master/daybyday/batting-byposition-{i}.csv'
        r = requests.get(url, allow_redirects=True)
        open(f'raw_data/retrosplit/batting_by_position/batting-byposition-{i}.csv', 'wb').write(r.content)

def getRetrosplitsBattingByRunners(start=1974,end=2020):
    '''
    help
    '''
    ## Individual player game logs
    for i in tqdm(range(start,end+1), ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        url = f'https://raw.githubusercontent.com/chadwickbureau/retrosplits/master/daybyday/batting-byrunners-{i}.csv'
        r = requests.get(url, allow_redirects=True)
        open(f'raw_data/retrosplit/batting_by_runners/batting-by-runners-{i}.csv', 'wb').write(r.content)

def getRetrosplitsBattingByPlatoon(start=1974,end=2020):
    '''
    help
    '''
    ## Individual player game logs
    for i in tqdm(range(start,end+1), ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        url = f'https://raw.githubusercontent.com/chadwickbureau/retrosplits/master/daybyday/batting-platoon-{i}.csv'
        r = requests.get(url, allow_redirects=True)
        open(f'raw_data/retrosplit/batting_platoon/batting-platoon-{i}.csv', 'wb').write(r.content)

def getRetrosplitsBattingHeadToHead(start=1974,end=2020):
    '''
    help
    '''
    ## Individual player game logs
    for i in tqdm(range(start,end+1), ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        url = f'https://raw.githubusercontent.com/chadwickbureau/retrosplits/master/daybyday/batting-platoon-{i}.csv'
        r = requests.get(url, allow_redirects=True)
        open(f'raw_data/retrosplit/batting_head_to_head/headtohead-{i}.csv', 'wb').write(r.content)

def getRetrosplitsPitchingByRunners(start=1974,end=2020):
    '''
    help
    '''
    ## Individual player game logs
    for i in tqdm(range(start,end+1), ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        url = f'https://raw.githubusercontent.com/chadwickbureau/retrosplits/master/daybyday/batting-platoon-{i}.csv'
        r = requests.get(url, allow_redirects=True)
        open(f'raw_data/retrosplit/pitching_by_runners/batting-by-runners-{i}.csv', 'wb').write(r.content)

def getRetrosplitsPitchingByPlatoon(start=1974,end=2020):
    '''
    help
    '''
    ## Individual player game logs
    for i in tqdm(range(start,end+1), ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        url = f'https://raw.githubusercontent.com/chadwickbureau/retrosplits/master/daybyday/batting-platoon-{i}.csv'
        r = requests.get(url, allow_redirects=True)
        open(f'raw_data/retrosplit/pitching_platoon/pitching-platoon-{i}.csv', 'wb').write(r.content)



def main():
    print('Starting up Python!')

    ## Game Logs
    getRetrosheetGameLogZip()
    getRetrosheetBioFile()
    getRetrosheetParkFile()
    getRetrosheetTransactionFile()
    getRetrosheetEjectionFile()
    getRetrosheetScheduleFiles()
    getRetrosplitsGameLogs()
    getRetrosplitsTeamGameLogs()

    
    #getRetrosplitsBattingByPosition(start=i,end=i+1)
    #getRetrosplitsBattingByRunners(start=i,end=i+1)
    #getRetrosplitsBattingByPlatoon(start=i,end=i+1)
    #getRetrosplitsBattingHeadToHead(start=i,end=i+1)
    #getRetrosplitsPitchingByRunners(start=i,end=i+1)
    #getRetrosplitsPitchingByPlatoon(start=i,end=i+1)

if __name__ == "__main__":
    main()