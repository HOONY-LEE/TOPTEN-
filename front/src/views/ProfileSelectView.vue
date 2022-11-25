<template>
  <div>
    <div class="cover_container">
      <nav class="navbar navbar-dark bg-dark fixed-top" id="my_navbar">
        <div class="container-fluid">
          <div class="navbar-brand">
            <img src="../assets\topten_logo.png" alt="logo" width="36" height="30" margin-top="5px" />
            <a class="navbar-brand">&nbsp;&nbsp;TOPTEN+</a>
          </div>
          <button class="login_btn" @click="profileMangeMode">프로필 관리</button>
        </div>
      </nav>


      <div class="cover_big_box">
        <br>
        <h1 class="title_big">프로필을 선택해주세요<br></h1>
        <h1 class="title_big nosee">삭제할 프로필을 선택하세요<br></h1>
        <div class="profile_component_box lay2">
          <ProfileComponentList :profile="profile" v-for="(profile, index) in profiles" :key="index"
            @refresh="getProfiles">
          </ProfileComponentList>
          <div class="add_profile_box lay2" @click="newProfile">
            <img class="add_profile_img" src="../assets\add_profile.png" alt="#" width="36" height="36" />
            <div class="add_profile_text">프로필 생성</div>
          </div>


        </div>

      </div>
    </div>

  </div>
</template>

<script>
import axios from "axios"
import ProfileComponentList from "@/components/ProfileComponentList.vue"

const API_URL = "http://127.0.0.1:8000"

export default {
  name: "ProfileSelectView",
  components: { ProfileComponentList },
  data() {
    return {
      profiles: [],
    }
  },
  methods: {
    getProfiles() {

      axios({
        method: "get",
        url: `${API_URL}/movies/profiles/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          // console.log(res.data)
          this.profiles = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    newProfile() {
      this.$router.push({ name: 'newprofile' })
    },
    profileMangeMode() {
      const title_big = document.querySelectorAll('.title_big')
      title_big.forEach(element => {
        element.classList.toggle('nosee')
      });

      const delete_btn = document.querySelectorAll('.delete_profile_btn')
      delete_btn.forEach(element => {
        element.classList.toggle('nosee')
      });
    }
  },
  created() {
    this.getProfiles()
  },
}
</script>

<style>
.cover_container {
  position: fixed;
  top: 0px;
  left: 0px;
  z-index: 10000;
  text-align: center;
  width: 100%;
  height: 100%;
  background-color: #1A1D29;

}

.cover_navbar {
  position: fixed;
  z-index: 10010;
  width: 100%;
  height: 80px;
  background-color: #1A1D29 !important;
}


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

.navbar-brand {
  color: #de2a60 !important;
  font-size: 30px !important;
  font-family: SB;
}

.title_big {
  margin-top: 240px;
  font-weight: 600;
}

.cover_mid_box {
  height: 600px;
  width: 560px;
  margin: 140px auto;
  border-radius: 14px;
  background-color: #1A1D29;
  z-index: 10090;
}

.profile_component_box {
  width: 80%;
  margin: 80px auto;
  display: flex;
  text-align: center;
  justify-content: center;
}

.add_profile_img {
  width: 140px;
  height: 140px;
}

.add_profile_text {
  margin-top: 10px;
}

.add_profile_box {
  margin-left: 10px;
  width: 170px;
  height: 180px;
}

.add_profile_box:hover {
  cursor: pointer;
}

.profile_img2:hover {
  outline: 4px solid white;
  width: 160px;
  height: 160px;
  border-radius: 100%;
}

.add_profile_box:hover img {
  width: 160px;
  height: 160px;
  border-radius: 100%;
  outline: 4px solid white;
}
</style>