<template>
  <div>
    <h1>프로필</h1>
    <div>
      <h3>TOPTEN</h3>
      <div v-if="profile.movie1">
        <h5>TOP1 {{ movie1.title }}</h5>
        <button v-if="profile.movie2" @click="switchTopTen(1)">아래로</button>
        <button @click="deleteTopTen(1)">X</button>
      </div>
      <div v-if="profile.movie2">
        <h5>TOP2 {{ movie2.title }}</h5>
        <button @click="switchTopTen(1)">위로</button>
        <button v-if="profile.movie3" @click="switchTopTen(2)">아래로</button>
        <button @click="deleteTopTen(2)">X</button>
      </div>
      <div v-if="profile.movie3">
        <h5>TOP3 {{ movie3.title }}</h5>
        <button @click="switchTopTen(2)">위로</button>
        <button v-if="profile.movie4" @click="switchTopTen(3)">아래로</button>
        <button @click="deleteTopTen(3)">X</button>
      </div>
      <div v-if="profile.movie4">
        <h5>TOP4 {{ movie4.title }}</h5>
        <button @click="switchTopTen(3)">위로</button>
        <button v-if="profile.movie5" @click="switchTopTen(4)">아래로</button>
        <button @click="deleteTopTen(4)">X</button>
      </div>
      <div v-if="profile.movie5">
        <h5>TOP5 {{ movie5.title }}</h5>
        <button @click="switchTopTen(4)">위로</button>
        <button v-if="profile.movie6" @click="switchTopTen(5)">아래로</button>
        <button @click="deleteTopTen(5)">X</button>
      </div>
      <div v-if="profile.movie6">
        <h5>TOP6 {{ movie6.title }}</h5>
        <button @click="switchTopTen(5)">위로</button>
        <button v-if="profile.movie7" @click="switchTopTen(6)">아래로</button>
        <button @click="deleteTopTen(6)">X</button>
      </div>
      <div v-if="profile.movie7">
        <h5>TOP7 {{ movie7.title }}</h5>
        <button @click="switchTopTen(6)">위로</button>
        <button v-if="profile.movie8" @click="switchTopTen(7)">아래로</button>
        <button @click="deleteTopTen(7)">X</button>
      </div>
      <div v-if="profile.movie8">
        <h5>TOP8 {{ movie8.title }}</h5>
        <button @click="switchTopTen(7)">위로</button>
        <button v-if="profile.movie9" @click="switchTopTen(8)">아래로</button>
        <button @click="deleteTopTen(8)">X</button>
      </div>
      <div v-if="profile.movie9">
        <h5>TOP9 {{ movie9.title }}</h5>
        <button @click="switchTopTen(8)">위로</button>
        <button v-if="profile.movie10" @click="switchTopTen(9)">아래로</button>
        <button @click="deleteTopTen(9)">X</button>
      </div>
      <div v-if="profile.movie10">
        <h5>TOP10 {{ movie10.title }}</h5>
        <button @click="switchTopTen(9)">위로</button>
        <button @click="deleteTopTen(10)">X</button>
      </div>
    </div>
    <div>
      <h3>장르데이터</h3>
      <p>액션 : {{ actions }}</p>
      <p>모험 : {{ adventure }}</p>
      <p>애니메이션 : {{ animation }}</p>
      <p>코미디 : {{ comedy }}</p>
      <p>범죄 : {{ crime }}</p>
      <p>드라마 : {{ drama }}</p>
      <p>가족 : {{ family }}</p>
      <p>판타지 : {{ fantasy }}</p>
      <p>역사 : {{ history }}</p>
      <p>공포 : {{ horror }}</p>
      <p>음악 : {{ music }}</p>
      <p>미스터리 : {{ mystery }}</p>
      <p>로맨스 : {{ romance }}</p>
      <p>SF : {{ sf }}</p>
      <p>스릴러 : {{ thriller }}</p>
      <p>전쟁 : {{ war }}</p>
    </div>
    <div>
      <div>
        <h5>팔로워</h5>
        <p>{{ profile.followers }}</p>
      </div>
      <div>
        <h5>팔로잉</h5>
        <p>{{ profile.followings }}</p>
      </div>
      <div>
        <h5>받은 메시지</h5>
        <p>{{ profile.message_recive }}</p>
      </div>
      <div>
        <h5>보낸 메시지</h5>
        <p>{{ profile.message_send }}</p>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios"

const API_URL = "http://127.0.0.1:8000"

export default {
  name: "ProfileView",
  data() {
    return {
      profileId: this.$route.params.profileId,
      profile: null,
      action: 0,
      adventure: 0,
      animation: 0,
      comedy: 0,
      crime: 0,
      drama: 0,
      family: 0,
      fantasy: 0,
      history: 0,
      horror: 0,
      music: 0,
      mystery: 0,
      romance: 0,
      sf: 0,
      thriller: 0,
      war: 0,
    }
  },
  methods: {
    getProfile() {
      console.log('acive getProfile')
      axios({
        method: "get",
        url: `${API_URL}/movies/profiles/${this.profileId}`,
      })
        .then((res) => {
          this.profile = res.data
        })
        .then(() => {
          // this.getTopTen()
          this.calcGenres()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    
    deleteTopTen(i) {
      axios({
        method: "delete",
        url: `${API_URL}/movies/profiles/${this.profileId}/topten/${i}/`,
      })
        .then((res) => {
          this.profile = res.data
        })
        .then(() => {
          this.getProfile()
          this.calcGenres()
        })
        .catch((err) => {
          console.log(err)
        })
      this.getTopTen()
    },
    switchTopTen(i) {
      axios({
        method: "put",
        url: `${API_URL}/movies/profiles/${this.profileId}/topten/${i}/`,
      })
        .then((res) => {
          this.profile = res.data
        })
        .then(() => {
          this.getProfile()
          this.calcGenres()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    calcGenres() {
      this.action = 0
      this.adventure = 0
      this.animation = 0
      this.comedy = 0
      this.crime = 0
      this.drama = 0
      this.family = 0
      this.fantasy = 0
      this.history = 0
      this.horror = 0
      this.music = 0
      this.mystery = 0
      this.romance = 0
      this.sf = 0
      this.thriller = 0
      this.war = 0
      if (this.profile.movie1 !== null) {
        this.profile.movie1_genres_info.forEach((genre) => {
          if (genre.name == "액션") {
            this.action += 10
          } else if (genre.name == "모험") {
            this.adventure += 10
          } else if (genre.name == "애니메이션") {
            this.animation += 10
          } else if (genre.name == "코미디") {
            this.comedy += 10
          } else if (genre.name == "범죄") {
            this.crime += 10
          } else if (genre.name == "드라마") {
            this.drama += 10
          } else if (genre.name == "가족") {
            this.family += 10
          } else if (genre.name == "판타지") {
            this.fantasy += 10
          } else if (genre.name == "역사") {
            this.history += 10
          } else if (genre.name == "공포") {
            this.horror += 10
          } else if (genre.name == "음악") {
            this.music += 10
          } else if (genre.name == "미스터리") {
            this.mystery += 10
          } else if (genre.name == "로맨스") {
            this.romance += 10
          } else if (genre.name == "SF") {
            this.sf += 10
          } else if (genre.name == "스릴러") {
            this.thriller += 10
          } else if (genre.name == "전쟁") {
            this.war += 10
          }
        })
      }
      if (this.profile.movie2 !== null) {
        this.profile.movie2_genres_info.forEach((genre) => {
          if (genre.name == "액션") {
            this.action += 9
          } else if (genre.name == "모험") {
            this.adventure += 9
          } else if (genre.name == "애니메이션") {
            this.animation += 9
          } else if (genre.name == "코미디") {
            this.comedy += 9
          } else if (genre.name == "범죄") {
            this.crime += 9
          } else if (genre.name == "드라마") {
            this.drama += 9
          } else if (genre.name == "가족") {
            this.family += 9
          } else if (genre.name == "판타지") {
            this.fantasy += 9
          } else if (genre.name == "역사") {
            this.history += 9
          } else if (genre.name == "공포") {
            this.horror += 9
          } else if (genre.name == "음악") {
            this.music += 9
          } else if (genre.name == "미스터리") {
            this.mystery += 9
          } else if (genre.name == "로맨스") {
            this.romance += 9
          } else if (genre.name == "SF") {
            this.sf += 9
          } else if (genre.name == "스릴러") {
            this.thriller += 9
          } else if (genre.name == "전쟁") {
            this.war += 9
          }
        })
      }
    }
  },
  created() {
    console.log('acive created')
    window.scrollTo(0, 0)
    this.getProfile()
    this.calcGenres()
  },
}
</script>
