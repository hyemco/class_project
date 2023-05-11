<template>
  <div>
    <div class="input-group mb-3">
      <input v-model="searchKeyword" type="text" class="form-control" placeholder="검색어를 입력하세요" aria-label="Recipient's username" aria-describedby="button-addon2">
      <button class="btn btn-success " type="button" id="button-addon2" @click="getSearchVideo">찾기</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SearchInput',
  data() {
    return {
      searchKeyword: null
    }
  },
  methods: {
    getSearchVideo() {
      this.$store.dispatch('getSearchVideo', this.searchKeyword)
    }
  }
}
</script>

<style>

</style>