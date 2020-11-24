import CoreRadio from 'core-radio';

export default {
  main: function() {
    let modalsById = {};
    let modals = document.querySelectorAll('.modal');

    if(!modals) {
      console.warn('There is no modals. Exit.');
      return;
    }

    modals.forEach(modal => {
      let id = modal.getAttribute('id');
      if(!id) {
        console.warn('Modal ID is required');
        return;
      }
      modalsById[id] = modal;
    });

    CoreRadio.subscribe('modal:open', context => {
      if(modalsById[context.dataset.target]) {
        modalsById[context.dataset.target].classList.add('is--active');
      }
    });

    CoreRadio.subscribe('modal:close', context => {
      if(modalsById[context.dataset.target]) {
        modalsById[context.dataset.target].classList.remove('is--active');
      }
    });
  }
};
