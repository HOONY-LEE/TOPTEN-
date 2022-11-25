<template>
  <div id="app" class="app_background">
    <navbar class="lay"> </navbar>
    <div class="navbar-space lay"></div>
    <sidebar class="lay"> </sidebar>
    <div class="middle_box">
      <div class="content_box_margin">
        <router-view />
      </div>
    </div>
    <footer class="lay2">
      <FooterComponent class="footer_componenet"></FooterComponent>
    </footer>

  </div>
</template>
<script>
import Sidebar from "./components/Sidebar"
import Navbar from "./components/Navbar"
import FooterComponent from "./components/FooterComponent.vue"

export default {
  name: "App",
  components: {
    Navbar,
    Sidebar,
    FooterComponent,
  },
}
</script>

<style>
@font-face {
  font-family: "SB";
  src: url(./fonts/SBagroB.ttf) format("woff");
}

@font-face {
  font-family: "AppleSDL";
  src: url(./fonts/AppleSDGothicNeoL.ttf) format("woff");
}

@font-face {
  font-family: "AppleSDUL";
  src: url(./fonts/AppleSDGothicNeoUL.ttf) format("woff");
}

@font-face {
  font-family: "AppleSDB";
  src: url(./fonts/AppleSDGothicNeoB.ttf) format("woff");
}

@font-face {
  font-family: "AppleSDEB";
  src: url(./fonts/AppleSDGothicNeoEB.ttf) format("woff");
}

#app {
  font-family: AppleSDL, AppleSDUL, AppleSDB, AppleSDEB, SB, sans-serif;
  font-weight: 200;
  color: white;
}


nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: white;
}

.app_background {
  background-color: #1b1c1d;
}

.navbar-space {
  height: 80px;
}

.middle_box {
  display: flex;
  margin-left: 250px;
}

.content_box_margin {
  margin-left: 70px;
  margin-top: 30px;
  width: 100%;
}


.components_box {
  margin-bottom: 50px;
  height: 460px;
}

.profile_box,
.col:hover {
  cursor: pointer;
}

.app_cover {
  position: fixed;
  top: 00px;
  left: 0px;
  z-index: 9998;
  width: 100%;
  height: 100%;
  background-color: #1A1D29;
  display: none;

}

.footer_componenet {
  margin-top: 800px;
}





/* .lay {
  border: 1px solid green;
}

.lay2 {
  border: 1px dashed crimson;
}

.lay3 {
  border: 2px solid burlywood;
} */
</style>
