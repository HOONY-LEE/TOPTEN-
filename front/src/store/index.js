import Vue from "vue"
import Vuex from "vuex"
import axios from "axios"
import router from "@/router"

Vue.use(Vuex)

const API_URL = "http://127.0.0.1:8000"

export default new Vuex.Store({
  state: {
    popularity: [],
    vote: [],
    recent: [],
    soon: [],
    hip: [],
    trash: [],
    action: [],
    adventure: [],
    animation: [],
    comedy: [],
    crime: [],
    documentary: [],
    drama: [],
    family: [],
    fantasy: [],
    history: [],
    horror: [],
    music: [],
    mystery: [],
    romance: [],
    sf: [],
    tv: [],
    thriller: [],
    war: [],
    western: [],
    token: null,
    profile_id: null,
    keyword: null,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    },
    isProfile(state) {
      return state.profile_id ? true : false
    },
  },
  mutations: {
    GET_POPULARITY(state, popularity) {
      state.popularity = popularity
    },
    GET_VOTE(state, vote) {
      state.vote = vote
    },
    GET_RECENT(state, recent) {
      state.recent = recent
    },
    GET_SOON(state, soon) {
      state.soon = soon
    },
    GET_HIP(state, hip) {
      state.hip = hip
    },
    GET_TRASH(state, trash) {
      state.trash = trash
    },
    GET_ACTION(state, action) {
      state.action = action
    },
    GET_ADVENTURE(state, adventure) {
      state.adventure = adventure
    },
    GET_ANIMATION(state, animation) {
      state.animation = animation
    },
    GET_COMEDY(state, comedy) {
      state.comedy = comedy
    },
    GET_CRIME(state, crime) {
      state.crime = crime
    },
    GET_DRAMA(state, drama) {
      state.drama = drama
    },
    GET_FAMILY(state, family) {
      state.family = family
    },
    GET_FANTASY(state, fantasy) {
      state.fantasy = fantasy
    },
    GET_HISTORY(state, history) {
      state.history = history
    },
    GET_HORROR(state, horror) {
      state.horror = horror
    },
    GET_MUSIC(state, music) {
      state.music = music
    },
    GET_MYSTERY(state, mystery) {
      state.mystery = mystery
    },
    GET_ROMANCE(state, romance) {
      state.romance = romance
    },
    GET_SF(state, sf) {
      state.sf = sf
    },
    GET_THRILLER(state, thriller) {
      state.thriller = thriller
    },
    GET_WAR(state, war) {
      state.war = war
    },
    SAVE_TOKEN(state, token) {
      state.token = token
    },
    SEARCH_KEYWORD(state, payload) {
      console.log(payload)
      state.keyword = payload
    },
    LOG_OUT(state, payload) {
      console.log(payload)
      state.token = payload
      state.profile_id = payload
    },
    CHANGE_PROFILE(state, payload) {
      console.log(payload)
      state.profile_id = payload
    },
  },
  actions: {
    getMovies(context) {
      axios({
        method: "get",
        url: `${API_URL}/movies/home/-popularity`,
        params: {
          page: 1,
        },
      })
        .then((res) => {
          context.commit("GET_POPULARITY", res.data)
        })
        .catch((err) => {
          console.log(err)
        })
      axios({
        method: "get",
        url: `${API_URL}/movies/home/-vote_avg`,
        params: {
          page: 1,
        },
      })
        .then((res) => {
          context.commit("GET_VOTE", res.data)
        })
        .catch((err) => {
          console.log(err)
        })
      axios({
        method: "get",
        url: `${API_URL}/movies/recent/`,
        params: {
          page: 1,
        },
      })
        .then((res) => {
          context.commit("GET_RECENT", res.data)
        })
        .catch((err) => {
          console.log(err)
        })
      axios({
        method: "get",
        url: `${API_URL}/movies/soon/`,
        params: {
          page: 1,
        },
      })
        .then((res) => {
          context.commit("GET_SOON", res.data)
        })
        .catch((err) => {
          console.log(err)
        })
      axios({
        method: "get",
        url: `${API_URL}/movies/home/popularity`,
        params: {
          page: 1,
        },
      })
        .then((res) => {
          context.commit("GET_HIP", res.data)
        })
        .catch((err) => {
          console.log(err)
        })
      axios({
        method: "get",
        url: `${API_URL}/movies/home/vote_avg`,
        params: {
          page: 1,
        },
      })
        .then((res) => {
          context.commit("GET_TRASH", res.data)
        })
        .catch((err) => {
          console.log(err)
        })
      axios({
        method: "get",
        url: `${API_URL}/movies/genre/28`,
        params: {
          page: 1,
        },
      })
        .then((res) => {
          context.commit("GET_ACTION", res.data)
        })
        .catch((err) => {
          console.log(err)
        })
      axios({
        method: "get",
        url: `${API_URL}/movies/genre/12`,
        params: {
          page: 1,
        },
      })
        .then((res) => {
          context.commit("GET_ADVENTURE", res.data)
        })
        .catch((err) => {
          console.log(err)
        })
      axios({
        method: "get",
        url: `${API_URL}/movies/genre/16`,
        params: {
          page: 1,
        },
      })
        .then((res) => {
          context.commit("GET_ANIMATION", res.data)
        })
        .catch((err) => {
          console.log(err)
        })
      axios({
        method: "get",
        url: `${API_URL}/movies/genre/35`,
        params: {
          page: 1,
        },
      })
        .then((res) => {
          context.commit("GET_COMEDY", res.data)
        })
        .catch((err) => {
          console.log(err)
        })
      axios({
        method: "get",
        url: `${API_URL}/movies/genre/80`,
        params: {
          page: 1,
        },
      })
        .then((res) => {
          context.commit("GET_CRIME", res.data)
        })
        .catch((err) => {
          console.log(err)
        })
      axios({
        method: "get",
        url: `${API_URL}/movies/genre/18`,
        params: {
          page: 1,
        },
      })
        .then((res) => {
          context.commit("GET_DRAMA", res.data)
        })
        .catch((err) => {
          console.log(err)
        })
      axios({
        method: "get",
        url: `${API_URL}/movies/genre/10751`,
        params: {
          page: 1,
        },
      })
        .then((res) => {
          context.commit("GET_FAMILY", res.data)
        })
        .catch((err) => {
          console.log(err)
        })
      axios({
        method: "get",
        url: `${API_URL}/movies/genre/14`,
        params: {
          page: 1,
        },
      })
        .then((res) => {
          context.commit("GET_FANTASY", res.data)
        })
        .catch((err) => {
          console.log(err)
        })
      axios({
        method: "get",
        url: `${API_URL}/movies/genre/36`,
        params: {
          page: 1,
        },
      })
        .then((res) => {
          context.commit("GET_HISTORY", res.data)
        })
        .catch((err) => {
          console.log(err)
        })
      axios({
        method: "get",
        url: `${API_URL}/movies/genre/27`,
        params: {
          page: 1,
        },
      })
        .then((res) => {
          context.commit("GET_HORROR", res.data)
        })
        .catch((err) => {
          console.log(err)
        })
      axios({
        method: "get",
        url: `${API_URL}/movies/genre/10402`,
        params: {
          page: 1,
        },
      })
        .then((res) => {
          context.commit("GET_MUSIC", res.data)
        })
        .catch((err) => {
          console.log(err)
        })
      axios({
        method: "get",
        url: `${API_URL}/movies/genre/9648`,
        params: {
          page: 1,
        },
      })
        .then((res) => {
          context.commit("GET_MYSTERY", res.data)
        })
        .catch((err) => {
          console.log(err)
        })
      axios({
        method: "get",
        url: `${API_URL}/movies/genre/10749`,
        params: {
          page: 1,
        },
      })
        .then((res) => {
          context.commit("GET_ROMANCE", res.data)
        })
        .catch((err) => {
          console.log(err)
        })
      axios({
        method: "get",
        url: `${API_URL}/movies/genre/878`,
        params: {
          page: 1,
        },
      })
        .then((res) => {
          context.commit("GET_SF", res.data)
        })
        .catch((err) => {
          console.log(err)
        })
      axios({
        method: "get",
        url: `${API_URL}/movies/genre/53`,
        params: {
          page: 1,
        },
      })
        .then((res) => {
          context.commit("GET_THRILLER", res.data)
        })
        .catch((err) => {
          console.log(err)
        })
      axios({
        method: "get",
        url: `${API_URL}/movies/genre/10752`,
        params: {
          page: 1,
        },
      })
        .then((res) => {
          context.commit("GET_WAR", res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    signUp(context, payload) {
      // console.log(payload)
      axios({
        method: "post",
        url: `${API_URL}/accounts/signup/`,
        data: {
          username: payload.username,
          password1: payload.password1,
          password2: payload.password2,
        },
      })
        .then((res) => {
          // console.log(res)
          context.commit("SAVE_TOKEN", res.data.key)
        })
        .then(() => {
          router.push({ name: "profiles" })
        })
        .catch((err) => {
          console.log(err.response.data)
          alert("회원가입 실패")
          router.go({ name: "signup" })
        })
    },
    logIn(context, payload) {
      axios({
        method: "post",
        url: `${API_URL}/accounts/login/`,
        data: {
          username: payload.username,
          password: payload.password,
        },
      })
        .then((res) => {
          // console.log(res)
          context.commit("SAVE_TOKEN", res.data.key)
        })
        .then(() => {
          router.push({ name: "profiles" })
        })
        .catch((err) => {
          console.log(err.response.data)
          alert("로그인 실패")
        })
    },
    searchKeyword(context, payload) {
      console.log(payload)
      context.commit("SEARCH_KEYWORD", payload)
    },
    logOut(context, payload) {
      console.log(payload)
      context.commit("LOG_OUT", payload)
    },
    changeProfile(context, payload) {
      console.log(payload)
      context.commit("CHANGE_PROFILE", payload)
    },
  },
  modules: {},
})
