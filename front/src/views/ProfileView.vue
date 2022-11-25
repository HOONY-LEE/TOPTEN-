<template>
  <div>
    <h1>프로필</h1>
    <div class="profile_container">
      <div class="left_container container lay">

        <!-- 내 프로필 -->
        <div v-if="this.myProfileId === this.profileId">
          <h3>나의 TOP10 순위</h3><br>

          <div class="my_topten_container lay3">
            <div v-if="profile.movie1" class="top_ten_unit lay2">
              <div class="unit_left lay3">
                <h6>[1] {{ movie1.title.substring(0, 10) }}</h6>
                <img :src="`https://image.tmdb.org/t/p/original/${movie1.poster_path}`" alt="" />
              </div>
              <div class="unit_right lay3">
                <button class="btns">TOP10</button>
                <button class="btns delete_btn" @click="deleteTopTen(1)">X</button>
                <button class="btns" v-if="profile.movie1" @click="switchTopTen(1)">DOWN</button>
              </div>
            </div>
            <div v-if="profile.movie2" class="top_ten_unit lay2">
              <div class="unit_left lay3">
                <h6>[2] {{ movie2.title.substring(0, 10) }}</h6>
                <img :src="`https://image.tmdb.org/t/p/original/${movie2.poster_path}`" alt="" />
              </div>
              <div class="unit_right lay3">
                <button class="btns" @click="switchTopTen(1)">UP</button>
                <button class="btns delete_btn" @click="deleteTopTen(2)">X</button>
                <button class="btns" v-if="profile.movie2" @click="switchTopTen(2)">DOWN</button>
              </div>
            </div>
            <div v-if="profile.movie3" class="top_ten_unit lay2">
              <div class="unit_left lay3">
                <h6>[3] {{ movie3.title.substring(0, 10) }}</h6>
                <img :src="`https://image.tmdb.org/t/p/original/${movie3.poster_path}`" alt="" />
              </div>
              <div class="unit_right lay3">
                <button class="btns" @click="switchTopTen(2)">UP</button>
                <button class="btns delete_btn" @click="deleteTopTen(3)">X</button>
                <button class="btns" v-if="profile.movie3" @click="switchTopTen(3)">DOWN</button>
              </div>
            </div>
            <div v-if="profile.movie4" class="top_ten_unit lay2">
              <div class="unit_left lay3">
                <h6>[4] {{ movie4.title.substring(0, 10) }}</h6>
                <img :src="`https://image.tmdb.org/t/p/original/${movie4.poster_path}`" alt="" />
              </div>
              <div class="unit_right lay3">
                <button class="btns" @click="switchTopTen(3)">UP</button>
                <button class="btns delete_btn" @click="deleteTopTen(4)">X</button>
                <button class="btns" v-if="profile.movie4" @click="switchTopTen(4)">DOWN</button>
              </div>
            </div>
            <div v-if="profile.movie5" class="top_ten_unit lay2">
              <div class="unit_left lay3">
                <h6>[5] {{ movie5.title.substring(0, 10) }}</h6>
                <img :src="`https://image.tmdb.org/t/p/original/${movie5.poster_path}`" alt="" />
              </div>
              <div class="unit_right lay3">
                <button class="btns" @click="switchTopTen(4)">UP</button>
                <button class="btns delete_btn" @click="deleteTopTen(5)">X</button>
                <button class="btns" v-if="profile.movie5" @click="switchTopTen(5)">DOWN</button>
              </div>
            </div>
            <div v-if="profile.movie6" class="top_ten_unit lay2">
              <div class="unit_left lay3">
                <h6>[6] {{ movie2.title.substring(0, 10) }}</h6>
                <img :src="`https://image.tmdb.org/t/p/original/${movie6.poster_path}`" alt="" />
              </div>
              <div class="unit_right lay3">
                <button class="btns" @click="switchTopTen(5)">UP</button>
                <button class="btns delete_btn" @click="deleteTopTen(6)">X</button>
                <button class="btns" v-if="profile.movie6" @click="switchTopTen(6)">DOWN</button>
              </div>
            </div>
            <div v-if="profile.movie7" class="top_ten_unit lay2">
              <div class="unit_left lay3">
                <h6>[7] {{ movie7.title.substring(0, 10) }}</h6>
                <img :src="`https://image.tmdb.org/t/p/original/${movie7.poster_path}`" alt="" />
              </div>
              <div class="unit_right lay3">
                <button class="btns" @click="switchTopTen(6)">UP</button>
                <button class="btns delete_btn" @click="deleteTopTen(7)">X</button>
                <button class="btns" v-if="profile.movie7" @click="switchTopTen(7)">DOWN</button>
              </div>
            </div>
            <div v-if="profile.movie8" class="top_ten_unit lay2">
              <div class="unit_left lay3">
                <h6>[8] {{ movie8.title.substring(0, 10) }}</h6>
                <img :src="`https://image.tmdb.org/t/p/original/${movie8.poster_path}`" alt="" />
              </div>
              <div class="unit_right lay3">
                <button class="btns" @click="switchTopTen(7)">UP</button>
                <button class="btns delete_btn" @click="deleteTopTen(8)">X</button>
                <button class="btns" v-if="profile.movie8" @click="switchTopTen(8)">DOWN</button>
              </div>
            </div>
            <div v-if="profile.movie9" class="top_ten_unit lay2">
              <div class="unit_left lay3">
                <h6>[9] {{ movie9.title.substring(0, 10) }}</h6>
                <img :src="`https://image.tmdb.org/t/p/original/${movie9.poster_path}`" alt="" />
              </div>
              <div class="unit_right lay3">
                <button class="btns" @click="switchTopTen(8)">UP</button>
                <button class="btns delete_btn" @click="deleteTopTen(9)">X</button>
                <button class="btns" v-if="profile.movie9" @click="switchTopTen(9)">DOWN</button>
              </div>
            </div>
            <div v-if="profile.movie10" class="top_ten_unit lay2">
              <div class="unit_left lay3">
                <h6>[10] {{ movie10.title.substring(0, 10) }}</h6>
                <img :src="`https://image.tmdb.org/t/p/original/${movie10.poster_path}`" alt="" />
              </div>
              <div class="unit_right lay3">
                <button class="btns" @click="switchTopTen(9)">UP</button>
                <button class="btns delete_btn" @click="deleteTopTen(10)">X</button>
                <button class="btns">TOP10</button>
              </div>
            </div>
          </div>
        </div>


        <!-- 다른 사람 프로필 -->
        <div>
          <div v-if="this.myProfileId !== this.profileId">

            <h3>TOP10 순위</h3><br>

            <div class="my_topten_container lay3">


              <div v-if="profile.movie1" class="top_ten_unit lay2">
                <div class="unit_left lay3">
                  <h6>[1] {{ movie1.title.substring(0, 10) }}</h6>
                  <img :src="`https://image.tmdb.org/t/p/original/${movie1.poster_path}`" alt="" />
                </div>
              </div>

              <div v-if="profile.movie2" class="top_ten_unit lay2">
                <div class="unit_left lay3">
                  <h6>[2] {{ movie2.title.substring(0, 10) }}</h6>
                  <img :src="`https://image.tmdb.org/t/p/original/${movie2.poster_path}`" alt="" />
                </div>
              </div>

              <div v-if="profile.movie3" class="top_ten_unit lay2">
                <div class="unit_left lay3">
                  <h6>[3] {{ movie3.title.substring(0, 10) }}</h6>
                  <img :src="`https://image.tmdb.org/t/p/original/${movie3.poster_path}`" alt="" />
                </div>
              </div>

              <div v-if="profile.movie4" class="top_ten_unit lay2">
                <div class="unit_left lay3">
                  <h6>[4] {{ movie4.title.substring(0, 10) }}</h6>
                  <img :src="`https://image.tmdb.org/t/p/original/${movie4.poster_path}`" alt="" />
                </div>
              </div>

              <div v-if="profile.movie5" class="top_ten_unit lay2">
                <div class="unit_left lay3">
                  <h6>[5] {{ movie5.title.substring(0, 10) }}</h6>
                  <img :src="`https://image.tmdb.org/t/p/original/${movie5.poster_path}`" alt="" />
                </div>
              </div>

              <div v-if="profile.movie6" class="top_ten_unit lay2">
                <div class="unit_left lay3">
                  <h6>[6] {{ movie2.title.substring(0, 10) }}</h6>
                  <img :src="`https://image.tmdb.org/t/p/original/${movie6.poster_path}`" alt="" />
                </div>
              </div>

              <div v-if="profile.movie7" class="top_ten_unit lay2">
                <div class="unit_left lay3">
                  <h6>[7] {{ movie7.title.substring(0, 10) }}</h6>
                  <img :src="`https://image.tmdb.org/t/p/original/${movie7.poster_path}`" alt="" />
                </div>
              </div>

              <div v-if="profile.movie8" class="top_ten_unit lay2">
                <div class="unit_left lay3">
                  <h6>[8] {{ movie8.title.substring(0, 10) }}</h6>
                  <img :src="`https://image.tmdb.org/t/p/original/${movie8.poster_path}`" alt="" />
                </div>
              </div>

              <div v-if="profile.movie9" class="top_ten_unit lay2">
                <div class="unit_left lay3">
                  <h6>[9] {{ movie9.title.substring(0, 10) }}</h6>
                  <img :src="`https://image.tmdb.org/t/p/original/${movie9.poster_path}`" alt="" />
                </div>
              </div>

              <div v-if="profile.movie10" class="top_ten_unit lay2">
                <div class="unit_left lay3">
                  <h6>[10] {{ movie10.title.substring(0, 10) }}</h6>
                  <img :src="`https://image.tmdb.org/t/p/original/${movie10.poster_path}`" alt="" />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>





      <!-- 오른쪽 박스 -->
      <div class="right_container container lay">

        <div>

          <!-- 내 프로필-->
          <div v-if="this.myProfileId === this.profileId">

            <h3>팔로워</h3>
            <div class="genre_box lay2">
              <div class="profile_component_box lay2">
                <FollowingComponentList :followingProfileId="followingProfileId"
                  v-for="(followingProfileId, index) in profile.followings" :key="index">
                </FollowingComponentList>
              </div>
            </div>



            <h3>팔로잉</h3>
            <div class="genre_box lay2">
              <div class="profile_component_box lay2">
                <FollowerComponentList :followerProfileId="followerProfileId"
                  v-for="(followerProfileId, index) in profile.followers" :key="index">
                </FollowerComponentList>
              </div>
            </div>


            <h3>장르데이터</h3>
            <div class="genre_box lay2">
              <p v-if="action">/액션 : {{ action }}/</p>
              <p v-if="adventure">/모험 : {{ adventure }}/</p>
              <p v-if="animation">/애니메이션 : {{ animation }}/</p>
              <p v-if="comedy">/코미디 : {{ comedy }}/</p>
              <p v-if="crime">/범죄 : {{ crime }}/</p>
              <p v-if="drama">/드라마 : {{ drama }}/</p>
              <p v-if="family">/가족 : {{ family }}/</p>
              <p v-if="fantasy">/판타지 : {{ fantasy }}/</p>
              <p v-if="history">/역사 : {{ history }}/</p>
              <p v-if="horror">/공포 : {{ horror }}/</p>
              <p v-if="music">/음악 : {{ music }}/</p>
              <p v-if="mystery">/미스터리 : {{ mystery }}/</p>
              <p v-if="romance">/로맨스 : {{ romance }}/</p>
              <p v-if="sf">/SF : {{ sf }}/</p>
              <p v-if="thriller">/스릴러 : {{ thriller }}/</p>
              <p v-if="war">/전쟁 : {{ war }}/</p>
            </div>


            <h3>받은 메시지</h3>
            <div class="genre_box lay2">
              <div class="second_box lay1">
                <FromCommentComponentList :comment="comment" v-for="(comment, index) in profile.message_recive"
                  :key="index" :index="index">
                </FromCommentComponentList>
              </div>
            </div>


            <h3>보낸 메시지</h3>
            <div class="genre_box lay2">
              <div class="second_box lay1">
                <ToCommentComponentList :comment="comment" v-for="(comment, index) in profile.message_send" :key="index"
                  :index="index">
                </ToCommentComponentList>
              </div>
            </div>

          </div>


        </div>



        <!-- 내 프로필 -->
        <div v-if="this.myProfileId === this.profileId">

        </div>
        <div v-else>
          <button class="follow_btn" @click="follow">팔로우</button>

          <h3>팔로잉</h3>
          <div class="genre_box lay2">
            <div class="profile_component_box lay2">
              <FollowerComponentList :followerProfileId="followerProfileId"
                v-for="(followerProfileId, index) in profile.followers" :key="index">
              </FollowerComponentList>
            </div>
          </div>


          <h3>팔로워</h3>
          <div class="genre_box lay2">
            <div class="profile_component_box lay2">
              <FollowingComponentList :followingProfileId="followingProfileId"
                v-for="(followingProfileId, index) in profile.followings" :key="index">
              </FollowingComponentList>
            </div>
          </div>



          <h3>장르데이터</h3>
          <div class="genre_box lay2">
            <p v-if="action">/액션 : {{ action }}/</p>
            <p v-if="adventure">/모험 : {{ adventure }}/</p>
            <p v-if="animation">/애니메이션 : {{ animation }}/</p>
            <p v-if="comedy">/코미디 : {{ comedy }}/</p>
            <p v-if="crime">/범죄 : {{ crime }}/</p>
            <p v-if="drama">/드라마 : {{ drama }}/</p>
            <p v-if="family">/가족 : {{ family }}/</p>
            <p v-if="fantasy">/판타지 : {{ fantasy }}/</p>
            <p v-if="history">/역사 : {{ history }}/</p>
            <p v-if="horror">/공포 : {{ horror }}/</p>
            <p v-if="music">/음악 : {{ music }}/</p>
            <p v-if="mystery">/미스터리 : {{ mystery }}/</p>
            <p v-if="romance">/로맨스 : {{ romance }}/</p>
            <p v-if="sf">/SF : {{ sf }}/</p>
            <p v-if="thriller">/스릴러 : {{ thriller }}/</p>
            <p v-if="war">/전쟁 : {{ war }}/</p>
          </div>


          <h3>메시지 작성</h3>
          <div class="genre_box lay2">
            <div>
              <input class="send_input" v-model="message_content" />
              <button class="follow_btn" @click="writeMessage">메시지 보내기</button>
            </div>
          </div>


        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios"
import FollowingComponentList from "@/components/FollowingComponentList.vue"
import FollowerComponentList from "@/components/FollowerComponentList.vue"
import FromCommentComponentList from '@/components/FromCommentComponentList.vue'
import ToCommentComponentList from '@/components/ToCommentComponentList.vue'
// import FollowButtonComponent from '@/components/FollowButtonComponent.vue'


const API_URL = "http://127.0.0.1:8000"

export default {
  name: "ProfileView",
  components: { FollowingComponentList, FollowerComponentList, FromCommentComponentList, ToCommentComponentList },
  data() {
    return {
      myProfileId: this.$store.state.profile_id,
      profileId: this.$route.params.profileId,
      myProfile: null,
      profile: null,
      movie1: null,
      movie2: null,
      movie3: null,
      movie4: null,
      movie5: null,
      movie6: null,
      movie7: null,
      movie8: null,
      movie9: null,
      movie10: null,
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
      message_content: null,
      followCheck: null,
    }
  },
  methods: {
    getProfile() {
      console.log('active getProfile')
      axios({
        method: "get",
        url: `${API_URL}/movies/profiles/${this.profileId}`,
      })
        .then((res) => {
          this.profile = res.data
        })
        .then(() => {
          this.getTopTen()
          this.calcGenres()
        })
        .catch((err) => {
          console.log(err)
        })
      axios({
        method: "get",
        url: `${API_URL}/movies/profiles/${this.myProfileId}`,
      })
        .then((res) => {
          this.myProfile = res.data
        })
        .then(() => {
          this.getTopTen()
          this.calcGenres()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getTopTen() {
      console.log(this.profile)
      if (this.profile.movie1 !== null) {
        axios({
          method: "get",
          url: `${API_URL}/movies/${this.profile.movie1}/`,
        })
          .then((res) => {
            this.movie1 = res.data
          })
          .catch((err) => {
            console.log(err)
          })
      }
      if (this.profile.movie2 !== null) {
        axios({
          method: "get",
          url: `${API_URL}/movies/${this.profile.movie2}/`,
        })
          .then((res) => {
            this.movie2 = res.data
          })
          .catch((err) => {
            console.log(err)
          })
      }
      if (this.profile.movie3 !== null) {
        axios({
          method: "get",
          url: `${API_URL}/movies/${this.profile.movie3}/`,
        })
          .then((res) => {
            this.movie3 = res.data
          })
          .catch((err) => {
            console.log(err)
          })
      }
      if (this.profile.movie4 !== null) {
        axios({
          method: "get",
          url: `${API_URL}/movies/${this.profile.movie4}/`,
        })
          .then((res) => {
            this.movie4 = res.data
          })
          .catch((err) => {
            console.log(err)
          })
        if (this.profile.movie5 !== null) {
          axios({
            method: "get",
            url: `${API_URL}/movies/${this.profile.movie5}/`,
          })
            .then((res) => {
              this.movie5 = res.data
            })
            .catch((err) => {
              console.log(err)
            })
        }
        if (this.profile.movie6 !== null) {
          axios({
            method: "get",
            url: `${API_URL}/movies/${this.profile.movie6}/`,
          })
            .then((res) => {
              this.movie6 = res.data
            })
            .catch((err) => {
              console.log(err)
            })
        }
        if (this.profile.movie7 !== null) {
          axios({
            method: "get",
            url: `${API_URL}/movies/${this.profile.movie7}/`,
          })
            .then((res) => {
              this.movie7 = res.data
            })
            .catch((err) => {
              console.log(err)
            })
        }
        if (this.profile.movie8 !== null) {
          axios({
            method: "get",
            url: `${API_URL}/movies/${this.profile.movie8}/`,
          })
            .then((res) => {
              this.movie8 = res.data
            })
            .catch((err) => {
              console.log(err)
            })
        }
        if (this.profile.movie9 !== null) {
          axios({
            method: "get",
            url: `${API_URL}/movies/${this.profile.movie9}/`,
          })
            .then((res) => {
              this.movie9 = res.data
            })
            .catch((err) => {
              console.log(err)
            })
        }
        if (this.profile.movie10 !== null) {
          axios({
            method: "get",
            url: `${API_URL}/movies/${this.profile.movie10}/`,
          })
            .then((res) => {
              this.movie10 = res.data
            })
            .catch((err) => {
              console.log(err)
            })
        }
      }
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
          this.getTopTen()
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
          this.getTopTen()
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
      if (this.profile.movie3 !== null) {
        this.profile.movie3_genres_info.forEach((genre) => {
          if (genre.name == "액션") {
            this.action += 8
          } else if (genre.name == "모험") {
            this.adventure += 8
          } else if (genre.name == "애니메이션") {
            this.animation += 8
          } else if (genre.name == "코미디") {
            this.comedy += 8
          } else if (genre.name == "범죄") {
            this.crime += 8
          } else if (genre.name == "드라마") {
            this.drama += 8
          } else if (genre.name == "가족") {
            this.family += 8
          } else if (genre.name == "판타지") {
            this.fantasy += 8
          } else if (genre.name == "역사") {
            this.history += 8
          } else if (genre.name == "공포") {
            this.horror += 8
          } else if (genre.name == "음악") {
            this.music += 8
          } else if (genre.name == "미스터리") {
            this.mystery += 8
          } else if (genre.name == "로맨스") {
            this.romance += 8
          } else if (genre.name == "SF") {
            this.sf += 8
          } else if (genre.name == "스릴러") {
            this.thriller += 8
          } else if (genre.name == "전쟁") {
            this.war += 8
          }
        })
      }
      if (this.profile.movie4 !== null) {
        this.profile.movie4_genres_info.forEach((genre) => {
          if (genre.name == "액션") {
            this.action += 7
          } else if (genre.name == "모험") {
            this.adventure += 7
          } else if (genre.name == "애니메이션") {
            this.animation += 7
          } else if (genre.name == "코미디") {
            this.comedy += 7
          } else if (genre.name == "범죄") {
            this.crime += 7
          } else if (genre.name == "드라마") {
            this.drama += 7
          } else if (genre.name == "가족") {
            this.family += 7
          } else if (genre.name == "판타지") {
            this.fantasy += 7
          } else if (genre.name == "역사") {
            this.history += 7
          } else if (genre.name == "공포") {
            this.horror += 7
          } else if (genre.name == "음악") {
            this.music += 7
          } else if (genre.name == "미스터리") {
            this.mystery += 7
          } else if (genre.name == "로맨스") {
            this.romance += 7
          } else if (genre.name == "SF") {
            this.sf += 7
          } else if (genre.name == "스릴러") {
            this.thriller += 7
          } else if (genre.name == "전쟁") {
            this.war += 7
          }
        })
      }
      if (this.profile.movie5 !== null) {
        this.profile.movie5_genres_info.forEach((genre) => {
          if (genre.name == "액션") {
            this.action += 6
          } else if (genre.name == "모험") {
            this.adventure += 6
          } else if (genre.name == "애니메이션") {
            this.animation += 6
          } else if (genre.name == "코미디") {
            this.comedy += 6
          } else if (genre.name == "범죄") {
            this.crime += 6
          } else if (genre.name == "드라마") {
            this.drama += 6
          } else if (genre.name == "가족") {
            this.family += 6
          } else if (genre.name == "판타지") {
            this.fantasy += 6
          } else if (genre.name == "역사") {
            this.history += 6
          } else if (genre.name == "공포") {
            this.horror += 6
          } else if (genre.name == "음악") {
            this.music += 6
          } else if (genre.name == "미스터리") {
            this.mystery += 6
          } else if (genre.name == "로맨스") {
            this.romance += 6
          } else if (genre.name == "SF") {
            this.sf += 6
          } else if (genre.name == "스릴러") {
            this.thriller += 6
          } else if (genre.name == "전쟁") {
            this.war += 6
          }
        })
      }
      if (this.profile.movie6 !== null) {
        this.profile.movie6_genres_info.forEach((genre) => {
          if (genre.name == "액션") {
            this.action += 5
          } else if (genre.name == "모험") {
            this.adventure += 5
          } else if (genre.name == "애니메이션") {
            this.animation += 5
          } else if (genre.name == "코미디") {
            this.comedy += 5
          } else if (genre.name == "범죄") {
            this.crime += 5
          } else if (genre.name == "드라마") {
            this.drama += 5
          } else if (genre.name == "가족") {
            this.family += 5
          } else if (genre.name == "판타지") {
            this.fantasy += 5
          } else if (genre.name == "역사") {
            this.history += 5
          } else if (genre.name == "공포") {
            this.horror += 5
          } else if (genre.name == "음악") {
            this.music += 5
          } else if (genre.name == "미스터리") {
            this.mystery += 5
          } else if (genre.name == "로맨스") {
            this.romance += 5
          } else if (genre.name == "SF") {
            this.sf += 5
          } else if (genre.name == "스릴러") {
            this.thriller += 5
          } else if (genre.name == "전쟁") {
            this.war += 5
          }
        })
      }
      if (this.profile.movie7 !== null) {
        this.profile.movie7_genres_info.forEach((genre) => {
          if (genre.name == "액션") {
            this.action += 4
          } else if (genre.name == "모험") {
            this.adventure += 4
          } else if (genre.name == "애니메이션") {
            this.animation += 4
          } else if (genre.name == "코미디") {
            this.comedy += 4
          } else if (genre.name == "범죄") {
            this.crime += 4
          } else if (genre.name == "드라마") {
            this.drama += 4
          } else if (genre.name == "가족") {
            this.family += 4
          } else if (genre.name == "판타지") {
            this.fantasy += 4
          } else if (genre.name == "역사") {
            this.history += 4
          } else if (genre.name == "공포") {
            this.horror += 4
          } else if (genre.name == "음악") {
            this.music += 4
          } else if (genre.name == "미스터리") {
            this.mystery += 4
          } else if (genre.name == "로맨스") {
            this.romance += 4
          } else if (genre.name == "SF") {
            this.sf += 4
          } else if (genre.name == "스릴러") {
            this.thriller += 4
          } else if (genre.name == "전쟁") {
            this.war += 4
          }
        })
      }
      if (this.profile.movie8 !== null) {
        this.profile.movie8_genres_info.forEach((genre) => {
          if (genre.name == "액션") {
            this.action += 3
          } else if (genre.name == "모험") {
            this.adventure += 3
          } else if (genre.name == "애니메이션") {
            this.animation += 3
          } else if (genre.name == "코미디") {
            this.comedy += 3
          } else if (genre.name == "범죄") {
            this.crime += 3
          } else if (genre.name == "드라마") {
            this.drama += 3
          } else if (genre.name == "가족") {
            this.family += 3
          } else if (genre.name == "판타지") {
            this.fantasy += 3
          } else if (genre.name == "역사") {
            this.history += 3
          } else if (genre.name == "공포") {
            this.horror += 3
          } else if (genre.name == "음악") {
            this.music += 3
          } else if (genre.name == "미스터리") {
            this.mystery += 3
          } else if (genre.name == "로맨스") {
            this.romance += 3
          } else if (genre.name == "SF") {
            this.sf += 3
          } else if (genre.name == "스릴러") {
            this.thriller += 3
          } else if (genre.name == "전쟁") {
            this.war += 3
          }
        })
      }
      if (this.profile.movie9 !== null) {
        this.profile.movie9_genres_info.forEach((genre) => {
          if (genre.name == "액션") {
            this.action += 2
          } else if (genre.name == "모험") {
            this.adventure += 2
          } else if (genre.name == "애니메이션") {
            this.animation += 2
          } else if (genre.name == "코미디") {
            this.comedy += 2
          } else if (genre.name == "범죄") {
            this.crime += 2
          } else if (genre.name == "드라마") {
            this.drama += 2
          } else if (genre.name == "가족") {
            this.family += 2
          } else if (genre.name == "판타지") {
            this.fantasy += 2
          } else if (genre.name == "역사") {
            this.history += 2
          } else if (genre.name == "공포") {
            this.horror += 2
          } else if (genre.name == "음악") {
            this.music += 2
          } else if (genre.name == "미스터리") {
            this.mystery += 2
          } else if (genre.name == "로맨스") {
            this.romance += 2
          } else if (genre.name == "SF") {
            this.sf += 2
          } else if (genre.name == "스릴러") {
            this.thriller += 2
          } else if (genre.name == "전쟁") {
            this.war += 2
          }
        })
      }
      if (this.profile.movie10 !== null) {
        this.profile.movie10_genres_info.forEach((genre) => {
          if (genre.name == "액션") {
            this.action += 1
          } else if (genre.name == "모험") {
            this.adventure += 1
          } else if (genre.name == "애니메이션") {
            this.animation += 1
          } else if (genre.name == "코미디") {
            this.comedy += 1
          } else if (genre.name == "범죄") {
            this.crime += 1
          } else if (genre.name == "드라마") {
            this.drama += 1
          } else if (genre.name == "가족") {
            this.family += 1
          } else if (genre.name == "판타지") {
            this.fantasy += 1
          } else if (genre.name == "역사") {
            this.history += 1
          } else if (genre.name == "공포") {
            this.horror += 1
          } else if (genre.name == "음악") {
            this.music += 1
          } else if (genre.name == "미스터리") {
            this.mystery += 1
          } else if (genre.name == "로맨스") {
            this.romance += 1
          } else if (genre.name == "SF") {
            this.sf += 1
          } else if (genre.name == "스릴러") {
            this.thriller += 1
          } else if (genre.name == "전쟁") {
            this.war += 1
          }
        })
      }
      this.action = Math.floor(this.action * 100 / 55)
      this.adventure = Math.floor(this.adventure * 100 / 55)
      this.animation = Math.floor(this.animation * 100 / 55)
      this.comedy = Math.floor(this.comedy * 100 / 55)
      this.crime = Math.floor(this.crime * 100 / 55)
      this.drama = Math.floor(this.drama * 100 / 55)
      this.family = Math.floor(this.family * 100 / 55)
      this.fantasy = Math.floor(this.fantasy * 100 / 55)
      this.history = Math.floor(this.history * 100 / 55)
      this.horror = Math.floor(this.horror * 100 / 55)
      this.music = Math.floor(this.music * 100 / 55)
      this.mystery = Math.floor(this.mystery * 100 / 55)
      this.romance = Math.floor(this.romance * 100 / 55)
      this.sf = Math.floor(this.sf * 100 / 55)
      this.thriller = Math.floor(this.thriller * 100 / 55)
      this.war = Math.floor(this.war * 100 / 55)
    },
    writeMessage() {
      axios({
        method: "post",
        url: `${API_URL}/movies/profiles/${this.profileId}/message/${this.myProfileId}/`,
        data: {
          content: this.message_content,
        },
      })
        .then((res) => {
          console.log(res.data)
        })
        .catch((err) => {
          console.log(err)
        })
      this.message_content = null
    },
    isFollow() {
      console.log('active isFollow')
      this.getProfile()
      if (this.myProfile.followings.includes(this.profileId)) {
        this.followCheck = true
      } else {
        this.followCheck = false
      }
      console.log(this.followCheck)
    },
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
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  watch: {
    $route() {
      this.profileId = this.$route.params.profileId
      window.scrollTo(0, 0)
      this.getProfile()
    },
  },
  created() {
    window.scrollTo(0, 0)
    this.isFollow()
  }
}
</script>

<style>
.comment_text_box {
  width: 590px;
  height: 90px;
  display: flex;
}

.comment_right_box {
  width: 550px;
  height: 90px;
}

.comment_right_box>div {}

.user_name_box {
  margin-top: 20px;
  font-weight: bold;
}

.user_comment_box {}

.cover_big_box {
  margin-top: 80px;
  top: 10px;
  left: 10px;
  z-index: 10001;
  width: 100%;
  height: 1000px;
  justify-content: center;
  text-align: center;
  /* display: none; */

}

.title_big {
  margin-top: 240px;
  font-weight: 600;
}

.profile_component_box {
  width: 80%;
  margin: 20px auto;
  display: flex;
  text-align: center;
  justify-content: center;
}

.second_box {
  width: 590px;
  height: 600px;
  margin-left: 20px;
  border-radius: 6px;
  background-color: #303133;
}

.container {
  width: 100%;
  height: 10%;
  text-align: center;
  justify-content: center;
}

.profile_container {
  display: flex;
}

.my_topten_container {
  justify-content: center;
  text-align: center;
}

.top_ten_unit {
  display: flex;
  margin: 20px auto;
  padding: 20px auto;
  width: 300px;
  height: 200px;
  justify-content: center;
  background-color: #303133;
  border-radius: 8px;
  padding-bottom: 20px;

}

.unit_left {
  text-align: center;
  justify-content: center;
  padding: 0px auto;
  width: 160px;
  margin-top: 16px;
}

.unit_left img {
  width: 100px;
  height: 140px;

}

.unit_right {
  padding-top: 32px;
  display: flex;
  flex-direction: column;
}

.btns {
  width: 80px;
  height: 38px;
  margin-top: 14px;
  border-radius: 6px;
  background-color: #F82F62;
  color: white;
  border: none;
}

.delete_btn {
  border: 1.4px solid white;
  background-color: #303133;
}

.left_container {
  width: 800px;
}

.genre_box {
  display: flex;
  justify-content: center;
}

.follow_btn {
  width: 100px;
  height: 40px;
  background-color: #F82F62;
  border: none;
  color: white;
  border-radius: 6px;
  margin-bottom: 40px;

}

.send_input {
  margin-left: 20px;
  margin-right: 10px;
  width: 490px;
  height: 40px;
  background-color: gray;
  border-radius: 6px;
  color: white;

}
</style>

