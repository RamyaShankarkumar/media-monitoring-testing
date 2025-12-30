import pandas as pd
import plotly.express as px
import time

LOG_FILE = "../logs/stream_logs.csv"

while True:
    df = pd.read_csv(LOG_FILE)
    fig = px.line(df, x='timestamp', y=['buffering','latency','bitrate'], title='Streaming Metrics')
    #fig.show()
    fig.write_html("reports/streaming_metrics.html", auto_open=False)
    time.sleep(5)
