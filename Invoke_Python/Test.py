def ReadFile(fPath):

    import pandas as pd
    df = pd.read_csv(fPath)    
    df = df.dropna(subset=['File Extension'])
    return df.to_json(orient='records')    
 

