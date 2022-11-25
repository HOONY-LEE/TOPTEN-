<template>
  <div class="topten_box lay">
    <h3>TOP 10 인기</h3>
    <div class="components_box lay2">
      <ToptenComponentList :movie="movie" v-for="(movie, index) in popularity" :key="index" :index="index"
        class="toptenComponentList_box row row-cols-12 row-cols-md-12 g-2 lay2"></ToptenComponentList>
    </div>
    <h3>TOP 10 평점</h3>
    <div class="components_box lay2">
      <ToptenComponentList :movie="movie" v-for="(movie, index) in vote" :key="index" :index="index"
        class="toptenComponentList_box row row-cols-12 row-cols-md-12 g-2 lay2"></ToptenComponentList>
    </div>
    <h3>TOP 10 최신개봉작</h3>
    <div class="components_box lay2">
      <ToptenComponentList :movie="movie" v-for="(movie, index) in recent" :key="index" :index="index"
        class="toptenComponentList_box row row-cols-12 row-cols-md-12 g-2 lay2"></ToptenComponentList>
    </div>
    <h3>TOP 10 개봉예정작</h3>
    <div class="components_box lay2">
      <ToptenComponentList :movie="movie" v-for="(movie, index) in soon" :key="index" :index="index"
        class="toptenComponentList_box row row-cols-12 row-cols-md-12 g-2 lay2"></ToptenComponentList>
    </div>
    <h3>TOP 10 힙</h3>
    <div class="components_box lay2">
      <ToptenComponentList :movie="movie" v-for="(movie, index) in hip" :key="index" :index="index"
        class="toptenComponentList_box row row-cols-12 row-cols-md-12 g-2 lay2"></ToptenComponentList>
    </div>
    <h3>TOP 10 저평가</h3>
    <div class="components_box lay2">
      <ToptenComponentList :movie="movie" v-for="(movie, index) in trash" :key="index" :index="index"
        class="toptenComponentList_box row row-cols-12 row-cols-md-12 g-2 lay2"></ToptenComponentList>
    </div>
  </div>
</template>

<script>
import ToptenComponentList from "./ToptenComponentList.vue"

export default {
  name: "HomeComponent",
  computed: {
    popularity() {
      return this.$store.state.popularity
    },
    vote() {
      return this.$store.state.vote
    },
    recent() {
      return this.$store.state.recent
    },
    soon() {
      return this.$store.state.soon
    },
    hip() {
      return this.$store.state.hip
    },
    trash() {
      return this.$store.state.trash
    },
  },
  components: { ToptenComponentList },
}
</script>

<style>
.topten_box {
  margin-top: 20px;
}

.toptenComponentList_box {
  display: flex !important;
  margin-top: 50px !important;
  margin-right: 20px !important;
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
  margin-top: -30px;
}
</style>
