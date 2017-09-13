<template>
    <div>
        <h1 class="header">{{ $route.query.label }}</h1>

        <div v-if="messages.length > 0" class="ui segment">
            <router-link :to="{ name: 'index' }">
                <div style="position: absolute; right: 10px;" class="ui green basic button icon">
                    <i class="home icon"></i>
                </div>
            </router-link>

            <div class="ui divided selection list">
                <div 
                    v-for="(message, index) in messages"
                    :key="index"
                    style="padding: 1em;" 
                    class="item">
                    <div class="ui stackable grid">
                        <div class="four wide column">
                            {{ message.timestamp }}
                        </div>
                        <div class="eight wide column">
                            <span style="color: #5BBD72;">{{ message.message }}</span>
                        </div>
                        <div class="two wide column">
                            {{ message.handle }}
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="ui segment">
            <div class="ui stackable grid">
                <div class="six wide column">
                    <div class="ui fluid labeled input">
                        <div class="ui label">
                          Handle
                        </div>
                        <input v-model="handle" type="text" placeholder="Your name">
                    </div>
                </div>
                <div class="eight wide column">
                    <div class="ui fluid input">
                      <input v-model="newMessage" type="text" placeholder="Message...">
                    </div>
                </div>
                <div class="two wide column">
                    <button
                        @click="send"
                        class="ui fluid teal right labeled right floated icon button">
                      <i class="reply icon"></i>
                      Send
                  </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data () {
        return {
            chatsock: null,
            messages: [],
            handle: "",
            newMessage: ""
        }
    },
    methods: {
        send () {
            var message = {
                handle: this.handle,
                message: this.newMessage
            }
            this.chatsock.send(JSON.stringify(message));
            this.newMessage = "";
        }
    },

    mounted () {
        var url = "api/message/?limit=50&label=" + this.$route.query.label
        this.$http.get(url).then((response) => {
            this.messages = response.body
        })
        // Chat WebSocket
        var vm = this
        this.chatsock = new WebSocket(window.wsRoot + '/chat' + '/' + this.$route.query.label);

        this.chatsock.onmessage = function(message) {
            var data = JSON.parse(message.data);
            vm.messages.push(data);
        };
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: bold;
  font-size: 5em;
}

@media only screen and (max-width: 767px) {
    h1, h2 {
     font-weight: bold;
     font-size: 2em;
    }
}
</style>
