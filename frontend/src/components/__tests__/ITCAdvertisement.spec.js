import { describe, it, expect } from 'vitest'

import { mount } from '@vue/test-utils'
import ITCButton from '../ITCButton.vue'

describe('ITCButton', () => {
  it('renders properly', () => {
    const wrapper = mount(ITCButton, { props: { msg: 'Hello Vitest' } })
    expect(wrapper.text()).toContain('Hello Vitest')
  })
})
