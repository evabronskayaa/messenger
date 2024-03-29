import {createStore} from "vuex";

import users from './modules/users';
import chats from './modules/chats';
import axios from "axios";

export default createStore({
    state: {
        accessToken: localStorage.getItem('access_token')
    },
    getters: {
        accessToken: state => state.accessToken,
        isAuthenticated: state => !!state.accessToken
    },
    actions: {
        clearAccessToken({commit}) {
            commit('setAccessToken', null);
        }
    },
    mutations: {
        setAccessToken(state, token) {
            state.accessToken = token;
            if (token == null) {
                localStorage.removeItem('access_token');
            } else {
                localStorage.setItem('access_token', token);
            }
            axios.defaults.headers.common["Authorization"] = "Bearer " + localStorage.getItem("access_token");
        },
    },
    modules: {
        users,
        chats,
    }
});