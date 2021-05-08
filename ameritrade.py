import requests, time, re
import pandas as pd
import pickle as pkl

url = 'https://api.tdameritrade.com/v1/instruments'


df = pd.read_excel('company_list.xlsx')
symbols = df['Symbol'].values.toList()

start = 0
end = 500
files = []
while start < len(symbols):
    ticker = symbols[start:end]

    payload
    {
        'apikey': ameritrade,
        'symbol': 'GOOG',
        'projection': 'fundamental'}
    results = requests.get(url,parms=payload)
    data = result.json()
    f_name = time.ascttime() + '.pkl'
    f_name = re.sub('[ :]','_',f_name)
    files.append(f_name)

    with open(f_name,'wb') as file
        pkl.dump(data,file)
    start = end
    end += 500
    time.sleep(2)

data = []



for file in files:
    with open(file,'rb') as f:
        info = pkl.load(f)
    tickers = list(info)
    points = ['symbol', 'netProfitMarginMRQ','peRatio', 'pegRatio', 'high52']
    for ticker in tickers:
        tick = []
        for point in points:
            tic.append(info[ticker]['fundamental'][point])
        data.append(tick)
    os.remove(file)

points = ['symbol', 'Margin', 'pe', 'peg', 'high52']

df_result = pd.DataFrame(data, columns= points)

df_peg = df_results[df_results['PEG'] > 1]

def view(size):
    start = 0
    stop = size
    while stop  < len(df_peg):
        print(df_peg[start:stop])
        start = stop
        stop += size
    print(df_peg[start:stop])






