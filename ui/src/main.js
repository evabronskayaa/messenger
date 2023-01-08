import { createApp } from 'vue'
import App from './App.vue'


import './assets/styles/main.css'
import {createRouter, createWebHistory} from "vue-router";
import RegisterForm from "@/components/SignUp/SignUp.vue";
import TheWelcome from "@/components/TheWelcome.vue";
import SignUp from "@/components/SignUp/SignUp.vue";


const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            name: 'root',
            component: TheWelcome
        },
        {
            path: '/signup',
            name: 'signup',
            component: SignUp
        }
    ]
})


const app = createApp(App)
app.use(router)
app.mount('#app')