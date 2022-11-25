<template>
  <div class="search lay">
    <h1>검색</h1>

    <div class="search_big_box">
      <div class="search_middle_box">
        <img class="icons" src="../assets\search_icon_gray.png" alt="" />
        <input @focus="focusinEvent" :value="keyword" @input="changeKeyword" class="search_small_box" type="text"
          placeholder="검색어를 입력하세요" @keyup="searchBaro" />
      </div>
    </div>
    <div class="search_result_box">
      <div class="components_box lay2">
        <ToptenComponentList :movie="movie" v-for="(movie, index) in searched_movies" :key="index" :index="index"
          class="toptenComponentList_box row row-cols-12 row-cols-md-12 g-2 lay2"></ToptenComponentList>
      </div>
    </div>

  </div>
</template>

<script>
import axios from "axios"
import ToptenComponentList from "@/components/ToptenComponentList.vue"

const API_URL = "http://127.0.0.1:8000"

export default {
  name: "SearchView",
  components: { ToptenComponentList },
  data() {
    return {
      keyword: null,
      searched_movies: [],
    }
  },
  methods: {
    focusinEvent() {
      const newSrc =
        "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACIAAAAiCAYAAAA6RwvCAAAABHNCSVQICAgIfAhkiAAAAhNJREFUWEftl4FNw0AMRZsJYAPKBMAEhAmACYAJKBMQJgAmICPABLQTwAakEwAThP8ln+Q6l8RXSCgSliySxue82D77yCYbItmGcEz+Fkhd1/uI3BmUf6nb0A/oK/QR+pRlWfWd6HZGRABu8YLc8ZISNlcAImCytIIA4hzeCMGv9wohjgDDSCVJFEQgHoynJe7vJB3h0QkuqDvKdi2YBoik41lF4hPXBb6SEA2BPSM2g16rhxWuD1LSFAOZw8mhOCVE7gl1JIo3WFd487MCItF4UYtZfNFItESHtpfyjCna9UbFgmhHSziZer+IdpKmd7XmAj5Kjw8LotOSFI3wMsCwrxzL/T1AWD+9YkEYzi1ZxW1IsCQBCOsiFO4CPnKPAwtSq0W/CrIxEdE14s6vDv1P1QgLi22dUkGTmhIgpljzpsBOUSMs3l6xNWIdJTUlE42k7R/rrCXwOfKDuHoBIOy6pI+IgXB2MC1hGxOogLJmGiNe0sF0cvgFcW/bsKBt+vLwMzcwhOBvesTnuKdaYV3QLgofsW8/KsrcoUM94mM+9G8L3BA4dFbCsB/1Hpb6TmhhxHM36VRZIJ5VSk5b01lp54JxHZ5lmLEGmIapouBL5nqLii1TuGfsOiPjAunLh32+DswgIARLhRkMJBVmUJAUmMFBOmBWmt4oIBGYxqF8NBAFwyY5s/8ZjArS1Qb+QWx0vgBNSfcj+ggjkQAAAABJRU5ErkJggg=="

      event.target.parentElement.firstElementChild.setAttribute("src", newSrc)
      event.target.parentElement.classList.toggle("box_focused")
    },
    changeKeyword(keyword) {
      // console.log(keyword)

      // axios({
      //   method: "GET",
      //   url: `${API_URL}/movies/search/${keyword}`,
      // })
      //   .then((res) => {
      //     this.searched_movies = res.data
      //   })
      //   .catch((err) => {
      //     console.log(err)
      //   })

      this.keyword = keyword.target.value
    },
    searchBaro() {
      const keyword = this.keyword
      axios({
        method: "GET",
        url: `${API_URL}/movies/search/${keyword}`,
      })
        .then((res) => {
          this.searched_movies = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  created() {
    window.scrollTo(0, 0)
    this.keyword = this.$store.state.keyword
    const keyword = this.keyword
    axios({
      method: "GET",
      url: `${API_URL}/movies/search/${keyword}`,
    })
      .then((res) => {
        this.searched_movies = res.data
      })
      .catch((err) => {
        console.log(err)
      })

    this.$store.dispatch("searchKeyword", null)
  },
  // watch: {
  //   keyword() {
  //     const keyword = this.keyword

  //     axios({
  //       method: "GET",
  //       url: `${API_URL}/movies/search/${keyword}`,
  //     })
  //       .then((res) => {
  //         this.searched_movies = res.data
  //       })
  //       .catch((err) => {
  //         console.log(err)
  //       })
  //   }
  // },
}
</script>

<style>
.search_big_box {
  display: flex;
  flex-direction: column;
  /* justify-content: center; */
  /* align-items: center; */
  margin-left: 300px;
  width: 100%;
  height: 100%;
  padding-top: 60px;
}

.search_middle_box {
  width: 400px;
  height: 44px;
  border-radius: 6px;
  display: flex;
  background-color: #30333e;
}

.search_small_box {
  width: 340px;
  border: none;
  outline: none;
  margin-left: 4px;
  margin-top: 2px;
  background-color: #30333e;
  color: white;
}

.icons {
  margin-top: 10px;
  margin-left: 8px;
}

.box_focused {
  border: 1px solid white;
}

.topten_box {
  margin-top: 20px;
}

.toptenComponentList_box {
  display: flex !important;
  margin-top: 50px;
  margin-right: 20px;
  margin-left: 0px;
  width: 50%;
}

.content-list {
  display: flex;
  gap: 0.5rem;
  overflow-x: scroll;
  scroll-behavior: smooth;
  display: none;
}

.components_box {
  display: flex;
}

.search_result_box {
  margin-top: 100px;
}
</style>