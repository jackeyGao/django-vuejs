<template>
    <div>
        <h1 id="header" >Django Channels Example</h1>

        <div 
            class="description">
            This is a demo using <a href="http://channels.readthedocs.org/en/latest/">Django Channels</a> and <a href="https://cn.vuejs.org/index.html">Vue.js</a> to implement a simple WebSocket-based chat server. You can see the <a href="https://github.com/jackeyGao/django-vuejs">code on GitHub</a>, or try the app:
        </div>

        <div id="buttons">
            <div 
                id="createButton"
                class="ui huge grey basic button"
                @click="createRoom">
                Create New Room
            </div>
        </div>

        <div id="roomlist" class="ui segment" >
            <div class="ui selection list">
                <div class="nomobile item" style="padding: 1em;">
                    <div class="ui grid">
                        <div class="two wide column" >
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

                <div class="ui divider"></div>
                <div class="item" v-for="room in rooms" :key="room.id" style="padding: 0 1em;">
                    <div class="ui stackable grid">
                        <div class="two wide column nomobile">
                            <h3 class="ui header">{{ room.id }}</h3>
                        </div>
                        <div class="ten wide column">
                            <span class="onlymobile">
                                <i style="width: 20px; margin-right: 0;" class="black minus icon"></i><i style="width: 20px;margin-left: -10px;" class="black minus icon"></i>
                                <router-link :to="{ name: 'room', query: { label: room.label }}">
                                    <span style="display: inline-block; color: #000;">{{ room.label }}</span>
                                </router-link>
                            </span>
                            <span class="nomobile">
                                <span style="display: inline-block; color: #000;">{{ room.label }}</span>
                            </span>
                        </div>
                        <div class="four wide column nomobile">
                            <router-link :to="{ name: 'room', query: { label: room.label }}">
                                 <h5 style="float: right;" class="ui green header">进入</h5>
                            </router-link>
                        </div>
                    </div>
                    <div class="ui divider" style="margin-left: -1em; margin-right: -1em;"></div>
                </div>
            </div>
        </div>

        <div class="description" style="margin-bottom: 0;">
            Or, you can visit <span class="code">{{ root }}/any-path-you-want</span> to create a arbitrary room or join one whose name you know.
        </div>
    </div>
</template>


<script>
import Vue from 'vue';

export default {
    data () {
        return {
            rooms: [],
            root: Vue.http.options.root,
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
    font-weight: normal;
    color: #5BBD72;
}

.description {
    margin-top: 2em;
    margin-bottom: 2em;
    font-size: 2em;
    line-height: 150%;
}

.footer {

}

#createButton {
    font-size: 2.42857143rem;
    margin-bottom: 1em;
}

.onlymobile {
    display: none;
}

#header {
    margin-top: 2em;
    font-size: 5em;
}

@media only screen and (max-width: 767px) {
    #buttons {
        text-align: center;
    }

    #createButton {
        font-size: 0.92857143rem;
        margin-bottom: 1em;
        margin-left: auto;
        margin-right: auto;
        width: 100%;
    }

    #header {
        font-size: 2em;
    }

    .description {
        margin-top: 1em;
        margin-bottom: 1em;
        font-size: 1em;
        line-height: 150%;
        background-color: rgba(230, 224, 208, 0.09);
        margin-left: -1em!important;
        margin-right: -1em!important;
        padding: 1em;
    }

    .footer {
        font-size: 1em;
    }

    #roomlist {
        border: 0;
        box-shadow: 0px 0px 0px 0px;
        padding: 0;
        margin: -1em;
        margin-top: 1em;
    }

    .onlymobile {
        display: inline;
    }

    .nomobile {
        display: none !important;
    }

    * {
        border-radius: 0!important;
    }
}

</style>


