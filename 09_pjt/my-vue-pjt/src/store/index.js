import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

import axios from 'axios'

const YOUTUBE_API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const YOUTUBE_URL = 'https://www.googleapis.com/youtube/v3/search'

export default new Vuex.Store({
  state: {
    searchVideos: [],
  },
  getters: {
  },
  mutations: {
    GET_SEARCH_VIDEO(state, videos) {
      // 검색 결과 초기화
      state.searchVideos.splice(0);

      videos.forEach((video) => {
        const addVideo = {
          imgSrc: video.snippet.thumbnails.high.url,
          title: video.snippet.title
        }
        state.searchVideos.push(addVideo)
      })
    }
  },
  actions: {
    async getSearchVideo(context, searchKeyword) {
      const res = await axios.get(`${YOUTUBE_URL}?key=${YOUTUBE_API_KEY}&part=snippet&type=video&maxResults=16&q=${searchKeyword}`)
      context.commit('GET_SEARCH_VIDEO', res.data.items)
    }
  },
  modules: {
  }
})
