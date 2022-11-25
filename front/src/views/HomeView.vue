<template>
  <div class="home lay">
    <div>
      <!-- <img alt="Topten Logo" src="../assets/topten_logo.png" width="100px" /> -->
      <h1>TOPTEN</h1>
      <!-- <div id="root"></div> -->
      <HomeComponent></HomeComponent>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

import HomeComponent from '@/components/HomeComponent.vue';

export default {
  name: "HomeView",
  components: { HomeComponent, },
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