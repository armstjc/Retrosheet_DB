###################################################
##  Author:  Joseph Armstrong                    ##
##  Email:   armstrongjoseph08@gmail.com         ##
##  Purpose: Parse data from the                 ##
##           Retrosheet organization.            ##
###################################################
import glob
import os
from numpy import False_, spacing
import pandas as pd
from tqdm import tqdm


def parsePlayerGameLogs():
    '''
    help
    '''
    l = 'raw_data/retrosplit/player_gamelog/'
    f = os.listdir(l)
    numF = len(f)
    main = pd.DataFrame()
    for i in range(0,numF):
        print(f'{i}/{numF}: {f[i]}')
        fileName = l + f[i]
        df = pd.read_csv(fileName)
        #print(df)
        main = pd.concat([main, df], ignore_index=True)
    main.to_csv('data/playerGameLogs.csv',index=False)
    
    print(main)
    del main

def parseTeamGameLogs():
    '''
    help
    '''
    l = 'raw_data/retrosplit/team_gamelog/'
    f = os.listdir(l)
    numF = len(f)
    main = pd.DataFrame()
    for i in range(0,numF):
        print(f'{i}/{numF}: {f[i]}')
        fileName = l + f[i]
        df = pd.read_csv(fileName)
        #print(df)
        main = pd.concat([main, df], ignore_index=True)
    main.to_csv('data/teamGameLogs.csv',index=False)
    
    print(main)
    del main

def parseBattingByPosition():
    '''
    help
    '''
    l = 'raw_data/retrosplit/batting_by_position/'
    f = os.listdir(l)
    numF = len(f)
    main = pd.DataFrame()
    for i in range(0,numF):
        print(f'{i}/{numF}: {f[i]}')
        fileName = l + f[i]
        df = pd.read_csv(fileName)
        #print(df)
        main = pd.concat([main, df], ignore_index=True)
    main.to_csv('data/battingByPosition.csv',index=False)
    
    print(main)
    del main



def parseBattingByRunners():
    '''
    help
    '''
    l = 'raw_data/retrosplit/batting_by_runners/'
    f = os.listdir(l)
    numF = len(f)
    main = pd.DataFrame()
    for i in range(0,numF):
        print(f'{i}/{numF}: {f[i]}')
        fileName = l + f[i]
        df = pd.read_csv(fileName)
        #print(df)
        main = pd.concat([main, df], ignore_index=True)
    main.to_csv('data/battingByPosition.csv',index=False)
    
    print(main)
    del main

def parseBattingHeadToHead():
    '''
    help
    '''
    l = 'raw_data/retrosplit/batting_head_to_head/'
    f = os.listdir(l)
    numF = len(f)
    main = pd.DataFrame()
    for i in range(0,numF):
        print(f'{i}/{numF}: {f[i]}')
        fileName = l + f[i]
        df = pd.read_csv(fileName)
        #print(df)
        main = pd.concat([main, df], ignore_index=True)
    main.to_csv('data/battingHeadToHead.csv',index=False)
    
    print(main)
    del main

def parseBattingPlatoon():
    '''
    help
    '''
    l = 'raw_data/retrosplit/batting_platoon/'
    f = os.listdir(l)
    numF = len(f)
    main = pd.DataFrame()
    for i in range(0,numF):
        print(f'{i}/{numF}: {f[i]}')
        fileName = l + f[i]
        df = pd.read_csv(fileName)
        #print(df)
        main = pd.concat([main, df], ignore_index=True)
    main.to_csv('data/battingPlatoon.csv',index=False)
    
    print(main)
    del main


def parsePitchingByRunners():
    '''
    help
    '''
    l = 'raw_data/retrosplit/pitching_by_runners/'
    f = os.listdir(l)
    numF = len(f)
    main = pd.DataFrame()
    for i in range(0,numF):
        print(f'{i}/{numF}: {f[i]}')
        fileName = l + f[i]
        df = pd.read_csv(fileName)
        #print(df)
        main = pd.concat([main, df], ignore_index=True)
    main.to_csv('data/pitchingByRunners.csv',index=False)
    
    print(main)
    del main

def parsePitchingPlatoon():
    '''
    help
    '''
    l = 'raw_data/retrosplit/pitching_platoon/'
    f = os.listdir(l)
    numF = len(f)
    main = pd.DataFrame()
    for i in range(0,numF):
        print(f'{i}/{numF}: {f[i]}')
        fileName = l + f[i]
        df = pd.read_csv(fileName)
        #print(df)
        main = pd.concat([main, df], ignore_index=True)
    main.to_csv('data/pitchingPlatoon.csv')
    
    print(main)
    del main

def parseMlbTransactionFile():
    c=['primary-date','time','approximate-indicator','secondary-date','approximate-indicator-2','transaction-ID','player','type','from-team','from-league','to-team','to-league','draft-type','draft-round','pick-number','info']

    df = pd.read_csv('raw_data/retrosheet/transactions/tran.txt') 


    df.columns=c    
    df.to_csv('data/transactions.csv',index=False)

def parseMlbSchedules():
    print('')
    l = 'raw_data/retrosheet/schedules/'
    #f = os.listdir(l)
    #numF = len(f)
    all_files = glob.glob(l+"*SKED.TXT")
    numF = len(all_files)
    main = pd.DataFrame(columns=['date','game#','day','visitor','visiting_lg','v_g#','home','home_lg','h_g#','daytime','is_postponed','makeup_date'])
    c = 0
    for i in all_files:
        c = c + 1
        print(f'{c}/{numF}: {i}')
        fileName = i
        df = pd.read_csv(fileName)
        df.columns = ['date','game#','day','visitor','visiting_lg','v_g#','home','home_lg','h_g#','daytime','is_postponed','makeup_date']
        #print(df)
        main = pd.concat([main, df], ignore_index=True)
    try:
        df = pd.read_csv('raw_data/retrosheet/schedules/2020REV.TXT')
        df.columns = ['date','game#','day','visitor','visiting_lg','v_g#','home','home_lg','h_g#','daytime','is_postponed','makeup_date']
        main = pd.concat([main, df], ignore_index=True)
    except:
        print('The 2020 Schedule was not found. Check ./raw_data/retrosheet/schedules/ if you belive this is an error.')

    main.to_csv('data/schedule.csv', index=False)
    
    print(main)
    del main

def main():
    print('Starting up!')
    #parsePlayerGameLogs()
    #parseTeamGameLogs()
    #parseBattingByPosition()
    #parseBattingByRunners()
    #parseBattingHeadToHead()
    #parseBattingPlatoon()
    #parsePitchingByRunners()
    #parsePitchingPlatoon()
    #parseMlbTransactionFile()
    parseMlbSchedules()
if __name__ == "__main__":
    main()