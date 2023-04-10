import { describe, it, expect } from 'vitest'

import { mount } from '@vue/test-utils'
import ITCConvertTool from '../ITCConvertTool.vue'

describe('ITCConvertTool', () => {
    it('render properly', () => {
        const wrapper = mount(ITCConvertTool);
        expect(wrapper.text()).toContain('Add image files here');
    });
    
    it('input file should be rendered properly', () => {
        const wrapper = mount(ITCConvertTool);
        expect(wrapper.find("input[type='file']").attributes('accept')).toContain('.jpg, .jpeg, .png, .webp');
    });

    it('input file should support multiple file select', () => {
        const wrapper = mount(ITCConvertTool);
        expect(wrapper.find("input[type='file']").attributes('multiple')).toBeDefined();
    });
    
    it('convert to radio inputs should have the following values', () => {
        const wrapper = mount(ITCConvertTool);
        const expectedValues = ['JPG', 'PNG', 'WEBP'];
        const query = wrapper.findAll(".form__group--radio > input");
        for (let i = 0; i < query.length; i++) {
            const $input = query[i];
            const value = $input.element.value;
            expect(expectedValues.indexOf(value)).not.toBe(-1);
        }
    });
});