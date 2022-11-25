<template>
  <button @click="follow" v-if="followCheck">팔로우 취소</button>
  <button @click="follow" v-else>팔로우 취소</button>
</template>

<script>
import axios from "axios"

const API_URL = "http://127.0.0.1:8000"

export default {
  name: "FollowButtonComponent",
  props: {
    followCheck: Boolean,
    profileId: Number,
    myProfileId: Number,
  },
  methods: {
    follow() {
      axios({
        method: "post",
        url: `${API_URL}/movies/profiles/${this.profileId}/follow/${this.myProfileId}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res.data)
          console.log(this.followCheck)
          this.$emit('checkFollow')
          this.$forceUpdate()
        })
        .catch((err) => {
          console.log(err)
        })
    },
  }
}
</script>

<style>

</style>