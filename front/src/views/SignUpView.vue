<template>
  <div class="cover_container">
    <nav class="navbar navbar-dark bg-dark fixed-top" id="my_navbar">
      <div class="container-fluid">
        <!-- <div class="navbar-brand" @click="toHome"> -->
        <div class="navbar-brand">
          <img src="../assets\topten_logo.png" alt="logo" width="36" height="30" margin-top="5px" />
          <a class="navbar-brand">&nbsp;&nbsp;TOPTEN+</a>
        </div>
        <button class="login_btn" @click="goLogin">로그인</button>

      </div>
    </nav>
    <div class="cover_big_box">

      <div class="cover_mid_box">
        <div class="cover_samll_box lay id_box">
          <p>1/3단계</p>
          <h1 class="title_text">이메일을 입력하세요.</h1>
          <div class="form_box lay2">
            <div>
              <p class="sub_text">이 이메일과 비밀번호로 탑텐+ 계정에 로그인하여 서비스를 이용할 수 있습니다.</p>
              <label for="username"></label>
              <div class="input_box">
                <input class="input_text" type="text" id="username" v-model="username" placeholder="이메일을 입력하세요.">
              </div>
              <!-- 약관 박스 -->
              <div class="agree_box lay3">
                <div class="check_box_unit">
                  <input class="my_checkbox" id="flexCheckDefault" type="checkbox" value="1" style="zoom:1.5">
                  <label for="flexCheckDefault">
                    <span class="check_box">(필수) 본인은 만 19세 이상이며 </span><span class="underline_text">탑탠+
                      이용약관</span><span>에 동의합니다.</span>
                  </label>
                </div>
                <div class="check_box_unit">
                  <input class="my_checkbox" id="flexCheckDefault2" type="checkbox" value="2" style="zoom:1.5">
                  <label for="flexCheckDefault2">
                    <span class="check_box">(필수) 탑탠+의 </span><span class="underline_text">개인정보 수집 및 이용</span><span>에
                      동의합니다.</span>
                  </label>
                </div>
                <div class="check_box_unit">
                  <input class="my_checkbox" id="flexCheckDefault3" type="checkbox" value="3" style="zoom:1.5">
                  <label for="flexCheckDefault3">
                    <span class="check_box">(선택) 탑탠+에 관한 최신 소식, 특별 혜택 및 기타 정보를 받아보겠습니다.</span>
                  </label>
                </div>

              </div>

            </div>
            <br>
            <button @click="nextClicked" class="next_btn">다음으로</button>
          </div>
        </div>
        <div class="cover_samll_box lay pw_box nosee">
          <p>2/3단계</p>
          <h1 class="title_text">비밀번호를 생성하세요</h1>
          <div class="form_box lay2">
            <div>
              <p class="sub_text">이 이메일과 비밀번호로 TOP 10+ 계정에 로그인하여 서비스를 이용할 수 있습니다.</p>
              <div class="input_box pw_box2">
                <input class="input_text" type="password" id="password1" v-model="password1" placeholder="비밀번호를 입력하세요.">
              </div><br>
              <div class="input_box pw_box2">
                <input class="input_text" type="password" id="password2" v-model="password2" placeholder="비밀번호 확인">
              </div>
            </div>
            <br>
            <input @click="signUp" class="next_btn" type="submit" value="시작하기">
          </div>
        </div>
      </div>





      <img class="backdrop_img2" src="../assets\wallpaper.png" alt="배경" />
    </div>

  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username: username,
        password1: password1,
        password2: password2,
      }
      this.$store.dispatch('signUp', payload)
      console.log(this.$store.state.token)
      if (this.$store.state.token) {
        document.querySelector('.cover_container').classList.toggle('nosee')
      }

    },
    nextClicked() {
      document.querySelector('.id_box').classList.add('nosee');
      document.querySelector('.pw_box').classList.toggle('nosee');
    },
    goLogin() {
      this.$router.push({ name: 'login' })
    }

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

.agree_box {
  height: 140px;
  margin-top: 20px;
}

.check_box {
  margin-left: 10px;
}


input[type="checkbox"] {
  -webkit-appearance: none;
  position: relative;
  width: 12px;
  height: 12px;
  cursor: pointer;
  outline: none !important;
  border: 1px solid #60626B;
  border-radius: 2px;
  background: #30333E;
}

input[type="checkbox"]::before {
  content: "\2713";
  position: absolute;
  top: 50%;
  left: 50%;
  overflow: hidden;
  transform: scale(0.2) translate(-50%, -50%);
  line-height: 1;
}

input[type="checkbox"]:hover {
  border-color: white;
}

input[type="checkbox"]:checked {
  background-color: #de2a60;
  border-color: #de2a60;
  color: white;
}

input[type="checkbox"]:checked::before {
  border-radius: 2px;
  transform: scale(0.6) translate(-80%, -80%)
}

.check_box_unit {
  display: flex;
  font-size: 14px;
  color: #848588;
  margin-top: 14px;
}

.underline_text {
  text-decoration: underline;
  color: #61AEEC;
}

.pw_box2 {
  margin-top: 20px;
}

input:-webkit-autofill {
  -webkit-box-shadow: 0 0 0 1000px #30333E inset;
  box-shadow: 0 0 0 1000px #30333E inset;
}
</style>