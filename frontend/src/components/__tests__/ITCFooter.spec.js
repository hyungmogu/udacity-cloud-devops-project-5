import { describe, it, expect } from 'vitest'

import { mount } from '@vue/test-utils'
import ITCFooter from '../ITCFooter.vue'

describe('ITCFooter', () => {
    it('render properly', () => {
        const wrapper = mount(ITCFooter);
        expect(wrapper.text()).toContain('Software Engineer Who');
    });
    
    it('render properly with router-link ".itc-footer__logo-link"', () => {
        const wrapper = mount(ITCFooter);
        expect(wrapper.find('.itc-footer__logo-link').attributes('to')).toContain('/');
    });
    
    it('render properly with ".itc-footer__sns-link.itc-footer__sns-link--portfolio"', () => {
        const wrapper = mount(ITCFooter);
        expect(wrapper.find('.itc-footer__sns-link.itc-footer__sns-link--portfolio').attributes('href')).toContain('https://hyungmogu.com');
    });
    
    it('render properly with ".itc-footer__sns-link.itc-footer__sns-link--github"', () => {
        const wrapper = mount(ITCFooter);
        expect(wrapper.find('.itc-footer__sns-link.itc-footer__sns-link--github').attributes('href')).toContain('https://github.com/hyungmogu');
    });
 
    it('render properly with ".itc-footer__sns-link.itc-footer__sns-link--linkedIn"', () => {
        const wrapper = mount(ITCFooter);
        expect(wrapper.find('.itc-footer__sns-link.itc-footer__sns-link--linkedIn').attributes('href')).toContain('https://www.linkedin.com/in/hyungmo-gu');
    });
});