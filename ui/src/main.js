import { createApp } from 'vue'
import App from './App.vue'


import './assets/styles/main.css'
import {createRouter, createWebHistory} from "vue-router";
import RegisterForm from "@/components/RegisterForm.vue";
import TheWelcome from "@/components/TheWelcome.vue";


const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/register',
            name: 'register',
            component: RegisterForm
        },
        {
            path: '/',
            name: 'root',
            component: TheWelcome
        }]
})


const app = createApp(App)
app.use(router)
app.mount('#app')