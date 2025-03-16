import backtrader as bt
import datetime

class TestStrategy(bt.Strategy):
    def __init__(self):
        self.dataclose = self.datas[0].close

    def next(self):
        if self.dataclose[0] < self.dataclose[-1]:
            if self.dataclose[-1] < self.dataclose[-2]:
                self.buy()

if __name__ == '__main__':
    cerebro = bt.Cerebro()
    cerebro.addstrategy(TestStrategy)

    data = bt.feeds.YahooFinanceData(
        dataname='AAPL',
        fromdate=datetime.datetime(2020, 1, 1),
        todate=datetime.datetime(2021, 1, 1),
        reverse=False
    )

    cerebro.adddata(data)
    cerebro.broker.setcash(10000.0)
    cerebro.run()
    cerebro.plot()