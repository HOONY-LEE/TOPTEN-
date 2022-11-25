<template>
  <div class="topten_box lay">
    <h3>TOP 10 액션</h3>
    <div class="components_box lay2">
      <ToptenComponentList :movie="movie" v-for="(movie, index) in action" :key="index" :index="index"
        class="toptenComponentList_box row row-cols-12 row-cols-md-12 g-2 lay2"></ToptenComponentList>
    </div>
    <h3>TOP 10 모험</h3>
    <div class="components_box lay2">
      <ToptenComponentList :movie="movie" v-for="(movie, index) in adventure" :key="index" :index="index"
        class="toptenComponentList_box row row-cols-12 row-cols-md-12 g-2 lay2"></ToptenComponentList>
    </div>
    <h3>TOP 10 애니메이션</h3>
    <div class="components_box lay2">
      <ToptenComponentList :movie="movie" v-for="(movie, index) in animation" :key="index" :index="index"
        class="toptenComponentList_box row row-cols-12 row-cols-md-12 g-2 lay2"></ToptenComponentList>
    </div>
    <h3>TOP 10 코미디</h3>
    <div class="components_box lay2">
      <ToptenComponentList :movie="movie" v-for="(movie, index) in comedy" :key="index" :index="index"
        class="toptenComponentList_box row row-cols-12 row-cols-md-12 g-2 lay2"></ToptenComponentList>
    </div>
    <h3>TOP 10 범죄</h3>
    <div class="components_box lay2">
      <ToptenComponentList :movie="movie" v-for="(movie, index) in crime" :key="index" :index="index"
        class="toptenComponentList_box row row-cols-12 row-cols-md-12 g-2 lay2"></ToptenComponentList>
    </div>
    <h3>TOP 10 드라마</h3>
    <div class="components_box lay2">
      <ToptenComponentList :movie="movie" v-for="(movie, index) in drama" :key="index" :index="index"
        class="toptenComponentList_box row row-cols-12 row-cols-md-12 g-2 lay2"></ToptenComponentList>
    </div>
    <h3>TOP 10 가족</h3>
    <div class="components_box lay2">
      <ToptenComponentList :movie="movie" v-for="(movie, index) in family" :key="index" :index="index"
        class="toptenComponentList_box row row-cols-12 row-cols-md-12 g-2 lay2"></ToptenComponentList>
    </div>
    <h3>TOP 10 판타지</h3>
    <div class="components_box lay2">
      <ToptenComponentList :movie="movie" v-for="(movie, index) in fantasy" :key="index" :index="index"
        class="toptenComponentList_box row row-cols-12 row-cols-md-12 g-2 lay2"></ToptenComponentList>
    </div>
    <h3>TOP 10 역사</h3>
    <div class="components_box lay2">
      <ToptenComponentList :movie="movie" v-for="(movie, index) in history" :key="index" :index="index"
        class="toptenComponentList_box row row-cols-12 row-cols-md-12 g-2 lay2"></ToptenComponentList>
    </div>
    <h3>TOP 10 공포</h3>
    <div class="components_box lay2">
      <ToptenComponentList :movie="movie" v-for="(movie, index) in horror" :key="index" :index="index"
        class="toptenComponentList_box row row-cols-12 row-cols-md-12 g-2 lay2"></ToptenComponentList>
    </div>
    <h3>TOP 10 음악</h3>
    <div class="components_box lay2">
      <ToptenComponentList :movie="movie" v-for="(movie, index) in music" :key="index" :index="index"
        class="toptenComponentList_box row row-cols-12 row-cols-md-12 g-2 lay2"></ToptenComponentList>
    </div>
    <h3>TOP 10 미스터리</h3>
    <div class="components_box lay2">
      <ToptenComponentList :movie="movie" v-for="(movie, index) in mystery" :key="index" :index="index"
        class="toptenComponentList_box row row-cols-12 row-cols-md-12 g-2 lay2"></ToptenComponentList>
    </div>
    <h3>TOP 10 로맨스</h3>
    <div class="components_box lay2">
      <ToptenComponentList :movie="movie" v-for="(movie, index) in romance" :key="index" :index="index"
        class="toptenComponentList_box row row-cols-12 row-cols-md-12 g-2 lay2"></ToptenComponentList>
    </div>
    <h3>TOP 10 SF</h3>
    <div class="components_box lay2">
      <ToptenComponentList :movie="movie" v-for="(movie, index) in sf" :key="index" :index="index"
        class="toptenComponentList_box row row-cols-12 row-cols-md-12 g-2 lay2"></ToptenComponentList>
    </div>
    <h3>TOP 10 스릴러</h3>
    <div class="components_box lay2">
      <ToptenComponentList :movie="movie" v-for="(movie, index) in thriller" :key="index" :index="index"
        class="toptenComponentList_box row row-cols-12 row-cols-md-12 g-2 lay2"></ToptenComponentList>
    </div>
    <h3>TOP 10 전쟁</h3>
    <div class="components_box lay2">
      <ToptenComponentList :movie="movie" v-for="(movie, index) in war" :key="index" :index="index"
        class="toptenComponentList_box row row-cols-12 row-cols-md-12 g-2 lay2"></ToptenComponentList>
    </div>
  </div>
</template>

<script>
import ToptenComponentList from "./ToptenComponentList.vue"

export default {
  name: "ToptenComponent",
  computed: {
    action() {
      return this.$store.state.action
    },
    adventure() {
      return this.$store.state.adventure
    },
    animation() {
      return this.$store.state.animation
    },
    comedy() {
      return this.$store.state.comedy
    },
    crime() {
      return this.$store.state.crime
    },
    drama() {
      return this.$store.state.drama
    },
    family() {
      return this.$store.state.family
    },
    fantasy() {
      return this.$store.state.fantasy
    },
    history() {
      return this.$store.state.history
    },
    horror() {
      return this.$store.state.horror
    },
    music() {
      return this.$store.state.music
    },
    mystery() {
      return this.$store.state.mystery
    },
    romance() {
      return this.$store.state.romance
    },
    sf() {
      return this.$store.state.sf
    },
    thriller() {
      return this.$store.state.thriller
    },
    war() {
      return this.$store.state.war
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
