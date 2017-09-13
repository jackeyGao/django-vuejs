<template>
    <div>
        <h1 style="margin-top: 2em;font-size: 5em;">Django Channels Example</h1>

        <div style="margin-top: 2em; margin-bottom: 2em; font-size: 2em; line-height: 150%;"
            class="ui">
            This is a demo using <a href="http://channels.readthedocs.org/en/latest/">Django Channels</a> and <a href="https://cn.vuejs.org/index.html">Vue.js</a> to implement a simple WebSocket-based chat server. You can see the <a href="https://github.com/jackeyGao/django-vuejs">code on GitHub</a>, or try the app:
        </div>

        <div style="font-size: 2.42857143rem;margin-bottom: 1em;" class="ui huge grey basic button" @click="createRoom">Create New Room</div>

        <div class="ui segment">
            <div class="ui selection list">
                <div class="item">
                    <div class="ui grid">
                        <div class="two wide column">
                            <h3 class="ui header">#</h3>
                        </div>
                        <div class="eight wide column">
                            <h3 class="ui header">Label</h3>
                        </div>
                        <div class="six wide column">
                            <h3 class="ui right floated header">-</h3>
                        </div>
                    </div>
                </div>

                <div class="item" v-for="room in rooms" :key="room.id">
                    <div class="ui grid">
                        <div class="two wide column">
                            <h3 class="ui header">{{ room.id }}</h3>
                        </div>
                        <div class="eight wide column">
                            {{ room.label }}
                        </div>
                        <div class="six wide column">
                            <router-link :to="{ name: 'room', query: { label: room.label }}">
                                 <h5 style="float: right;" class="ui green header">进入</h5>
                            </router-link>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <h5 class="ui grey header">Or, you can visit <span class="code">http://127.0.0.1:8000/any-path-you-want</span> to create a arbitrary room or join one whose name you know.</h5>
    </div>
</template>


<script>
export default {
    data () {
        return {
            rooms: []
        }
    },

    methods: {
        createRoom () {
            this.$http.post('api/room/').then((response) => {
                this.$router.push({name: 'room', query: {label: response.body["label"]}})
            })
        }
    },

    mounted () {
        this.$http.get('api/room/').then((response) => {
            this.rooms = response.body
        })
    }
}
</script>

<style>

.code {
    font-family: Courier, 'Courier New', monospace!important;
}

a {
    color: #5BBD72;
}

</style>


