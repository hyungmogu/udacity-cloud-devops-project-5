import { describe, it, expect } from 'vitest'

import { mount } from '@vue/test-utils'
import ITCButton from '../ITCButton.vue'

describe('ITCButton', () => {
  it('render properly with prop class', () => {
    const wrapper = mount(ITCButton, { props: { class: 'form__button form__button--file' } });
    expect(wrapper.find(".itc-button").attributes('class')).toContain('form__button form__button--file');
  });

  it('render properly with slot', () => {
    const wrapper = mount(ITCButton, { slots: { default: 'test' } });
    expect(wrapper.text()).toContain('test');
  });

  it('render properly with props disabled', () => {
    const wrapper = mount(ITCButton, { props: { disabled: true } });
    expect(wrapper.find('button').attributes().disabled).not.toBeUndefined();
  });
})
