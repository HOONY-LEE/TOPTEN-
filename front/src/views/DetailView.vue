<template>
  <div class="detail_container">

    <div class="detail_big_box lay2">

      <div class="backdrop_box">

        <img class="backdrop_img" :src="`https://image.tmdb.org/t/p/original/${movie.backdrop_path}`" alt="#" />
        <img class="poster_img" :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`" alt="#" />
        <div class="backdrop_text_area lay3">
          <h1>{{ movie.title }}</h1>
          <h5>{{ movie.original_title }} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [출시] {{
              movie.released_date
          }}</h5>
          <br><br>

          <div class="font_ul">
            <h4>장르 : {{ genre }}</h4>
            <h4>감독 : {{ movie.director[0].name }}</h4>
            <h4>출연진 : {{ actor }}</h4>
          </div>
          <div class="font_ul overview_box">
            <p> {{ movie.overview }} </p>
          </div>

          <button @click="playMovie" class="play_btn my_btn">감상하기</button>
          <button @click="addTopTen" class="add_btn my_btn">추가하기</button>
        </div>


        <!-- 비디오 영역 -->
        <div @click="closeMovie" class="video_box_background nosee"></div>
        <div class="video_box nosee">
          <div class="video_space">
            <!-- <button @click="closeMovie" class="close_btn">
              <h1>X</h1>
            </button> -->
          </div>
          <div class="video-wrap">
            <iframe id="video" width="100%" height="315"
              :src="`https://www.youtube.com/embed/${movie.trailer[0].key}/?autoplay=1&mute=1`" frameborder="0"
              allow="encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
          </div>
        </div>
      </div>

      <div class="recommand_title">
        <h3>추천 영화</h3>
        <h3 class="comment_title">시청자 한줄평</h3>
      </div>
      <div class="contents_area lay2">
        <div class="relative_box lay3">
          <div class="relative_movie_box">
            <div class="inner_box ">
              <img class="recommand_poster_img"
                :src="`https://image.tmdb.org/t/p/original/${movie.similar[0].poster_path}`" alt="#" />
              <div class="inner_contents_box">
                <p class="recTitle">{{ movie.similar[0].title }}</p>
                <h5>{{ movie.similar[0].release_date }}</h5>
                <p class="font_small"> {{ movie.similar[0].overview.substring(0, 86) + '...' }} </p>
              </div>
            </div>
            <div class="inner_box">
              <img class="recommand_poster_img"
                :src="`https://image.tmdb.org/t/p/original/${movie.similar[2].poster_path}`" alt="#" />
              <div class="inner_contents_box">
                <p class="recTitle">{{ movie.similar[2].title }}</p>
                <h5>{{ movie.similar[2].release_date }}</h5>
                <p class="font_small"> {{ movie.similar[2].overview.substring(0, 86) + '...' }} </p>
              </div>
            </div>
          </div>
          <div class="relative_movie_box ">
            <div class="inner_box">
              <img class="recommand_poster_img"
                :src="`https://image.tmdb.org/t/p/original/${movie.similar[1].poster_path}`" alt="#" />
              <div class="inner_contents_box">
                <p class="recTitle">{{ movie.similar[1].title }}</p>
                <h5>{{ movie.similar[1].release_date }}</h5>
                <p class="font_small"> {{ movie.similar[1].overview.substring(0, 86) + '...' }} </p>
              </div>
            </div>
            <div class="inner_box">
              <img class="recommand_poster_img"
                :src="`https://image.tmdb.org/t/p/original/${movie.similar[3].poster_path}`" alt="#" />
              <div class="inner_contents_box">
                <p class="recTitle">{{ movie.similar[3].title }}</p>
                <h5>{{ movie.similar[3].release_date }}</h5>
                <p class="font_small"> {{ movie.similar[3].overview.substring(0, 86) + '...' }} </p>
              </div>
            </div>
          </div>

        </div>
        <!-- 한줄평 공간 -->
        <div class="second_box lay1">
          <div class="comment_big_box lay2">
            <div class="comment_text_box">
              <img class="profile_img4" :src="require(`../assets/profile${profile.img}.png`)" alt="#" width="36"
                height="36" />

              <div class="comment_right_box lay3">
                <div class="user_comment_big_box lay2">
                  <div class="user_comment_mid_box" >
                    <input class="user_comment_box2" v-model="comment_content" />
                  </div>
                  
                  <button class="wirte_btn" @click="writeComment">작성</button>
                </div>
                
                
              </div>
            </div>
          </div>
          <CommentComponentList :movieId="movieId" :comment="comment" v-for="(comment, index) in comments" :key="index"
            :index="index">
          </CommentComponentList>
          <!-- 더보기 버튼 -->
          <button class="more_btn"> + 더보기</button>
        </div>
        <!-- <div>id : {{ movie.backdrop_path }}</div>
        <div>id : {{ movie.poster_path }}</div>
        <div>title : {{ movie.title }}</div>
        <div>original_title : {{ movie.original_title }}</div>
        <div>tagline : {{ movie.tagline }}</div>
        <div>released_data : {{ movie.released_date }}</div>
        <div>vote_avg : {{ movie.vote_avg }}</div>
        <div>overview : {{ movie.overview }}</div>
        <div>genres : {{ movie.genres }}</div>
        <div>genres_info : {{ movie.genres_info }}</div>
        <br>
        <div>actor : {{ movie.actor }}</div>
        <br>
        <div>director : {{ movie.director }}</div>
        <br>
        <div>trailer : {{ movie.trailer }}</div>
        <br>
        <div>watch : {{ movie.watch }}</div>
        <br>
        <div>similar :{{ movie.similar }}</div> -->
      </div>



    </div>



  </div>
</template>
<script>
import axios from "axios"
import CommentComponentList from '@/components/CommentComponentList.vue'


const API_URL = "http://127.0.0.1:8000"


export default {
  name: "DetailView",
  components: { CommentComponentList },
  data() {
    return {
      movieId: this.$route.params.movieId,
      profileId: this.$store.state.profile_id,
      movie: null,
      profile: null,
      actors: [],
      genres: [],
      similarList: [],
      comments: null,
      comment_content: null,
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
    }
  },
  computed: {
    overview() {
      return this.movie.similar[0].overview.substring(0, 50) + '...'
    },

    actor() {
      const movieList = this.movie.actor

      movieList.forEach((element, index) => {
        if (index !== movieList.length - 1) {
          this.actors += JSON.stringify(element.name).replaceAll('"', '') + ', '
        } else {
          this.actors += JSON.stringify(element.name).replaceAll('"', '')
        }

      });
      return this.actors
    },
    genre() {
      const genreList = this.movie.genres_info
      genreList.forEach((element, index) => {
        if (index !== genreList.length - 1) {
          this.genres += JSON.stringify(element.name).replaceAll('"', '') + ', '
        } else {
          this.genres += JSON.stringify(element.name).replaceAll('"', '')
        }

      });
      return this.genres
    },
  },
  methods: {

    getDetail() {
      axios({
        method: "get",
        url: `${API_URL}/movies/${this.movieId}`,
        params: {
          page: 1,
        },
      })
        .then((res) => {
          this.movie = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    playMovie() {
      document.querySelector('.video_box').classList.toggle("nosee")
      document.querySelector('.video_box_background').classList.toggle("nosee")
    },
    closeMovie() {
      document.querySelector('.video_box').classList.add("nosee")
      document.querySelector('.video_box_background').classList.add("nosee")
    },
    addTopTen() {
      axios({
        method: "put",
        url: `${API_URL}/movies/${this.movieId}/topten/${this.profileId}/`,
      })
        .then((res) => {
          console.log(res)
          alert('TOPTEN에 추가되었습니다.')
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getComments() {
      axios({
        method: "get",
        url: `${API_URL}/movies/${this.movieId}/comments/`,
      })
        .then((res) => {
          // console.log(res.data)
          this.comments = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    writeComment() {
      axios({
        method: "post",
        url: `${API_URL}/movies/${this.movieId}/comments/${this.profileId}/`,
        data: {
          content: this.comment_content,
        },
      })
        .then((res) => {
          console.log(res.data)
        })
        .then(() => {
          this.getComments()
        })
        .catch((err) => {
          console.log(err)
        })
      this.comment_content = null
    },
    getProfile() {
      axios({
        method: "get",
        url: `${API_URL}/movies/profiles/${this.profileId}/`,
      })
        .then((res) => {
          this.profile = res.data
          this.getTopTen()
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
  },
  created() {
    window.scrollTo(0, 0)
    this.getDetail()
    this.getComments()
    this.getProfile()
    console.log('프로필 데이터 확인')
    console.log(this.profile.movie1)
  }
}
</script>

<style>
.detail_container {
  margin-left: -70px;
}

.detail_big_box {
  margin-left: 0px;
  margin-top: -30px;
  width: 100%;
  height: 800px;
}

.backdrop_box {
  width: 1651px;
  height: 100%;
}

.backdrop_img {
  width: 100%;
  height: 100%;
  filter: brightness(30%);
  opacity: 0.5;
}

.poster_img {
  position: absolute;
  width: 500px;
  height: 680px;
  top: 130px;
  left: 280px;
}

.backdrop_text_area {
  position: absolute;
  top: 130px;
  left: 820px;
  width: 1060px;
  height: 678px;
}

.backdrop_text_area>h1 {
  font-weight: 900;
  font-size: 60px;
}

h5 {
  color: #CED2D8;
}

.font_ul {
  font-family: 'AppleSDUL';
  font-weight: lighter;
  font-size: 26px;
}

.overview_box {
  margin-top: 60px;
}

.my_btn {
  position: absolute;
  right: 14px;
  bottom: 10px;
  border-radius: 6px;
  border: none;
  width: 240px;
  height: 60px;
  color: white;
  font-size: 20px;
}

.play_btn {
  background-color: #de2a60;
  right: 280px;
}

.add_btn {
  background-color: grey;
  margin-left: 20px;
}

.video_box {
  position: absolute;
  width: 1440px;
  height: 920px;
  border-radius: 16px;
  top: 40px;
  left: 180px;
  background-color: black;
  color: white;
  z-index: 99999;
  /* display: none; */
}

.video_box_background {
  position: absolute;
  width: 100%;
  height: 200%;
  top: 0px;
  left: 0px;
  background-color: rgba(10, 10, 10, 0.7);
  filter: brightness(30%);
  filter: blur(40%);
  opacity: 0.5;
  z-index: 99995;

}

.video_space {
  height: 50px;
}

.video-wrap {
  position: relative;
  padding-bottom: 56.25%;
  padding-top: 30px;
  height: 0;
  overflow: hidden;
}

.video-wrap iframe,
.video-wrap object,
.video-wrap embed {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.close_btn {
  position: absolute;
  top: 10px;
  right: 10px;
}

.relative_box {
  margin-left: 20px;
  display: flex;
  width: 1000px;
  height: 600px;
}

.relative_movie_box {
  width: 500px;
  height: 600px;
}

.inner_box {
  display: flex;
  margin-right: 20px;
  margin-bottom: 20px;
  ;
  width: 480px;
  height: 280px;
  background-color: #303133;
  border-radius: 6px;
}

.recommand_title {
  height: 40px;
  margin-top: 20px;
  margin-left: 28px;
  display: flex;
}

.recommand_poster_img {
  border-radius: 4px;
  margin: 16px;
  width: 190px;
  height: 250px;
}

.inner_contents_box {
  margin: 18px 10px 0px 10px;
}

.recTitle {
  font-size: 24px;
  font-weight: 600;
}

.font_small {
  font-size: 18px !important;
  font-weight: 200 !important;
  padding-top: 6px !important;
}

.second_box {
  width: 590px;
  height: 600px;
  margin-left: 20px;
  border-radius: 6px;
  background-color: #303133;
}

.comment_title {
  margin-left: 910px;
}

.contents_area {
  display: flex;
}

.profile_img4 {
  margin: 20px;
  width: 50px;
  height: 50px;
}

.comment_text_box {
  width: 590px;
  height: 90px;
  display: flex;
}

.comment_right_box {
  
  width: 550px;
  height: 90px;
}


.user_name_box {
  margin-top: 20px;
  font-weight: bold;
}
.user_comment_big_box {
  display: flex;
  width: 500px;
  height: 50px;
  margin-top: 20px;
}

.user_comment_box2 {
  margin-left: 20px;
  margin-top: 8px;
  border: none;
  outline: none;
  background-color: gray;
  color: white;
  width: 370px;
}

.more_btn {
  position: absolute;
  top: 1492px;
  background-color: #303133ab;
  border: 1px solid gray;
  width: 590px;
  height: 48px;
  border-bottom-left-radius: 6px;
  border-bottom-right-radius: 6px;
  color: white;
}
.user_comment_mid_box {
  width: 400px;
  height: 44px;
  background-color: gray;
  border-radius: 50px;
}
.wirte_btn {
  border-radius: 4px;
  margin-top: 2px;
  margin-left: 8px;
  height: 38px;
  width: 64px;
  color: white;
  background-color: #F82F62;
  border: none;
}
</style>
