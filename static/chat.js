$(function() {
    // When we're using HTTPS, use WSS too.
    var ws_scheme = window.location.protocol == "https:" ? "wss://" : "ws://";

    var chatsock = new ReconnectingWebSocket(ws_scheme + location.host + "/chat");
    chatsock.onmessage = function(message) {
        alert(message.data);
    };

    $("#go").on("click", function(event) {
        chatsock.send($("#message")[0].value);
    });
});