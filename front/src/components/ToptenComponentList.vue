<template>
  <div class="toptenList_box">
    <div class="col box1">
      <div class="col">
        <div class="card box2" @click="goDetail">
          <div class="top10_tag">
            <h4>{{ index + 1 }}</h4>
          </div>
          <img :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`" alt="" />
          <div class="card-body">
            <p id="card_title" class="card-title">{{ titles }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ToptenComponentList",
  props: {
    movie: Object,
    index: Number,
  },
  computed: {
    titles() {
      const title = this.movie.title
      return title.substring(0, 14)
    },
  },
  methods: {
    goDetail() {
      this.$router.push({ name: 'detail', params: { movieId: this.movie.id } })
    }
  }
}
</script>

<style>
.toptenList_box {
  float: left;
  margin-left: 100px;
  /* width: 2000px; */
}

.card>img {
  width: 240px;
  height: 300px;
  border-top-left-radius: 6px;
  border-top-right-radius: 6px;
}

.box1 {
  display: inline-block !important;
  margin: 0px !important;
  padding: 10px !important;
}

.top10_tag {
  background-color: crimson;
  border-radius: 6px;
  width: 30px;
  height: 34px;
  color: white;
  position: absolute;
  text-align: center;
  padding-top: 4px;
  border: 1px solid crimson;
  outline: 2px dashed crimson;
}

.card {
  border: none !important;
  width: 240px;
  height: 356px !important;
  background-color: #141517 !important;
  color: white;
  margin-right: 20px;
}

.card-body {
  background-color: none !important;
}

.card-title {
  text-align: center;
  color: darkgray;
  font-size: large;
  padding-top: 0px;

}



.box2:hover #card_title {
  color: white !important;
}

.box2:hover img {
  width: 250px !important;
  height: 310px !important;
}


.box2:hover {
  width: 250px !important;
  height: 360px !important;
  outline: 3.4px solid crimson !important;
}
</style>
