import { describe, it, expect } from 'vitest'

import { mount } from '@vue/test-utils'
import ITCPageBanner from '../ITCPageBanner.vue'

describe('ITCPageBanner', () => {
    it('render properly', () => {
        const wrapper = mount(ITCPageBanner);
        expect(wrapper.text()).toContain('Convert Any Image Format to Your Preferred File Type');
    });
});
