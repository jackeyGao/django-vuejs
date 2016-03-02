$(function() {
    // When we're using HTTPS, use WSS too.
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var chatsock = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + "/chat" + window.location.pathname);
    
    chatsock.onmessage = function(message) {
        var data = JSON.parse(message.data);
        $("#chat").append('<tr>' 
            + '<td>' + data.timestamp + '</td>' 
            + '<td>' + data.username + '</td>'
            + '<td>' + data.message + ' </td>'
        + '</tr>');
    };

    $("#go").on("click", function(event) {
        var message = {
            username: $('#username').val(),
            message: $('#message').val(),
        }
        chatsock.send(JSON.stringify(message));
    });
});