<template>
  <div class="">
    <h1>TOP10 영화 추천</h1>
    <ToptenComponentList :movie="movie" v-for="(movie, index) in movies" :key="index"
      class="toptenComponentList_box row row-cols-2 row-cols-3 g-1 lay2"></ToptenComponentList>
  </div>
</template>

<script>
import ToptenComponentList from "@/components/ToptenComponentList.vue"

export default {
  name: "ToptenView",
  components: { ToptenComponentList },
  computed: {
    movies() {
      return this.$store.state.movies
    },
  },
  created() {
    window.scrollTo(0, 0)
  },
}
</script>

<style>
.toptenComponentList_box {
  display: flex;
  margin-top: 50px;
  margin-left: 20px;
}
</style>
