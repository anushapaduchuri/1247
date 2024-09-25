import os 
import pandas as pd
import matplotlib.py plot as plt
market_caps={
    'AAPL':2300,
    'MSFT':2100,
    'GOOGLE':1600,
    'AMZN':1700,
    'TSLA':900,
    'BRK-B':600,
    'NVDA':500,
    'META':700,
    'JNJ':400,
    'V':500,
}
top_10_companies={
    'AAPL':'Apple Inc.',
    'MSFT':'microsoft corporation',
    'GOOGL':'alphabet Inc.',
    'AMZN':'amazon.com,Inc.',
    'TSLA':'tesla,Inc.',
    'BRK-B':'Berkshire hathway Inc.',
    'NVDA':'NVIDIA Corporation',
    'META':'Meta platforms,Inc.',
    'JNJ':'Jhonson & Jhonsn',
    'v':'Visa Inc.',
}
current_directory=os.path.dirname(os.path.abspath(__file__))
CSV_file_path=os.path.join(current_directory,'top_10_stocks_sample_2013_2023.CSV')
df=pd.read_CSV(CSV_file_path)
df['date']=pd.to_datetime(df['date'])
df['year']=df['date'].dt.year
stock_columns=['AAPL_CLOSE','MSFT_CLOSE','GOOGL_CLOSE','TSLA_CLOSE','AMZN_CLOSE','BRK-B_CLOSE','NVDA_CLOSE','META_CLOSE','JNJ_CLOSE','V_CLOSE']
average_prices=df.groupby('year')[stocks_columns].mean().reset_index()
plt.figure(figsize=(20,10))
bar_width=0.1
years=average_prices['year']
positions=[years + 1 * bar_width for i in range(len(stock_columns))]
for i, column in enumerate(stock_columns):
    plt.bar(positions[1],average_prices[column],width=bar_width,label=column.split('_')[0])
    plt.xlabel('year')
    plt.ylabel('average closing price')
    plt.title('average closing price of top 10 stocks(2013_2023)')
    plt.xticks(years + bar_width* 4.5,years)
    plt.legend()
    plt.tight_layout()
    plt.show()