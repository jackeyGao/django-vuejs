import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import Room from '@/components/Room'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: Index
    },
    {
      path: '/room',
      name: 'room',
      component: Room
    }
  ]
})
