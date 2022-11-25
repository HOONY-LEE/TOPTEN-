<template>
  <div>
    <div class="profile_box_unit lay" @click="moveProfile">
      <!-- <img src="{% static '/media/profile/261143_20210325180240_500_0DlWsW8.jpg' %}" alt="#" /> -->
      <!-- <p v-html="img_tag"></p> -->
      <img class="profile_img" :src="require(`../assets/profile${profile.img}.png`)" alt="#" width="36" height="36" />
      <!-- <img v-if="profile.img === 1" class="profile_img" src="../assets\profile1.png" alt="#" width="36" height="36" />
      <img v-if="profile.img === 2" class="profile_img" src="../assets\profile2.png" alt="#" width="36" height="36" />
      <img v-if="profile.img === 3" class="profile_img" src="../assets\profile3.png" alt="#" width="36" height="36" />
      <img v-if="profile.img === 4" class="profile_img" src="../assets\profile4.png" alt="#" width="36" height="36" />
      <img v-if="profile.img === 5" class="profile_img" src="../assets\profile5.png" alt="#" width="36" height="36" />
      <img v-if="profile.img === 6" class="profile_img" src="../assets\profile6.png" alt="#" width="36" height="36" />
      <img v-if="profile.img === 7" class="profile_img" src="../assets\profile7.png" alt="#" width="36" height="36" />
      <img v-if="profile.img === 8" class="profile_img" src="../assets\profile8.png" alt="#" width="36" height="36" />
      <img v-if="profile.img === 9" class="profile_img" src="../assets\profile9.png" alt="#" width="36" height="36" /> -->
      <div class="profile_text_box">
        {{ profile.name }} [{{ gender }}] </div>
    </div>
  </div>
</template>

<script>
import axios from "axios"

const API_URL = "http://127.0.0.1:8000"

export default {
  name: "FollowingComponentList",
  props: {
    followingProfileId: Object,
  },
  data() {
    return {
      profile: null,
      gender: null,
    }
  },
  methods: {
    moveProfile() {
      this.$router.push({ name: 'profile', params: { profileId: this.profile.id } })
    },
    getProfile() {
      axios({
        method: "get",
        url: `${API_URL}/movies/profiles/${this.followingProfileId}`,
      })
        .then((res) => {
          this.profile = res.data
        })
        .then(() => {
          this.makeProfile()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    makeProfile() {
      if (this.profile.gender === 1) {
        this.gender = '남'
      } else if (this.profile.gender === 2) {
        this.gender = '여'
      }
      // this.img_tag = `<img class="profile_img" src="../assets\\profile${this.profile.img}.png" alt="#" width="36" height="36" />`
    }
  },
  created() {
    this.getProfile()
  },
}
</script>

<style>
.profile_box_unit {
  width: 150px;
  height: 200px;
  margin: 0px 20px;
  justify-content: center;
  ;
}

.profile_box_unit>img {
  width: 140px;
  height: 140px;
}

.profile_text_box {
  margin-top: 10px;
}
</style>