import Vue from "vue"
import VueRouter from "vue-router"
import store from "@/store/index"

Vue.use(VueRouter)

const routes = [
  {
    path: "/",
    name: "home",
    component: () => import("../views/HomeView.vue"),
    // beforeEnter(to, from, next) {
    //   if (store.state.token === null) {
    //     alert("로그인을 하셔야 합니다.")
    //     next({ name: "login" })
    //   } else {
    //     next()
    //   }
    // },
  },
  {
    path: "/search",
    name: "search",
    component: () => import("../views/SearchView.vue"),
    // beforeEnter(to, from, next) {
    //   if (store.state.token === null) {
    //     alert("로그인을 하셔야 합니다.")
    //     next({ name: "login" })
    //   } else {
    //     next()
    //   }
    // },
  },
  {
    path: "/topten",
    name: "topten",
    component: () => import("../views/ToptenView.vue"),
    // beforeEnter(to, from, next) {
    //   if (store.state.token === null) {
    //     alert("로그인을 하셔야 합니다.")
    //     next({ name: "login" })
    //   } else {
    //     next()
    //   }
    // },
  },
  {
    path: "/category",
    name: "category",
    component: () => import("../views/CategoryView.vue"),
  },
  {
    path: "/liked",
    name: "liked",
    component: () => import("../views/LikedView.vue"),
  },
  {
    path: "/matching",
    name: "matching",
    component: () => import("../views/MatchingView.vue"),
  },
  {
    path: "/profile/:profileId",
    name: "profile",
    component: () => import("../views/ProfileView.vue"),
    beforeEnter(to, from, next) {
      if (store.state.token === null) {
        alert("로그인을 하셔야 합니다.")
        next({ name: "login" })
      } else if (store.state.profile_id === null) {
        alert("프로필을 선택하셔야 합니다.")
        next({ name: "profiles" })
      } else {
        next()
      }
    },
  },
  {
    mode: "history",
    path: "/detail/:movieId",
    name: "detail",
    component: () => import("../views/DetailView.vue"),
    beforeEnter(to, from, next) {
      if (store.state.token === null) {
        alert("로그인을 하셔야 합니다.")
        next({ name: "login" })
      } else if (store.state.profile_id === null) {
        alert("프로필을 선택하셔야 합니다.")
        next({ name: "profiles" })
      } else {
        next()
      }
    },
  },
  {
    path: "/signup",
    name: "signup",
    component: () => import("../views/SignUpView.vue"),
  },
  {
    path: "/login",
    name: "login",
    component: () => import("../views/LoginView.vue"),
  },
  {
    path: "/profiles",
    name: "profiles",
    component: () => import("../views/ProfileSelectView.vue"),
    beforeEnter(to, from, next) {
      if (store.state.token === null) {
        alert("로그인을 하셔야 합니다.")
        next({ name: "login" })
      } else {
        next()
      }
    },
  },
  {
    path: "/newprofile",
    name: "newprofile",
    component: () => import("../views/NewProfileView.vue"),
    beforeEnter(to, from, next) {
      if (store.state.token === null) {
        alert("로그인을 하셔야 합니다.")
        next({ name: "login" })
      } else {
        next()
      }
    },
  },
  // {
  //   path: "/",
  //   name: "home",
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () =>
  //     import(/* webpackChunkName: "about" */ "../views/HomeView.vue"),
  // },
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
})

export default router
