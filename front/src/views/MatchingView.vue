<template>
  <div class="">
    <h1>매칭서비스</h1>

    <hr>

    <div class="form-check form-check-inline visually-hidden">
      <input class="form-check-input" type="radio" name="gender" id="x" value="1" v-model="gender">
      <label class="form-check-label" for="x">
        모두
      </label>
    </div>
    <div class="form-check form-check-inline visually-hidden">
      <input class="form-check-input" type="radio" name="gender" id="y" value="2" v-model="gender">
      <label class="form-check-label" for="y">
        모두
      </label>
    </div>
    <div class="form-check form-check-inline">
      <input class="form-check-input" type="radio" name="gender" id="all" value="3" v-model="gender">
      <label class="form-check-label" for="all">
        모두
      </label>
    </div>
    <div class="form-check form-check-inline">
      <input class="form-check-input" type="radio" name="gender" id="other" value="4" v-model="gender">
      <label class="form-check-label" for="other">
        이성만
      </label>
    </div>

    <hr>

    <div class="form-check form-check-inline">
      <input class="form-check-input" type="radio" name="method" value="1" id="random" v-model="method">
      <label class="form-check-label" for="random">
        랜덤 추천
      </label>
    </div>
    <div class="form-check form-check-inline">
      <input class="form-check-input" type="radio" name="method" value="2" id="pick" v-model="method">
      <label class="form-check-label" for="pick">
        탑텐 추천
      </label>
    </div>

    <hr>

    <button class="follow_btn matching_btn" @click="goRecommend">매칭하기</button>
  </div>
</template>
<script>
import axios from "axios"

const API_URL = "http://127.0.0.1:8000"

export default {
  name: "MatchingView",
  data() {
    return {
      profileId: this.$store.state.profile_id,
      profile: null,
      gender: 3,
      method: 1,
    }
  },
  methods: {
    getProfile() {
      axios({
        method: "get",
        url: `${API_URL}/movies/profiles/${this.profileId}/`,
      })
        .then((res) => {
          console.log(res.data)
          if (res.data.movie10) {
            this.profile = res.data
          } else {
            alert('무비 TOPTEN을 채워주세요!')
            this.$router.push({ name: 'home' })
          }
        })
        .catch((err) => {
          console.log(err)
        })
    },
    goRecommend() {
      if (this.gender == 4) {
        this.gender = this.profile.gender
      }
      axios({
        method: "get",
        url: `${API_URL}/movies/recommend/${this.profileId}/${this.gender}/${this.method}/`,
      })
        .then((res) => {
          console.log(res.data)
          if (res.data.length === 0) {
            alert('취향을 맞출 유저가 없습니다. ㅠㅠ')
          } else {
            this.$router.push({ name: 'profile', params: { profileId: res.data[0].id } })
          }
        })
        .catch((err) => {
          console.log(err)
        })

    }
  },
  created() {
    window.scrollTo(0, 0)
    this.getProfile()
  }
}
</script>

<style>
.matching_btn {
  width: 248px;
  margin-top: 20px;
}
</style>
