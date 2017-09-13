// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import VueResource from 'vue-resource'

Vue.use(VueResource)

window.wsScheme = window.location.protocol == "https:" ? "wss" : "ws";

// HTTP
Vue.use(VueResource);

if (process.env.NODE_ENV === 'development') {
    Vue.http.options.root = 'http://127.0.0.1:8000';
    window.wsRoot = 'ws://127.0.0.1:8000'
} else {
  Vue.http.options.root = window.location.protocol + "//" + window.location.host
  window.wsRoot = window.wsScheme + "://" + window.location.host
}

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
