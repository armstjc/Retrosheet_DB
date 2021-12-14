import os


def checkFolderCreation():
    try:
        os.mkdir('raw_data')
    except:
        pass

    try:
        os.mkdir('raw_data/zip')
    except:
        pass

    try:
        os.mkdir('raw_data/retrosheet')
    except:
        pass  
    
    try:
        os.mkdir('raw_data/retrosplit')
    except:
        pass    
    
    try:
        os.mkdir('raw_data/retrosheet/team_gamelog')
    except:
        pass

    try:
        os.mkdir('raw_data/retrosheet/play_by_play')
    except:
        pass

    try:
        os.mkdir('raw_data/retrosheet/play_by_play')
    except:
        pass
    
    try:
        os.mkdir('raw_data/retrosplit/player_gamelog')
    except:
        pass
    
    try:
        os.mkdir('raw_data/retrosplit/team_gamelog')
    except:
        pass
    
    try:
        os.mkdir('raw_data/retrosplit/batting_by_position')
    except:
        pass
    
    try:
        os.mkdir('raw_data/retrosplit/batting_by_runners')
    except:
        pass

    try:
        os.mkdir('raw_data/retrosplit/batting_platoon')
    except:
        pass

    try:
        os.mkdir('raw_data/retrosplit/batting_platoon')
    except:
        pass

    try:
        os.mkdir('raw_data/retrosplit/batting_head_to_head')
    except:
        pass
    
    try:
        os.mkdir('raw_data/retrosplit/pitching_by_runners')
    except:
        pass
    
    try:
        os.mkdir('raw_data/retrosplit/pitching_platoon')
    except:
        pass

    try:
        os.mkdir('raw_data/retrosheet/ejections')
    except:
        pass
    try:
        os.mkdir('raw_data/retrosheet/transactions')
    except:
        pass
    try:
        os.mkdir('raw_data/retrosheet/schedules')
    except:
        pass    
def main():
    checkFolderCreation()

if __name__ == "__main__":
    main()