import { describe, it, expect } from 'vitest'

import { mount } from '@vue/test-utils'
import ITCProgressMeter from '../ITCProgressMeter.vue'

describe('ITCProgressMeter', () => {
  it('render properly with class props', () => {
    const wrapper = mount(ITCProgressMeter, { props: { class: 'complete' } });
    expect(wrapper.find(".itc-progress-meter").attributes('class')).toContain('complete');
  });
})
