import { describe, it, expect } from 'vitest'

import { mount } from '@vue/test-utils'
import ITCButtonLink from '../ITCButtonLink.vue'

describe('ITCButton', () => {
  it('render properly with prop class', () => {
    const wrapper = mount(ITCButtonLink, { props: { class: 'form__button form__button--file' } });
    expect(wrapper.find("itc-button--link").attributes('class')).toContain('form__button form__button--file');
  });

  it('render properly with slot', () => {
    const wrapper = mount(ITCButtonLink, { slots: { default: 'test' } });
    expect(wrapper.text()).toContain('test');
  });

  it('render properly with props disabled', () => {
    const wrapper = mount(ITCButtonLink, { props: { disabled: true } });
    expect(wrapper.find('a').attributes('disabled')).toContain('disabled');
  });
})
