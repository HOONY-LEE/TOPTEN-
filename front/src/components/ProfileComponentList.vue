<template>
  <div>
    <div class="profile_box_unit lay" @click="changeProfile">
      <!-- <img src="{% static '/media/profile/261143_20210325180240_500_0DlWsW8.jpg' %}" alt="#" /> -->
      <!-- <p v-html="img_tag"></p> -->
      <img class="profile_img2" :src="require(`../assets/profile${profile.img}.png`)" />

      <div class="profile_text_box">
        {{ profile.name }}</div>

    </div>
    <button class="delete_profile_btn nosee" @click="deleteProfile">프로필 삭제</button>
  </div>
</template>

<script>
import axios from "axios"

const API_URL = "http://127.0.0.1:8000"

export default {
  name: "ProfileComponentList",
  props: {
    profile: Object,
  },
  data() {
    return {
      // img_tag: null,
      gender: null,
    }
  },
  methods: {
    changeProfile() {
      this.$store.dispatch("changeProfile", this.profile.id)
      this.$router.push({ name: 'home' })
    },
    deleteProfile() {
      axios({
        method: "delete",
        url: `${API_URL}/movies/profiles/${this.profile.id}`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then(() => {
          this.$emit("refresh")
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
    // const profile_img_list = document.querySelectorAll('.profile_img2')
    // profile_img_list.forEach(element => {
    //   console.log(this.profile.name)
    //   console.log(this.gender)
    //   if (this.profile.gender === 1) {
    //     element.classList.add('blue_round')
    //   } else if (this.profile.gender === 2) {
    //     element.classList.add('pink_round')
    //   }
    // });
    this.makeProfile()




  },
}
</script>

<style>
.profile_box_unit {
  width: 150px;
  height: 180px;
  margin: 0px 20px;
  justify-content: center;
  margin-bottom: 20px;
}

.profile_box_unit:hover {
  cursor: pointer;
}

.profile_box_unit:hover .profile_text_box {
  color: white;
}

.profile_box_unit>img {
  width: 140px;
  height: 140px;
}

.profile_text_box {
  margin-top: 20px;
  font-size: 22px;
  color: rgb(203, 203, 203);
}


.delete_profile_btn {
  width: 140px;
  height: 36px;
  border-radius: 6px;
  background-color: #FF0066;
  border: none;
  color: white;
  padding-top: 4px;
}

.profile_img2 {
  width: 140px;
  height: 140px;
}

.pink_round {
  border-radius: 100%;
  outline: 4px solid #F40061;
}

.blue_round {
  border-radius: 100%;
  outline: 4px solid #0072D2;
}
</style>