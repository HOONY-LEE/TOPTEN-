<template>
  <div class="home lay">
    <div>
      <!-- <img alt="Topten Logo" src="../assets/topten_logo.png" width="100px" /> -->
      <h1>장르 TOPTEN</h1>
      <!-- <div id="root"></div> -->
      <ToptenComponent></ToptenComponent>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

import ToptenComponent from '@/components/ToptenComponent.vue';

export default {
  name: "CategoryView",
  components: { ToptenComponent, },
  created() {
    window.scrollTo(0, 0)
    this.getMovies()

  },
  methods: {
    getMovies() {
      this.$store.dispatch("getMovies")
    },
  },
}
</script>

<style>
h1 {
  font-weight: 600;
}
</style>