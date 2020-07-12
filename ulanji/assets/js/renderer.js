var backend = null;
window.onload = function()
{
    new QWebChannel(qt.webChannelTransport, function(channel) {
        renderer = channel.objects.backend;
        renderer.getStr(function(val) {
            document.body.innerHTML = val;
        });
    });
}
