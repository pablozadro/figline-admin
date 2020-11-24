/******/ (() => { // webpackBootstrap
/******/ 	"use strict";
/******/ 	var __webpack_modules__ = ({

/***/ "../../../../Core/core-radio/index.js":
/*!********************************************!*\
  !*** ../../../../Core/core-radio/index.js ***!
  \********************************************/
/*! namespace exports */
/*! export default [provided] [no usage info] [missing usage info prevents renaming] */
/*! other exports [not provided] [no usage info] */
/*! runtime requirements: __webpack_require__, __webpack_exports__, __webpack_require__.r, __webpack_require__.d, __webpack_require__.* */
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => __WEBPACK_DEFAULT_EXPORT__
/* harmony export */ });
/* harmony import */ var core_types__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! core-types */ "../../../../Core/core-types/index.js");

/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ({
  topics: {},
  tokenID: 0,
  subscribe: function (topic, callback) {
    if (!core_types__WEBPACK_IMPORTED_MODULE_0__.default.is(topic).string()) {
      console.warn('topic must be a string');
      return;
    }

    if (!core_types__WEBPACK_IMPORTED_MODULE_0__.default.is(callback).function()) {
      console.warn('callback should be a function');
      return;
    }

    if (!this.topics[topic]) {
      this.topics[topic] = [];
    }

    const token = this.tokenID++;
    this.topics[topic].push({
      token: token,
      callback: callback
    });
    return token;
  },
  publish: function (topic, context = {}) {
    if (!core_types__WEBPACK_IMPORTED_MODULE_0__.default.is(topic).string()) {
      console.warn('topic must be a string');
      return;
    }

    if (!this.topics[topic]) {
      console.warn(`there is no subscriber to the topic ${topic}`);
      return;
    }

    this.topics[topic].forEach(callback => {
      callback.callback(context);
    });
  },
  unsubscribe: function (topic, token) {
    if (!core_types__WEBPACK_IMPORTED_MODULE_0__.default.is(topic).string()) {
      console.warn('topic must be a string');
      return;
    }

    if (!core_types__WEBPACK_IMPORTED_MODULE_0__.default.is(token).number()) {
      console.warn('token must be a number');
      return;
    }

    if (!this.topics[topic]) {
      console.warn(`topic ${topic} does not exists`);
      return;
    }

    this.topics[topic].forEach(callback => {
      if (callback.token === token) {
        this.topics[topic].splice(this.tokenID - 1, 1);
      }
    });
  },
  restore: function () {
    this.topics = {};
    this.tokenID = 0;
  }
});

/***/ }),

/***/ "../../../../Core/core-types/index.js":
/*!********************************************!*\
  !*** ../../../../Core/core-types/index.js ***!
  \********************************************/
/*! namespace exports */
/*! export default [provided] [no usage info] [missing usage info prevents renaming] */
/*! other exports [not provided] [no usage info] */
/*! runtime requirements: __webpack_exports__, __webpack_require__.r, __webpack_require__.d, __webpack_require__.* */
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => __WEBPACK_DEFAULT_EXPORT__
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ({
  _type: null,
  is: function (el) {
    this._type = el.constructor.name.toString();
    return this;
  },
  string: function () {
    return this._type === 'String';
  },
  number: function () {
    return this._type === 'Number';
  },
  array: function () {
    return this._type === 'Array';
  },
  object: function () {
    return this._type === 'Object';
  },
  function: function () {
    return this._type === 'Function';
  }
});

/***/ }),

/***/ "./src/js/app.js":
/*!***********************!*\
  !*** ./src/js/app.js ***!
  \***********************/
/*! namespace exports */
/*! export default [provided] [no usage info] [missing usage info prevents renaming] */
/*! other exports [not provided] [no usage info] */
/*! runtime requirements: __webpack_require__, __webpack_exports__, __webpack_require__.r, __webpack_require__.d, __webpack_require__.* */
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => __WEBPACK_DEFAULT_EXPORT__
/* harmony export */ });
/* harmony import */ var core_radio__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! core-radio */ "../../../../Core/core-radio/index.js");
/* harmony import */ var _components_topnav__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @/components/topnav */ "./src/js/components/topnav.js");
/* harmony import */ var _components_modal__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @/components/modal */ "./src/js/components/modal.js");



/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ({
  main: function main() {
    document.addEventListener('click', function (e) {
      if (!e.target.dataset.event) return;
      var dataset = Object.assign({}, e.target.dataset);
      core_radio__WEBPACK_IMPORTED_MODULE_0__.default.publish(dataset.event, {
        e: e,
        dataset: dataset
      });
    });
    _components_topnav__WEBPACK_IMPORTED_MODULE_1__.default.main();
    _components_modal__WEBPACK_IMPORTED_MODULE_2__.default.main();
  }
});

/***/ }),

/***/ "./src/js/components/modal.js":
/*!************************************!*\
  !*** ./src/js/components/modal.js ***!
  \************************************/
/*! namespace exports */
/*! export default [provided] [no usage info] [missing usage info prevents renaming] */
/*! other exports [not provided] [no usage info] */
/*! runtime requirements: __webpack_require__, __webpack_exports__, __webpack_require__.r, __webpack_require__.d, __webpack_require__.* */
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => __WEBPACK_DEFAULT_EXPORT__
/* harmony export */ });
/* harmony import */ var core_radio__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! core-radio */ "../../../../Core/core-radio/index.js");

/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ({
  main: function main() {
    var modalsById = {};
    var modals = document.querySelectorAll('.modal');

    if (!modals) {
      console.warn('There is no modals. Exit.');
      return;
    }

    modals.forEach(function (modal) {
      var id = modal.getAttribute('id');

      if (!id) {
        console.warn('Modal ID is required');
        return;
      }

      modalsById[id] = modal;
    });
    core_radio__WEBPACK_IMPORTED_MODULE_0__.default.subscribe('modal:open', function (context) {
      if (modalsById[context.dataset.target]) {
        modalsById[context.dataset.target].classList.add('is--active');
      }
    });
    core_radio__WEBPACK_IMPORTED_MODULE_0__.default.subscribe('modal:close', function (context) {
      if (modalsById[context.dataset.target]) {
        modalsById[context.dataset.target].classList.remove('is--active');
      }
    });
  }
});

/***/ }),

/***/ "./src/js/components/topnav.js":
/*!*************************************!*\
  !*** ./src/js/components/topnav.js ***!
  \*************************************/
/*! namespace exports */
/*! export default [provided] [no usage info] [missing usage info prevents renaming] */
/*! other exports [not provided] [no usage info] */
/*! runtime requirements: __webpack_require__, __webpack_exports__, __webpack_require__.r, __webpack_require__.d, __webpack_require__.* */
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => __WEBPACK_DEFAULT_EXPORT__
/* harmony export */ });
/* harmony import */ var core_radio__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! core-radio */ "../../../../Core/core-radio/index.js");

/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ({
  main: function main() {
    var content = document.querySelector('.topnav__content');

    if (!content) {
      console.warn('There is no topnav content');
      return;
    }

    core_radio__WEBPACK_IMPORTED_MODULE_0__.default.subscribe('topnav:toggle', function () {
      content.classList.toggle('is--active');
    });
  }
});

/***/ }),

/***/ "./src/js/index.js":
/*!*************************!*\
  !*** ./src/js/index.js ***!
  \*************************/
/*! namespace exports */
/*! exports [not provided] [no usage info] */
/*! runtime requirements: __webpack_require__, __webpack_require__.r, __webpack_exports__, __webpack_require__.* */
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _app__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @/app */ "./src/js/app.js");

_app__WEBPACK_IMPORTED_MODULE_0__.default.main();

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	// The module cache
/******/ 	var __webpack_module_cache__ = {};
/******/ 	
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/ 		// Check if module is in cache
/******/ 		if(__webpack_module_cache__[moduleId]) {
/******/ 			return __webpack_module_cache__[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = __webpack_module_cache__[moduleId] = {
/******/ 			// no module.id needed
/******/ 			// no module.loaded needed
/******/ 			exports: {}
/******/ 		};
/******/ 	
/******/ 		// Execute the module function
/******/ 		__webpack_modules__[moduleId](module, module.exports, __webpack_require__);
/******/ 	
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/ 	
/************************************************************************/
/******/ 	/* webpack/runtime/define property getters */
/******/ 	(() => {
/******/ 		// define getter functions for harmony exports
/******/ 		__webpack_require__.d = (exports, definition) => {
/******/ 			for(var key in definition) {
/******/ 				if(__webpack_require__.o(definition, key) && !__webpack_require__.o(exports, key)) {
/******/ 					Object.defineProperty(exports, key, { enumerable: true, get: definition[key] });
/******/ 				}
/******/ 			}
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/hasOwnProperty shorthand */
/******/ 	(() => {
/******/ 		__webpack_require__.o = (obj, prop) => Object.prototype.hasOwnProperty.call(obj, prop)
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/make namespace object */
/******/ 	(() => {
/******/ 		// define __esModule on exports
/******/ 		__webpack_require__.r = (exports) => {
/******/ 			if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 				Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 			}
/******/ 			Object.defineProperty(exports, '__esModule', { value: true });
/******/ 		};
/******/ 	})();
/******/ 	
/************************************************************************/
/******/ 	// startup
/******/ 	// Load entry module
/******/ 	__webpack_require__("./src/js/index.js");
/******/ 	// This entry module used 'exports' so it can't be inlined
/******/ })()
;
//# sourceMappingURL=core.bundle.js.map