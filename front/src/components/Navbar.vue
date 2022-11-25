<template>
  <div>
    <nav class="navbar navbar-dark bg-dark fixed-top" id="my_navbar">
      <div class="container-fluid">
        <div class="navbar-brand" @click="toHome">
          <img src="../assets\topten_logo.png" alt="logo" width="36" height="30" margin-top="5px" />
          <a class="navbar-brand">&nbsp;&nbsp;TOPTEN+</a>
        </div>
        <form class="d-flex" role="search">
          <div class="search_big_box_1">
            <div class="search_middle_box_1">
              <img class="icons" src="../assets\search_icon_gray.png" alt="" />
              <input @focus="focusinEvent" @keydown.prevent.enter="searchEnter" class="search_small_box_1" type="text"
                placeholder="Search" v-model="keyword" />
            </div>
          </div>
          <div v-if="profile" @click="clickProfile" class="profile_box">
            <h5 class="nick">{{ profile.name }}</h5>
            <img class="profile_img3" :src="require(`../assets/profile${profile.img}.png`)" alt="#" width="36"
              height="36" />
            <!-- <img v-if="profile.img === 1" class="profile_img" src="../assets\profile1.png" alt="#" width="36"
              height="36" />
            <img v-if="profile.img === 2" class="profile_img" src="../assets\profile2.png" alt="#" width="36"
              height="36" />
            <img v-if="profile.img === 3" class="profile_img" src="../assets\profile3.png" alt="#" width="36"
              height="36" />
            <img v-if="profile.img === 4" class="profile_img" src="../assets\profile4.png" alt="#" width="36"
              height="36" />
            <img v-if="profile.img === 5" class="profile_img" src="../assets\profile5.png" alt="#" width="36"
              height="36" />
            <img v-if="profile.img === 6" class="profile_img" src="../assets\profile6.png" alt="#" width="36"
              height="36" />
            <img v-if="profile.img === 7" class="profile_img" src="../assets\profile7.png" alt="#" width="36"
              height="36" />
            <img v-if="profile.img === 8" class="profile_img" src="../assets\profile8.png" alt="#" width="36"
              height="36" />
            <img v-if="profile.img === 9" class="profile_img" src="../assets\profile9.png" alt="#" width="36"
              height="36" /> -->
          </div>
          <div v-else @click="clickProfile" class="profile_box">
            <img class="profile_img" src="../assets\add_profile.png" alt="#" width="36" height="36" />
          </div>
        </form>
        <div class="profile_slide nosee">
          <li @click="profileAdd">프로필 추가</li>
          <li @click="profileSelect">프로필 전환</li>
          <li>고객센터</li>
          <li class="last_list" @click="logOut">로그아웃</li>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
import axios from "axios"

const API_URL = "http://127.0.0.1:8000"

export default {
  name: "NavBar",
  data() {
    return {
      keyword: null,
      searched_movies: [],
      profile: null,
    }
  },
  methods: {
    profileAdd() {
      this.$router.push({ name: "newprofile" })
    },
    toHome() {
      this.$router.push({ name: "home" }).catch(() => { })
    },
    clickProfile() {
      console.log(event.target.parentElement)
      document.querySelector(".profile_slide").classList.toggle("nosee")
    },
    focusinEvent() {
      const newSrc =
        "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACIAAAAiCAYAAAA6RwvCAAAABHNCSVQICAgIfAhkiAAAAhNJREFUWEftl4FNw0AMRZsJYAPKBMAEhAmACYAJKBMQJgAmICPABLQTwAakEwAThP8ln+Q6l8RXSCgSliySxue82D77yCYbItmGcEz+Fkhd1/uI3BmUf6nb0A/oK/QR+pRlWfWd6HZGRABu8YLc8ZISNlcAImCytIIA4hzeCMGv9wohjgDDSCVJFEQgHoynJe7vJB3h0QkuqDvKdi2YBoik41lF4hPXBb6SEA2BPSM2g16rhxWuD1LSFAOZw8mhOCVE7gl1JIo3WFd487MCItF4UYtZfNFItESHtpfyjCna9UbFgmhHSziZer+IdpKmd7XmAj5Kjw8LotOSFI3wMsCwrxzL/T1AWD+9YkEYzi1ZxW1IsCQBCOsiFO4CPnKPAwtSq0W/CrIxEdE14s6vDv1P1QgLi22dUkGTmhIgpljzpsBOUSMs3l6xNWIdJTUlE42k7R/rrCXwOfKDuHoBIOy6pI+IgXB2MC1hGxOogLJmGiNe0sF0cvgFcW/bsKBt+vLwMzcwhOBvesTnuKdaYV3QLgofsW8/KsrcoUM94mM+9G8L3BA4dFbCsB/1Hpb6TmhhxHM36VRZIJ5VSk5b01lp54JxHZ5lmLEGmIapouBL5nqLii1TuGfsOiPjAunLh32+DswgIARLhRkMJBVmUJAUmMFBOmBWmt4oIBGYxqF8NBAFwyY5s/8ZjArS1Qb+QWx0vgBNSfcj+ggjkQAAAABJRU5ErkJggg=="

      event.target.parentElement.firstElementChild.setAttribute("src", newSrc)
      event.target.parentElement.classList.toggle("box_focused")
    },
    searchEnter() {
      this.$store.dispatch("searchKeyword", this.keyword)
      this.$router.push({ name: 'search' }).catch(() => { })
      this.keyword = null
    },
    closeMovie() {
      document.querySelector('.video_box').classList.add("nosee")
    },
    logOut() {
      this.$store.dispatch("logOut", null)
      this.$router.push({ name: 'login' })
    },
    profileSelect() {
      this.$router.push({ name: 'profiles' })
    },
    getProfile() {
      if (this.$store.state.profile_id !== null) {
        axios({
          method: "get",
          url: `${API_URL}/movies/profiles/${this.$store.state.profile_id}`,
        })
          .then((res) => {
            this.profile = res.data
          })
          .catch((err) => {
            console.log(err)
          })
      }
    }
  },
  watch: {
    $route() {
      document.querySelector(".profile_slide").classList.add("nosee")
      this.getProfile()
    },
  },
}
</script>

<style>
#my_navbar {
  background-color: #141517 !important;
  height: 80px;
  /* border-bottom: 1px solid #4E4E4E; */
}

.navbar-brand {
  color: #de2a60 !important;
  font-size: 30px !important;
  font-family: SB;
}

.profile_box {
  display: flex;
  margin-left: 40px;
  padding-left: 10px;
  padding-right: 20px;
  width: 100%;
}

.profile_box>h5 {
  margin: auto;
  margin-right: 10px;
}

.search_box {
  border: 1px solid grey !important;
  background-color: #30333e !important;
  color: white !important;
}

.search_box:focus {
  border: 1px solid grey !important;
  outline-style: none;
}

.profile_slide {
  position: absolute;
  top: 60px;
  right: 10px;
  width: 140px;
  height: 160px;
  border-radius: 6px;
  background-color: #30333e;
  text-align: center;
}

.profile_slide>li {
  position: relative;
  margin-top: 10px;
  border-bottom: 1px solid rgb(80, 80, 80);
  width: 120px;
  padding: 0px;
  padding-bottom: 4px;
  margin-left: 10px;
  font-size: 16px;
  color: rgb(196, 196, 196);
}

.profile_slide li:hover {
  cursor: pointer;
  color: white;
}

.nosee {
  display: none;
}

.last_list {
  border-bottom: 1px solid #30333e !important;
}

.search_big_box_1 {
  display: flex;
  flex-direction: column;
  /* justify-content: center; */
  /* align-items: center; */
  margin-left: 300px;
  width: 100%;
  height: 100%;
  padding-top: 0px;
}

.search_middle_box_1 {
  width: 220px;
  height: 44px;
  border-radius: 6px;
  display: flex;
  background-color: #30333e;
}

.search_small_box_1 {
  border: none;
  outline: none;
  margin-left: 4px;
  margin-top: 2px;
  background-color: #30333e;
  color: white;
}

.nick {
  display: inline;
  width: 100%;
  justify-content: right;
}

.profile_img3 {
  width: 40px;
  height: 40px;
}
</style>
