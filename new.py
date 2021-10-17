import krakenex
import  datetime
from pykrakenapi import KrakenAPI
api = krakenex.API()
k = KrakenAPI(api)
ohlc, last = k.get_ohlc_data("XDGUSD")
close_prices = (ohlc.close.to_list())
close_time =  (ohlc.time.to_list()[::-1])

close_prices = close_prices[::-1]



    
begin='''
<!DOCTYPE HTML>
<html>
<head>  
<script>
window.onload = function () {

var chart = new CanvasJS.Chart("chartContainer", {
	animationEnabled: true,
	theme: "light1",
    backgroundColor:'#ffffff00',
	data: [{        
		type: "area",
      	indexLabelFontSize: 20,
        xValueType: "dateTime",
		dataPoints: [
'''

middle=''
for i in range(0,len(close_prices)):
    ts_epoch = close_time[i]
    #ts = datetime.datetime.fromtimestamp(ts_epoch).strftime('%Y-%m-%d %H:%M:%S')
    middle=middle+"{ x:"+str(ts_epoch*1000)+" ,y:"+str(close_prices[i])+"},\n"

end='''
]
	}]
});
chart.render();

}
</script>
</head>
<body style="background-color:orange">
<center>
<h1 style=" z-index: -10000;transform: translateY(4vh);">DogeCoin DashBoard</h1>
<div id="chartContainer" style="z-index:10;height: 370px; width: 70%;"></div>
</center>
<script src="https://canvasjs.com/assets/script/canvasjs.min.js"></script>
</body>       
</html>
'''

print(begin+middle+end,  file=open('DOGEgraph.html', 'w'))
