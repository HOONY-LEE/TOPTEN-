<template>
  <div class="sidebar_box fixed-top">
    <ul class="list_box">
      <router-link class="router_link" to="/">
        <div @click="btnClicked" class="list_btn_box btn_clicked">
          <img class="icons" src="../assets\topten_logo.png" alt="" />
          <li>TOPTEN</li>
        </div>
      </router-link>
      <router-link class="router_link" to="/search">
        <div @click="btnClicked" class="list_btn_box">
          <img class="icons" src="../assets\search_icon.png" alt="" />
          <li>검색</li>
        </div>
      </router-link>
      <!-- <router-link class="router_link" to="/topten">
        <div @click="btnClicked" class="list_btn_box">
          <img class="icons" src="../assets\topten_logo.png" alt="" />
          <li>TOP10</li>
        </div>
      </router-link> -->
      <router-link class="router_link" to="/category">
        <div @click="btnClicked" class="list_btn_box">
          <img class="icons" src="../assets\category_icon.png" alt="" />
          <li>카테고리</li>
        </div>
      </router-link>
      <!-- <router-link class="router_link" to="/liked">
        <div @click="btnClicked" class="list_btn_box">
          <img class="icons" src="../assets\stack_icon.png" alt="" />
          <li>관심목록</li>
        </div>
      </router-link> -->
      <router-link class="router_link" to="/matching">
        <div @click="btnClicked" class="list_btn_box">
          <img class="icons" src="../assets\matching_icon.png" alt="" />
          <li>매칭서비스</li>
        </div>
      </router-link>
      <div class="router_link" @click="goProfile">
        <div @click="btnClicked" class="list_btn_box">
          <img class="icons" src="../assets\liked_icon.png" alt="" />
          <li>프로필</li>
        </div>
      </div>
    </ul>
    <ul class="list_box2">
      <div class="list_btn_box2 lay">
        <img class="icons" src="../assets\matching_icon.png" alt="" />
        <li>설정</li>
      </div>
      <div class="list_btn_box2 lay">
        <img class="icons" src="../assets\matching_icon.png" alt="" />
        <li>다크테마</li>
        <div class="form-check form-switch">
          <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckChecked" checked />
          <label class="form-check-label" for="flexSwitchCheckChecked"></label>
        </div>
      </div>
    </ul>
  </div>
</template>

<script>
export default {
  name: "SideBar",
  methods: {
    btnClicked() {
      const cList = document.querySelectorAll(".list_btn_box")
      // console.log(cList)
      cList.forEach((element) => {
        element.classList.remove("btn_clicked")
      })
      event.target.parentElement.classList.toggle("btn_clicked")
    },
    closeMovie() {
      document.querySelector('.video_box').classList.add("nosee")
    },
    goProfile() {
      this.$router.push({ name: 'profile', params: { profileId: this.$store.state.profile_id } })
    }
  },
}
</script>

<style>
.sidebar_box {
  width: 250px;
  height: 100%;
  margin-top: 80px;
  margin-bottom: 0px;
  background-color: #141517;
  /* border-right: 1px solid #4E4E4E; */
}

li {
  font-family: AppleSDUL;
  list-style: none;
  font-size: 20px;
  padding-left: 20px;
  color: #ced2d8;
  width: 200px;
}

.list_box {
  margin-top: 30px;
  /* border: 1px solid white; */
  padding-left: 20px;
  padding-right: 20px;
}

.list_box2 {
  margin-top: 400px;
  padding-left: 20px;
  padding-right: 20px;
  /* border: 1px solid white; */
}

.list_btn_box {
  border-radius: 6px;
  margin: 6px;
  height: 44px;

  display: flex;
  line-height: 44px;
}

.icons {
  width: 20px;
  height: 20px;
  margin-top: 12px;
  margin-left: 10px;
}

.list_btn_box2 {
  margin: 6px;
  height: 44px;
  display: flex;
  line-height: 44px;
}

.list_btn_box:hover {
  background-color: #303133;
}

.list_btn_box:hover>li {
  color: white;
}

.btn_clicked {
  background-color: #303133;
}

.router_link {
  text-decoration: none;
  color: white;
}

.form-check-input {
  margin-top: 12px !important;
}
</style>
