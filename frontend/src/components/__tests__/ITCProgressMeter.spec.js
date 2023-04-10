import { describe, it, expect } from 'vitest'

import { mount } from '@vue/test-utils'
import ITCProgressMeter from '../ITCProgressMeter.vue'

describe('ITCProgressMeter', () => {
  it('render properly with class props', () => {
    const wrapper = mount(ITCProgressMeter, { props: { class: 'complete' } });
    expect(wrapper.text()).toContain('complete');
  });

  it('render properly with correct color given class complete', () => {
    // checks if "background-color: var(--third)" is appied to the element ".itc-progress-meter__bar" 
    const wrapper = mount(ITCProgressMeter, { props: { class: 'complete' } });
    expect(wrapper.find('.itc-progress-meter__bar').attributes('style')).toContain('background-color: var(--third)');
  });

  it('render properly with correct color given class error', () => {
    // checks if "background-color: var(--fourth)" is appied to the element ".itc-progress-meter__bar" 
    const wrapper = mount(ITCProgressMeter, { props: { class: 'error' } });
    expect(wrapper.find('.itc-progress-meter__bar').attributes('style')).toContain('background-color: var(--fourth)');
  });
})
