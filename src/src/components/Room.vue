<template>
    <div>
        <router-link :to="{ name: 'index' }">
            <div style="position: absolute; left: 10px; top: 10px;" class="ui green basic button icon">
                <i class="home icon"></i>
            </div>
        </router-link>
        <h1 class="header">{{ $route.query.label }}</h1>

        <div id="messagelist" v-if="messages.length > 0" class="ui segment">

            <div class="ui mobile divider"></div>
            <div class="ui divided selection list">
                <div 
                    v-for="(message, index) in messages"
                    :key="index"
                    style="padding: 1em;" 
                    :class="{new: isNew(message)}"
                    class="item">
                    <div class="ui stackable grid">
                        <div class="four wide column">
                            {{ timeFormat(message.timestamp) }}
                        </div>
                        <div class="eight wide column">
                            <span style="color: #5BBD72;">{{ message.message }}</span>
                        </div>
                        <div class="two wide column">
                            {{ message.handle }}
                        </div>
                    </div>
                </div>
                <div class="ui mobile divider"></div>
            </div>
        </div>
        <div id="inputhandle" class="ui segment">
            <div class="ui stackable grid">
                <div class="six wide column nopadding">
                    <div class="ui fluid right action left icon input">
                        <i class="user icon"></i>
                        <input v-model="handle" type="text" placeholder="Your name">
                        <button @click="randomName" class="ui teal icon button">
                            <i class="refresh icon"></i>
                        </button>
                    </div>
                </div>
                <div class="eight wide column nopadding">
                    <div class="ui fluid input">
                      <input v-model="newMessage" type="text" placeholder="Message...">
                    </div>
                </div>
                <div class="two wide column nopadding">
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
import ReconnectingWebsocket from 'reconnectingwebsocket';
import Haikunator from 'haikunator';
import moment from 'moment';

var STORAGE_KEY = "channels-example";
var haikunator = new Haikunator();

var Storage = {
    fetch: function () {
        return JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');
    },
    save: function (data) {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
    }
};


export default {
    data () {
        return {
            chatsock: null,
            messages: [],
            handle: '',
            newMessage: ""
        }
    },

    watch: {
        handle (name) {
            Storage.save({ name: name })
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
        },

        randomName () {
            var random = haikunator.haikunate({tokenLength: 0});

            this.handle = random.split('-').map(function (n) {
                return n[0].toUpperCase()+n.substr(1);
            }).join(' ');
        },

        whoami () {
            var data = Storage.fetch()

            if (data.name) {
                this.handle = data.name
            } else {
                this.randomName()
            }
        },

        timeFormat (time) {
            return moment(moment.utc(time, 'lll')._d).format('lll')
        },

        isNew (message) {
            var ms = moment.utc().diff(moment.utc(message.timestamp, 'lll'))
            if (ms / 1000 < 60) {
                return true
            }
            return false
        }
    },

    mounted () {
        var url = "api/message/?limit=50&label=" + this.$route.query.label
        this.$http.get(url).then((response) => {
            this.messages = response.body
        })
        // Chat WebSocket
        var vm = this
        this.chatsock = new ReconnectingWebsocket(window.wsRoot + '/chat' + '/' + this.$route.query.label);

        this.chatsock.onmessage = function(message) {
            var data = JSON.parse(message.data);
            vm.messages.push(data);
        };

        this.whoami()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: bold;
  font-size: 5em;
}

.mobile {
    visibility: hidden !important;
}

.mobile.divider {
    margin: 0!important;
}

.new {
    background-color: rgba(230, 224, 208, 0.29)!important;
}

@media only screen and (max-width: 767px) {
    h1, h2 {
     font-weight: bold;
     font-size: 2em;
    }

    #messagelist {
        border: 0;
        box-shadow: 0px 0px 0px 0px;
        padding: 0;
        margin: -1em;
        margin-top: 1em;
    }

    #messagelist .list {
        margin-top: 0;
    }

    .mobile {
        visibility: visible !important;
    }

    #inputhandle {
        border: 0;
        box-shadow: 0px 0px 0px 0px;
        padding: 0;
        margin: -1em;
        margin-top: 1em;
        margin-top: 30px;
    }

    .nopadding {
        padding: 0!important;
    }

    .new {
        background-color: rgba(230, 224, 208, 0.29)!important;
    }

    * {
        border-radius: 0!important;
    }
}
</style>
