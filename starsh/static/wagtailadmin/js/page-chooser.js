(()=>{"use strict";var t,e={5585:function(t,e,o){var r,n=this&&this.__extends||(r=function(t,e){return r=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(t,e){t.__proto__=e}||function(t,e){for(var o in e)Object.prototype.hasOwnProperty.call(e,o)&&(t[o]=e[o])},r(t,e)},function(t,e){if("function"!=typeof e&&null!==e)throw new TypeError("Class extends value "+String(e)+" is not a constructor or null");function o(){this.constructor=t}r(t,e),t.prototype=null===e?Object.create(e):(o.prototype=e.prototype,new o)});e.__esModule=!0;var a=function(t){function e(e,o,r){var n=this;return n.initialParentId=o,n.options=r,(n=t.call(this,e)||this).modalOnloadHandlers=PAGE_CHOOSER_MODAL_ONLOAD_HANDLERS,n.titleStateKey="adminTitle",n.editUrlStateKey="editUrl",n.chosenResponseName="pageChosen",n}return n(e,t),e.prototype.getStateFromHTML=function(){var e=t.prototype.getStateFromHTML.call(this);return e&&(e.parentId=this.initialParentId),e},e.prototype.getModalUrl=function(){var e=t.prototype.getModalUrl.call(this);return this.state&&this.state.parentId&&(e+=this.state.parentId+"/"),e},e.prototype.getModalUrlParams=function(){var t={page_type:this.options.model_names.join(",")};return this.options.target_pages&&(t.target_pages=this.options.target_pages),this.options.match_subclass&&(t.match_subclass=this.options.match_subclass),this.options.can_choose_root&&(t.can_choose_root="true"),this.options.user_perms&&(t.user_perms=this.options.user_perms),t},e}(o(211).Chooser);window.PageChooser=a,window.createPageChooser=function(t,e,o){return new a(t,e,o)}},5311:t=>{t.exports=jQuery}},o={};function r(t){var n=o[t];if(void 0!==n)return n.exports;var a=o[t]={exports:{}};return e[t].call(a.exports,a,a.exports,r),a.exports}r.m=e,t=[],r.O=(e,o,n,a)=>{if(!o){var i=1/0;for(u=0;u<t.length;u++){for(var[o,n,a]=t[u],s=!0,l=0;l<o.length;l++)(!1&a||i>=a)&&Object.keys(r.O).every((t=>r.O[t](o[l])))?o.splice(l--,1):(s=!1,a<i&&(i=a));if(s){t.splice(u--,1);var p=n();void 0!==p&&(e=p)}}return e}a=a||0;for(var u=t.length;u>0&&t[u-1][2]>a;u--)t[u]=t[u-1];t[u]=[o,n,a]},r.n=t=>{var e=t&&t.__esModule?()=>t.default:()=>t;return r.d(e,{a:e}),e},r.d=(t,e)=>{for(var o in e)r.o(e,o)&&!r.o(t,o)&&Object.defineProperty(t,o,{enumerable:!0,get:e[o]})},r.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(t){if("object"==typeof window)return window}}(),r.o=(t,e)=>Object.prototype.hasOwnProperty.call(t,e),r.r=t=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},r.j=957,(()=>{var t={957:0};r.O.j=e=>0===t[e];var e=(e,o)=>{var n,a,[i,s,l]=o,p=0;if(i.some((e=>0!==t[e]))){for(n in s)r.o(s,n)&&(r.m[n]=s[n]);if(l)var u=l(r)}for(e&&e(o);p<i.length;p++)a=i[p],r.o(t,a)&&t[a]&&t[a][0](),t[a]=0;return r.O(u)},o=globalThis.webpackChunkwagtail=globalThis.webpackChunkwagtail||[];o.forEach(e.bind(null,0)),o.push=e.bind(null,o.push.bind(o))})();var n=r.O(void 0,[751],(()=>r(5585)));n=r.O(n)})();