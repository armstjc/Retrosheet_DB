from pybaseball import statcast, pybaseball

import pandas as pd

def getStatcastDataInYearRange(start=2019,end=2021):
    '''
    getStatcastDataInYearRange(start = ) 
    '''
 
    for i in range(start, end+1):
            
        start = f'{i}-01-01'
        end = f'{i}-12-31'
        print(start,end)
        data = statcast(start_dt=start, end_dt=end,verbose=True)
        data.to_csv(f'raw_data/Statcast/{i}-{j}.csv')
    print('All done')



if __name__ == "__main__":
    pybaseball.cache.enable()
    ## Min year is 1974
    getStatcastDataInYearRange()
    
    