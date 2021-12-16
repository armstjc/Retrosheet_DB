###################################################
##  Author:  Joseph Armstrong                    ##
##  Email:   armstrongjoseph08@gmail.com         ##
##  Purpose: Parse data from the                 ##
##           Retrosheet organization.            ##
###################################################
import glob
import os
import pandas as pd
from tqdm import tqdm

def merger():
    main = pd.DataFrame()
    #f = len(glob.iglob(dir+"/*csv"))
    f = 21968
    l = "C:/Users/xme10/OneDrive - University of Cincinnati/CFB STATS PROJECT/NFL Player Stats/NFL Player Files"
    for file in tqdm(glob.iglob(l+"/*csv"),total=f,ascii=True, bar_format='{l_bar}{bar:30}{r_bar}{bar:-30b}'):
        #f = f + 1
        id = str(file)
        #print('file #' + str(f))
        df = pd.read_csv(file)
        df['Player'] = id
        main = pd.concat([main, df], ignore_index=True)
    
    main.to_csv('C:/Users/xme10/OneDrive - University of Cincinnati/CFB STATS PROJECT/NFL Player Stats/Merged.csv', index=False)

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
    main.to_csv('data/playerGameLogs.csv')

    print(main)

def main():
    print('Starting up!')
    parsePlayerGameLogs()


if __name__ == "__main__":
    main()