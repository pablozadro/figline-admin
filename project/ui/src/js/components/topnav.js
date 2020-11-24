import CoreRadio from 'core-radio';

export default {
  main: function() {
    const content = document.querySelector('.topnav__content');

    if(!content) {
      console.warn('There is no topnav content');
      return;
    }

    CoreRadio.subscribe('topnav:toggle', () => {
      content.classList.toggle('is--active');
    });
  }
};
