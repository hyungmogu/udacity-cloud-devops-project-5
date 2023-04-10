// add test cases based on ../ITCConvertTool.vue
// it should do the following:
// 1. render properly (it should contain words 'Add image files here')
// 2. input file should be rendered properly (it should only accept image files including .jpg, .png, .webp) 
// 3. convert to radio inputs (".form__group form__group--radio > input") should have the following values: 'JPG', 'PNG', 'WEBP'

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

        // query selector all .form__group--radio > input
        // expect the value of each input to be either 'JPG', 'PNG', 'WEBP'
        const query = wrapper.findAll(".form__group--radio > input");
        for (let i = 0; i < query.length; i++) {
            const $input = query[i];
            
            // get the value of the input
            // expect the value to be either 'JPG', 'PNG', 'WEBP'
            value = $input.attributes('value');

            expect(['JPG', 'PNG', 'WEBP']).toContain(value);
            
        }

        expect(wrapper.find(".form__group--radio > input").attributes('value')).toContain('JPG');
        expect(wrapper.find(".form__group--radio > input").attributes('value')).toContain('PNG');
        expect(wrapper.find(".form__group--radio > input").attributes('value')).toContain('WEBP');
    });
});