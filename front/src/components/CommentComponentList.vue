<template>
  <div class="comment_big_box lay2">
    <div class="comment_text_box">
      <img class="profile_img4" :src="require(`../assets/profile${comment.userprofile}.png`)" alt="#" width="36"
        height="36" />
      <!-- <img v-if="comment.userprofile === 1" class="profile_img" src="../assets\profile1.png" alt="#" width="36"
        height="36" />
      <img v-else-if="comment.userprofile === 2" class="profile_img" src="../assets\profile2.png" alt="#" width="36"
        height="36" />
      <img v-else-if="comment.userprofile === 3" class="profile_img" src="../assets\profile3.png" alt="#" width="36"
        height="36" />
      <img v-else-if="comment.userprofile === 4" class="profile_img" src="../assets\profile4.png" alt="#" width="36"
        height="36" />
      <img v-else-if="comment.userprofile === 5" class="profile_img" src="../assets\profile5.png" alt="#" width="36"
        height="36" />
      <img v-else-if="comment.userprofile === 6" class="profile_img" src="../assets\profile6.png" alt="#" width="36"
        height="36" />
      <img v-else-if="comment.userprofile === 7" class="profile_img" src="../assets\profile7.png" alt="#" width="36"
        height="36" />
      <img v-else-if="comment.userprofile === 8" class="profile_img" src="../assets\profile8.png" alt="#" width="36"
        height="36" />
      <img v-else-if="comment.userprofile === 9" class="profile_img" src="../assets\profile9.png" alt="#" width="36"
        height="36" /> -->
      <div class="comment_right_box">
        <div class="user_name_box">
          {{ comment.username }}
          <span v-if="grade !== 0">님의 TOP {{ grade }}</span>
        </div>
        <div class="user_comment_box">{{ comment.content }}</div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios"

const API_URL = "http://127.0.0.1:8000"

export default {
  name: "CommentComponentList",
  props: {
    comment: Object,
    movieId: Number,
  },
  data() {
    return {
      profile: null,
      grade: 0,
    }
  },
  methods: {
    getProfile() {
      console.log('실행')
      axios({
        method: "get",
        url: `${API_URL}/movies/profiles/${this.comment.user}/`,
      })
        .then((res) => {
          this.profile = res.data
        })
        .then(() => {
          this.getGrade()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getGrade() {
      console.log(this.profile)
      if (this.movieId === this.profile.movie1) {
        this.grade = 1
      } else if (this.movieId === this.profile.movie2) {
        this.grade = 2
      } else if (this.movieId === this.profile.movie3) {
        this.grade = 3
      } else if (this.movieId === this.profile.movie4) {
        this.grade = 4
      } else if (this.movieId === this.profile.movie5) {
        this.grade = 5
      } else if (this.movieId === this.profile.movie6) {
        this.grade = 6
      } else if (this.movieId === this.profile.movie7) {
        this.grade = 7
      } else if (this.movieId === this.profile.movie8) {
        this.grade = 8
      } else if (this.movieId === this.profile.movie9) {
        this.grade = 9
      } else if (this.movieId === this.profile.movie10) {
        this.grade = 10
      }
    }
  },
  created() {
    this.getProfile()
  },
  updated() {
    this.getProfile()
  },
}
</script>

<style>

</style>