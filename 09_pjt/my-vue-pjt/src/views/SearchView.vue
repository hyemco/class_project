<template>
  <div class="searchView">
    <router-link :to="{name: 'home'}" class="text-decoration-none">
      <div class="mb-3 text-secondary" >
        <b-icon-arrow-left class="me-2"></b-icon-arrow-left>뒤로가기
      </div>
    </router-link>
    
    <h1>비디오 검색</h1>
    <SearchInput />
    <SearchVideoList />

    <div class="card-group">
      
    </div>
  </div>
</template>

<script>
import SearchInput from '@/components/SearchInput'
import SearchVideoList from '@/components/SearchVideoList'

export default {
  name: 'SearchView',
  components: {
    SearchInput,
    SearchVideoList
  }
}
</script>

<style>
.searchView {
  text-align: left;
}

img {
  height: 300px;
}
</style>