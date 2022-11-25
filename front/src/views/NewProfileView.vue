<template>
  <div>
    <div class="cover_container">
      <nav class="navbar navbar-dark bg-dark fixed-top" id="my_navbar">
        <div class="container-fluid">
          <div class="navbar-brand">
            <img src="../assets\topten_logo.png" alt="logo" width="36" height="30" margin-top="5px" />
            <a class="navbar-brand">&nbsp;&nbsp;TOPTEN+</a>
          </div>
          <button @click="cancleProfile" class="login_btn">취소</button>
        </div>
      </nav>


      <div class="cover_big_box">

        <h1 class="title_big">프로필 생성</h1>
        <div class="profile_component_box lay2">
          <div class="boxes left_box lay3">
            <div class="input_box">
              <input class="input_text" type="text" id="nick" v-model="nick" placeholder="프로필 이름">
            </div>


            <div class="left_down_box">
              <h6 class="sub_text">성별</h6>
              <div class="gender_box">
                <label class="" for="genderMale">
                  <div @click="btn_selected1" class="check_box_btn btn_selected male_btn">
                    <div class="gender_text_box">
                      <h5 class="font_mid">남성</h5>
                      <p class="font_small">Male</p>
                    </div>
                    <input class="radio_btn" type="radio" value="1" checked name="gender" id="genderMale"
                      v-model="gender">
                  </div>
                </label>

                <label class="" for="genderFemale">
                  <div @click="btn_selected2" class="check_box_btn female_btn">
                    <div class="gender_text_box">
                      <h5 class="font_mid">여성</h5>
                      <p class="font_small">Female</p>
                    </div>
                    <input class="radio_btn" type="radio" value="2" name="gender" id="genderFemale" v-model="gender">
                  </div>
                </label>
              </div>

              <div class="tmp_box">
                <h6 class="sub_text">성인컨텐츠 제한 해제</h6>
                <div class="switch_box form-check form-switch">
                  <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckChecked" checked />
                  <label class="form-check-label" for="flexSwitchCheckChecked"></label>
                </div>
              </div>

              <p class="font_small">19+콘텐츠까지 시청하실 수 있습니다.</p>
              <input @click="newProfile" class="submit_btn" type="submit" value="생성하기">
            </div>
          </div>

          <div class="boxes right_box lay3">
            <div @click="selectImgSee" class="change_img_box lay2">
              <img class="profile_img_default" :src="require(`../assets/profile${img}.png`)" alt="#" />
              <img class="modify_img" src="../assets\modify.png" alt="#" width="46" height="46" />
            </div>
          </div>
        </div>



        <div class="select_img_box nosee">

          <div @click="selectedImg" class="form-check">
            <input class="nosee" v-model="img" value="1" type="radio" name="img" id="img1" checked="checked">
            <label class="form-check-label" for="img1">
              <img @click="selectedImg" class="profile_img" src="../assets\profile1.png" alt="#" width="46"
                height="46" />
            </label>
          </div>
          <div class="form-check">
            <input class="nosee" v-model="img" value="2" type="radio" name="img" id="img2">
            <label class="" for="img2">
              <img @click="selectedImg" class="profile_img" src="../assets\profile2.png" alt="#" width="46"
                height="46" />
            </label>
          </div>
          <div class="form-check">
            <input class="nosee" v-model="img" value="3" type="radio" name="img" id="img3">
            <label class="" for="img3">
              <img @click="selectedImg" class="profile_img" src="../assets\profile3.png" alt="#" width="46"
                height="46" />
            </label>
          </div>
          <div class="form-check">
            <input class="nosee" v-model="img" value="4" type="radio" name="img" id="img4">
            <label class="" for="img4">
              <img @click="selectedImg" class="profile_img" src="../assets\profile4.png" alt="#" width="46"
                height="46" />
            </label>
          </div>
          <div class="form-check">
            <input class="nosee" v-model="img" value="5" type="radio" name="img" id="img5">
            <label class="" for="img5">
              <img @click="selectedImg" class="profile_img" src="../assets\profile5.png" alt="#" width="46"
                height="46" />
            </label>
          </div>
          <div class="form-check">
            <input class="nosee" v-model="img" value="6" type="radio" name="img" id="img6">
            <label class="" for="img6">
              <img @click="selectedImg" class="profile_img" src="../assets\profile6.png" alt="#" width="46"
                height="46" />
            </label>
          </div>
          <div class="form-check">
            <input class="nosee" v-model="img" value="7" type="radio" name="img" id="img7">
            <label class="" for="img7">
              <img @click="selectedImg" class="profile_img" src="../assets\profile7.png" alt="#" width="46"
                height="46" />
            </label>
          </div>
          <div class="form-check">
            <input class="nosee" v-model="img" value="8" type="radio" name="img" id="img8">
            <label class="" for="img8">
              <img @click="selectedImg" class="profile_img" src="../assets\profile8.png" alt="#" width="46"
                height="46" />
            </label>
          </div>
          <div class="form-check">
            <input class="nosee" v-model="img" value="9" type="radio" name="img" id="img9">
            <label class="" for="img9">
              <img @click="selectedImg" class="profile_img" src="../assets\profile9.png" alt="#" width="46"
                height="46" />
            </label>
          </div>

        </div>
      </div>
    </div>





  </div>
</template>

<script>
import axios from "axios"

const API_URL = "http://127.0.0.1:8000"

export default {
  name: "NewProfileView",
  data() {
    return {
      nick: null,
      gender: 1,
      img: 1,
      // srcUrl: require("../assets\\profile" + this.img + ".png"),
    }
  },
  methods: {
    cancleProfile() {
      this.$router.push({ name: 'profiles' })
    },
    selectedImg() {
      document.querySelector('.select_img_box').classList.toggle('nosee')
    },
    selectImgSee() {
      document.querySelector('.select_img_box').classList.toggle('nosee')
    },
    newProfile() {
      axios({
        method: "post",
        url: `${API_URL}/movies/profiles/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
        data: {
          name: this.nick,
          gender: this.gender,
          img: this.img,
        },
      })
        .then((res) => {
          console.log(res.data)
        })
        .then(() => {
          this.$router.push({ name: 'profiles' })
        })
        .catch((err) => {
          console.log(err)
        })
    },
    btn_selected1() {
      console.log(document.querySelector(".female_btn"))
      document.querySelector(".female_btn").classList.remove("btn_selected")
      document.querySelector(".male_btn").classList.add("btn_selected")
    },
    btn_selected2() {
      console.log(document.querySelector(".male_btn"))
      document.querySelector(".female_btn").classList.add("btn_selected")
      document.querySelector(".male_btn").classList.remove("btn_selected")
    }
  },
}
</script>

<style>
.profile_submit_box {
  display: flex;
}

.boxes {
  width: 300px;
  height: 260px;
}

.input_box {
  width: 380px;
  height: 56px;
  outline: 2px solid #6D7582;
  background-color: #30333E;
  border: none;
}

.input_box:hover {
  outline: 2px solid #d8d8d8;
}

.profile_component_box {
  margin: 40px auto;
}

input:-webkit-autofill {
  -webkit-box-shadow: 0 0 0 1000px #30333E inset;
  box-shadow: 0 0 0 1000px #30333E inset;
}

.left_box {
  width: 440px;
}

.right_box {
  width: 300px;
}

.left_down_box {
  text-align: left;
}

.check_box_btn {
  background-color: #30333E;
  width: 178px;
  height: 70px;
  border-radius: 6px;
  display: flex;
  margin-top: 4px;
  margin-right: 20px;
}

.check_box_btn:hover {
  cursor: pointer;
  outline: 2px solid #d8d8d8;
}

.gender_box {
  display: flex;
}

.gender_text_box {
  margin: 2px auto;
}

.sub_text {
  margin-top: 20px;
  width: 240px;
}

.radio_btn {
  margin-right: 20px;
}

.font_mid {
  font-size: 20px;
  margin-top: 12px;
  margin-bottom: 0px;
  font-weight: 500;
}

.font_small {
  font-size: 14px;
  color: #6D7582;
}

.btn_selected {
  outline: 2px solid #0E4B84;
  background-color: #153151;
}

.tmp_box {
  margin-top: 20px;
  display: flex;
}

.switch_box {
  margin-left: 160px;
  margin-top: 8px;
}

.profile_img_default {
  width: 200px;
  height: 200px;
}

.change_img_box {
  height: 200px;
  width: 200px;
}

.change_img_box:hover {
  cursor: pointer;
}

.modify_img {
  position: relative;
  bottom: 48px;
  left: 68px;
}

.select_img_box {
  display: flex;
  width: 80%;
  margin: 100px auto;
  justify-content: center;

}

.profile_img {
  width: 120px;
  height: 120px;
}

.profile_img:hover {
  outline: 4px solid white;
  width: 130px;
  height: 130px;
  border-radius: 100%;
}

.submit_btn {
  width: 380px;
  height: 50px;
  border-radius: 6px;
  background-color: #FF0066;
  color: white;
  border: none;
}

.nosee {
  display: none;
}

.form-check {
  width: 140px;
}
</style>