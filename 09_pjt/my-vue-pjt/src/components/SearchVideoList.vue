<template>
  <div class="search-video-list">
    <div class="row row-cols-1 row-cols-md-3 g-4">
      <div v-for="(card, idx) in videos" :key="idx">
        <div class="col">
          <div class="card h-100">
            <img :src="card.imgSrc" class="card-img-top" alt="">
            <div class="card-body">
              <p class="card-text">{{ card.title }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import 

export default {
  name: 'SearchVideoList',
  computed: {
    videos() {
      return this.$store.state.searchVideos
    }
  },
  // created() {
  //   this.$store.dispatch('getSearchVideo')
  // },
  methods: {
  }
}
</script>

<style>
.search-video-list {
  text-align: left;
}
</style>