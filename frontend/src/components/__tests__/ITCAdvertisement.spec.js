// it should test the following:
// 1. on load, it should add google adsense script to <head>
// 2. google adsense script in <head> should be loaded only once
// 3. google adsense should be rendered properly

import {
  describe,
  it,
  expect
} from 'vitest'

import {
  mount
} from '@vue/test-utils'
import ITCAdvertisement from '../ITCAdvertisement.vue'

describe('ITCAdvertisement', () => {
  it('should add google adsense script to <head>', () => {
    mount(ITCAdvertisement, {
      props: {
        "data-ad-client": 'test1',
        'data-ad-slot': '12345',
        'data-ad-format': 'auto',
        'data-full-width-response': 'false'
      }
    });

    expect(document.head.innerHTML).toContain(`pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=test1`);
    expect(document.head.innerHTML).toContain(`class="adsbygoogle-test1"`);
  });

  it('google adsense props should be rendered properly', () => {
    const wrapper = mount(ITCAdvertisement, {
      props: {
        "data-ad-client": 'test1',
        'data-ad-slot': '12345',
        'data-ad-format': 'auto',
        'data-full-width-response': 'false'
      }
    });

    expect(wrapper.find('ins').attributes('class')).toContain('adsbygoogle');
    expect(wrapper.find('ins').attributes('data-ad-client')).toContain('test1');
    expect(wrapper.find('ins').attributes('data-ad-slot')).toContain('12345');
    expect(wrapper.find('ins').attributes('data-ad-format')).toContain('auto');
    expect(wrapper.find('ins').attributes('data-full-width-response')).toContain('false');
  });
});