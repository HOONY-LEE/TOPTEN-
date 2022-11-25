<template>
  <div>
    <div class="cover_container">
      <nav class="navbar navbar-dark bg-dark fixed-top" id="my_navbar">
        <div class="container-fluid">
          <div class="navbar-brand">
            <img src="../assets\topten_logo.png" alt="logo" width="36" height="30" margin-top="5px" />
            <a class="navbar-brand">&nbsp;&nbsp;TOPTEN+</a>
          </div>
          <button class="login_btn" @click.prevent="goSignUp">회원가입</button>
        </div>
      </nav>


      <div class="cover_big_box">

        <div class="cover_mid_box">
          <div class="cover_samll_box lay id_box">
            <p>TOPTEN+에 오신걸 환영합니다.</p>
            <h1 class="title_text">로그인</h1>
            <div class="form_box lay2">
              <div>
                <p class="sub_text">이 이메일과 비밀번호로 TOP 10+ 계정에 로그인하여 서비스를 이용할 수 있습니다.</p>
                <label for="username"></label>
                <div class="input_box">
                  <input class="input_text" type="text" id="username" v-model="username" placeholder="아이디를 입력하세요.">
                </div>
                <div class="input_box pw_box">
                  <input class="input_text" type="password" id="password" v-model="password" placeholder="비밀번호를 입력하세요.">
                </div>


              </div>
              <br><br>
              <button class="next_btn" @click.prevent="logIn">로그인</button>
              <div class="login_text_box" @click.prevent="goSignUp">
                <span>아직 TOP10+ 회원이 아니신가요? </span>
                <span class="underline_text">간편회원가입</span>
              </div>
            </div>
          </div>


        </div>





        <img class="backdrop_img2" src="../assets\wallpaper2.png" alt="배경" />

      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    logIn() {
      const username = this.username
      const password = this.password

      const payload = {
        username: username,
        password: password,
      }

      this.$store.dispatch('logIn', payload)
    },
    goSignUp() {
      this.$router.push({ name: 'signup' })
    }
  }
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
  background-color: #141517;
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

.cover_mid_box {
  height: 600px;
  width: 560px;
  margin: 140px auto;
  border-radius: 14px;
  background-color: #1A1D29;
  z-index: 10090;
}

.login_btn {
  margin-right: 20px;
  width: 120px;
  height: 34px;
  border-radius: 6px;
  border: none;
  background-color: #60626B;
  color: white;
  font-weight: 500;
  padding-top: 4px;
}

.title_text {
  font-weight: 600;
  font-size: xx-large;
}

.cover_samll_box {
  margin: 20px auto;
  padding-top: 40px;
  width: 450px;
  height: 600px;
  text-align: left;
}

.backdrop_img2 {
  position: absolute;
  z-index: -1000;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  filter: brightness(50%);
  opacity: 0.9;
}

.form_box {
  margin-top: 10px;
}

.input_box {
  width: 446px;
  height: 54px;
  background-color: #30333E;
  border-radius: 6px;
  display: flex;
  margin-top: 0px;
  border: 2px solid #60626B;
}

.input_text {
  width: 380px;
  height: 30px;
  background-color: #30333E;
  border: none;
  margin: 4px;
  color: white;
  margin-left: 16px;
  margin-top: 10px;
}

.input_text:focus {
  outline: none;
}

.sub_text {
  margin-bottom: 2px;
}

.next_btn {
  width: 100%;
  height: 50px;
  background-color: #de2a60;
  border: none;
  border-radius: 6px;
  color: white;
}

.login_text_box {
  margin: 20px auto;
  text-align: center;
  width: 340px;
  color: #B0B0B2;
}

.underline_text {
  text-decoration: underline;
  color: #3c78a8dc;
}

.login_text_box:hover {
  cursor: pointer;
  color: white;
}

.login_text_box:hover .underline_text {
  text-decoration: underline;
  color: #61AEEC;
}

.pw_box {
  margin-top: 40px;
}

input:-webkit-autofill {
  -webkit-box-shadow: 0 0 0 1000px #30333E inset;
  box-shadow: 0 0 0 1000px #30333E inset;
}
</style>
