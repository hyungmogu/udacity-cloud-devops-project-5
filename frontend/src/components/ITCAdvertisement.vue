
<template>
  <div class="itc-advertisement">
    <small class="itc-advertisement__title">This is advertisement</small>
    <div class="itc-advertisement__banner">
      <!-- Homepage Leaderboard -->
      <ins class="adsbygoogle" v-bind:class="className"
      v-bind:data-ad-client="dataAdClient"
      v-bind:data-ad-slot="dataAdSlot"></ins>
    </div>
  </div>
</template>
<script>
export default {
  props:{
    className:{
      type:String,
      default:'',
    },
    dataAdClient:{
      type:String,
      default:'',
    },
    dataAdSlot: {
     type: String,
     default: ''
    },
    dataAdFormat: {
     type: String,
     default: 'auto'
    },
    dataFullWidthResponse: {
      type: String,
      default: 'false'
    }
  },
  mounted() {
    this.handleLoadScriptTag();
    this.handleUpdateAdsbygoogle();
  },
  methods: {
    handleLoadScriptTag() {
      const script = document.createElement('script');
      script.src = `https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=${this.dataAdClient}`;
      script.async = true;
      script.crossOrigin = 'anonymous';
      document.head.appendChild(script);
    },
    handleUpdateAdsbygoogle() {
      window.adsbygoogle = window.adsbygoogle || [];
      window.adsbygoogle.push({});
    }
  }
};
</script>
<style lang="scss" scoped>
.itc-advertisement {
  &__title {
    text-align: center;
    display: block;
    margin: 0 0 10px 0;
  }

  &__banner {
    aspect-ratio: 728 / 90;
    background-color: var(--gray-3);
    width: 100%;
    max-width: 728px;
    margin: 0 auto;
  }
}
</style>
