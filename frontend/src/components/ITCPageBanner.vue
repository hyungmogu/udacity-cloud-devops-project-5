<template>
  <div class="itc-page-banner">
    <div class="itc_page-banner__left">
      <h1 class="itc-page-banner__title">Convert Any Image Format to Your Preferred File Type: <span
          class="emphasized emphasized--one">.jpg</span>, <span class="emphasized emphasized--one">.png</span>, <span
          class="emphasized emphasized--one">.webp</span></h1>
      <p class="itc-page-banner__subtitle">Image format conversion can be done using front-end, but it's done on
        back-end to practice and demonstrate author's system design skills.</p>
    </div>
    <div class="itc_page-banner__right">
      <svg class="itc-page-banner__image" version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
        x="0px" y="0px" viewBox="0 0 512 448" style="enable-background:new 0 0 512 448;" xml:space="preserve">
        <linearGradient id="SVGID_1_" gradientUnits="userSpaceOnUse" x1="-48.9043" y1="620.1898" x2="-47.9043"
          y2="620.1898" gradientTransform="matrix(512 0 0 -448 25039 278069)">
          <stop offset="5.000000e-02" style="stop-color:#FFD568" />
          <stop offset="0.95" style="stop-color:#62C9B7" />
        </linearGradient>
        <path class="st0" d="M0,64C0,28.7,28.7,0,64,0h384c35.3,0,64,28.7,64,64v320c0,35.3-28.7,64-64,64H64c-35.3,0-64-28.7-64-64V64z
	 M323.8,170.5c-4.5-6.6-11.9-10.5-19.8-10.5s-15.4,3.9-19.8,10.5l-87,127.6L170.7,265c-4.6-5.7-11.5-9-18.7-9s-14.2,3.3-18.7,9
	l-64,80c-5.8,7.2-6.9,17.1-2.9,25.4S78.8,384,88,384h96h32h208c8.9,0,17.1-4.9,21.2-12.8s3.6-17.4-1.4-24.7L323.8,170.5L323.8,170.5
	z M112,160c26.5,0,48-21.5,48-48s-21.5-48-48-48s-48,21.5-48,48S85.5,160,112,160z" />
      </svg>
    </div>
  </div>
</template>

<style lang="scss" scoped>
  .itc-page-banner {
    display: grid;
    row-gap: 60px;
    column-gap: 100px;
    align-items: center;

    @media screen and (min-width: 992px) {
      grid-template-columns: repeat(2, 1fr);
      height: 575px;
    }

    &__title {
      max-width: 470px;
      margin: 0 auto 30px auto;
      text-align: center;

      @media screen and (min-width: 992px) {
        max-width: 700px;
        text-align: left;
        margin: 0 0 30px 0;
      }
    }

    &__subtitle {
      max-width: 470px;
      margin: 0 auto;
      text-align: center;

      @media screen and (min-width: 992px) {
        max-width: 700px;
        text-align: left;
        margin: 0;
      }
    }

    .emphasized {
      font-weight: var(--font-weight-bold);

      &--one {
        color: var(--primary);
      }

      &--two {
        color: var(--secondary);
      }

      &--three {
        color: var(--third);
      }
    }

    &__image {
      max-width: 350px;
      display: block;
      margin: 0 auto;

      @media screen and (min-width: 992px) {
        max-width: 100%;
        margin: 0;
        transform: rotate(3deg);
      }
    }

    &__image .st0 {
      fill: url(#SVGID_1_);
    }
  }
</style>