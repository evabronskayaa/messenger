<template>
  <header>
  </header>

  <main>
    <ChatNavbar/>
    <ChatSearch/>
    <div v-if="chats">
      <div v-for="chat in filteredChats" :key="chat.id" class="chats">
        <ChatListItem v-bind:chat="chat"/>
      </div>
    </div>

    <div class="page">
      <button type="submit" @click="showModal" style="font-weight: bold">+</button>
      <NewChatModal ref="modal"></NewChatModal>
    </div>
  </main>
</template>

<script>
import ChatListItem from "@/components/ChatListItem.vue";
import ChatSearch from "@/components/ChatSearch.vue";
import ChatNavbar from "@/components/ChatListNavbar.vue";
import {mapGetters} from "vuex";
import NewChatModal from "@/components/NewChatModal.vue";

export default {
  name: "ChatList",
  components: {NewChatModal, ChatSearch, ChatListItem, ChatNavbar},
  methods: {
    showModal: function () {
      this.$refs.modal.show = true
    },
    orderedChats: function () {
      return this.chats.sort(
          (a, b) => a.message && !b.message ? 1 :
              !a.message && b.message ? -1 : !a.message && !b.message ?
                  Date.parse(a.created_date) - Date.parse(b.created_date) : Date.parse(a.message.created_date) - Date.parse(b.message.created_date)
      ).reverse();
    }
  },
  created: async function () {
    try {
      await this.$store.dispatch('getChats');
    } catch (e) {
      console.log(e);
    }
  },
  computed: {
    ...mapGetters({chats: 'chats', filter: 'filter'}),
    filteredChats() {
      let chats = this.orderedChats();
      return this.filter == null || this.filter === '' ? chats : chats.filter(chat => {
        return chat.name.toLowerCase().includes(this.filter.toLowerCase())
      })
    }
  },
}
</script>

<style lang="less" scoped>
main {
  background: #F3F3F7;
  position: fixed;
  top: 0;
  left: 0;
  width: 30%;
  height: 100%;
  padding: 30px 30px 0 30px;
  overflow: auto;
}

button {
  min-width: 50px;
  width: 50px;
  height: 50px;
  border-radius: 100%;
  position: fixed;
  bottom: 0;
  left: 25%;
}

button:hover {
  background-color: #aa94b7;
}
</style>